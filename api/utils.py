
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
def send_email_token(email, token):
        subject = 'Your account'
        html_message = loader.render_to_string(
            'api/main_body.html',
            {
                'username': email,
            }
        )
        message = f'Hi http://127.0.0.1:8000/verify/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail(subject, message, email_from, recipient_list,html_message=html_message)
    
        return True