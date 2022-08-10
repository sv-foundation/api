import binascii

from django.core.mail import EmailMessage

from help.models import HelpEmailReceiver
from svfoundation import settings
from svfoundation.celery import app


@app.task
def send_help_email(message, files_data):
    receivers = HelpEmailReceiver.objects.filter(is_active=True).all()
    receivers_emails = [receiver.email for receiver in receivers] or settings.HELP_EMAIL_RECIPIENTS
    mail = EmailMessage(f'Потребую допомоги - з форми на сторінці '
                        f'{settings.WEBSITE_URL}potrebuiu-dopomohy',
                        message,
                        settings.EMAIL_HOST_USER,
                        receivers_emails)
    for file_data in files_data:
        name, content, content_type = file_data
        mail.attach(name, binascii.unhexlify(content.encode()), content_type)
    mail.send(fail_silently=False)
