from django.conf import settings
from kavenegar import KavenegarAPI, APIException, HTTPException


def send_sms(user, message, sender=settings.SMS_SENDER):
    """
    Sends an SMS using the Kavenegar API.
    :param user: User object that includes phone number.
    :param message: The SMS message to be sent.
    :param sender: The SMS number to be sent.
    """
    try:
        api = KavenegarAPI(settings.SMS_API_KEY)
        params = {
            'sender': f'{sender}',  # optional
            'receptor': f'{user.phone}',  # multiple mobile number, split by comma
            'message': f'{user.first_name} {user.last_name} {message}.',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(f"API Error: {e}")
    except HTTPException as e:
        print(f"HTTP Error: {e}")


def subscription_activation(user):
    message = f'{user.first_name} عزیز، اشتراک شما با موفقیت فعال شد.'
    return send_sms(user, message)


def payment_reminder(user):
    message = f'{user.first_name} عزیز، اشتراک شما تا فلان روز به اتمام خواهد رسید.'
    return send_sms(user, message)


def successful_registration(user):
    message = f'{user.first_name} عزیز، ثبت نام شما در تاریخ فلان با موفقیت انجام شد.'
    return send_sms(user, message)


def general_alert(user):
    message = f'{user.first_name} عزیز، اطلاعیه مهمی برای شما داریم.'
    return send_sms(user, message)
