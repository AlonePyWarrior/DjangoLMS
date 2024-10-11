import os
import re

from django.conf import settings
from django.core.exceptions import ValidationError


def is_valid_iran_national_id(nat_id):
    if not re.search(r'^\d{10}$', nat_id): raise ValidationError("!کد ملی وارد شده صحیح نمی باشد")
    check = int(nat_id[9])
    s = sum(int(nat_id[x]) * (10 - x) for x in range(9)) % 11
    if s < 2:
        if not check == s:
            raise ValidationError("!کد ملی وارد شده صحیح نمی باشد")
    else:
        if not check + s == 11:
            raise ValidationError("!کد ملی وارد شده صحیح نمی باشد")


def user_directory_path(instance, filename):
    """
    File will be uploaded to MEDIA_ROOT/profile_images/<user_id>/<filename>
    """
    # Ensure the directory exists (create if necessary)
    user_id = instance.user.id
    path = os.path.join('profile_pics', str(user_id))
    os.makedirs(os.path.join(settings.MEDIA_ROOT, path), exist_ok=True)

    return os.path.join(path, filename)


def phone_check(n):
    phone = ""
    for ch in n:
        if ch.isnumeric():
            phone += ch
    return phone