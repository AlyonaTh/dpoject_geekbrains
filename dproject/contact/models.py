from django.db import models


class Contact(models.Model):
    """Contact us"""
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    email = models.EmailField()
    message = models.TextField('Message')
    description = models.TextField('Description')
    img = models.ImageField('Photo', upload_to='image/contact')

    def __str__(self):
        return f'{self.email}, {self.message}'

    class Meta:
        verbose_name = 'Contact'