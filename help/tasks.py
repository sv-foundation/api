import binascii

from django.core.mail import EmailMessage

from svfoundation import settings
from svfoundation.celery import app


@app.task
def send_help_email(message, files_data):
    mail = EmailMessage('Потребую допомоги - з форми на сторінці '
                        'https://beta.svfoundation.org.ua/potrebuiu-dopomohy',
                        message,
                        settings.EMAIL_HOST_USER,
                        settings.HELP_EMAIL_RECIPIENTS)
    for file_data in files_data:
        name, content, content_type = file_data
        mail.attach(name, binascii.unhexlify(content.encode()), content_type)
        # mail.attach(file.name, file.read(), file.content_type)
    mail.send(fail_silently=False)
