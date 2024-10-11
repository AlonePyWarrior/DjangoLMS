from django.views import generic

from . import sms_service


class SendSMSView(generic.View):
    def post(self, request, *args, **kwargs):
        user = ...
        sms_service.subscription_activation(user)
        return 'the response'

