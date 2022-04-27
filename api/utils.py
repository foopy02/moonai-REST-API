
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
def send_email_token(email, token, username):
        subject = 'Подтвердите свою почту'
        html_message = loader.render_to_string(
            'mail_body.html',
            {
                'username': username,
                'link':f'https://moonaifinanceapiendpointdomain.com/api/verify/{token}'
            }
        )
        message = f'https://moonaifinanceapiendpointdomain.com/api/verify/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail(subject, message, email_from, recipient_list,html_message=html_message)
    
        return True