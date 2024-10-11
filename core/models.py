from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField

from core.custom_utils import is_valid_iran_national_id, user_directory_path


class CustomUser(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', _("Male")
        FEMALE = 'F', _("Female")

    first_name = models.CharField(max_length=50, verbose_name=_("Firstname"))
    last_name = models.CharField(max_length=50, verbose_name=_("Lastname"))
    email = models.EmailField(unique=True, verbose_name=_("Email"))
    phone = models.CharField(
        max_length=16,
        default="",
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="شماره تلفن باید با فرمت '+989876543210' وارد شود. حداکثر ۱۵ رقم مجاز است."),
        ],
        verbose_name=_("Phone")
    )
    address = models.TextField(max_length=1000, blank=False, null=True, verbose_name=_("Address"))
    national_id = models.CharField(
        unique=True,
        null=True,
        blank=True,
        max_length=10,
        validators=[is_valid_iran_national_id],
        verbose_name=_("National ID")
    )
    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
        verbose_name=_("Gender")
    )
    profile_img = ResizedImageField(
        upload_to=user_directory_path,
        default=static(settings.DEFAULT_PROFILE_IMG),
        verbose_name=_("Profile Picture")
    )
    birthdate = models.DateField(verbose_name=_("Birth Date"), default=timezone.now)
    city = models.CharField(max_length=50, verbose_name=_("City"))
    province = models.CharField(max_length=50, verbose_name=_("Province"))
    country = models.CharField(max_length=50, verbose_name=_("Country"))

    # username = None
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    # objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("user_update", args=[self.id])

    @property
    def age(self):
        delta = timezone.now().date() - self.birthdate
        return delta.days // 365
