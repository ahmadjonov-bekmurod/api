from djoser import email
from django.contrib.auth.tokens import default_token_generator
from templated_mail.mail import BaseEmailMessage

from djoser import utils
from djoser.conf import settings


class ActivationEmail(email.ActivationEmail):
    template_name = 'C:\\Users\\ahmad\\OneDrive\\Ishchi stol\\API\\api\\authsystem\\accounts\\templates\\index.html'

    def get_context_data(self):
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["activation_url"] = settings.ACTIVATION_URL.format(**context)
        print(context["activation_url"])
        return context
