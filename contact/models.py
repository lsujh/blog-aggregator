from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator

from config.validators import file_size


class Contact(models.Model):
    email = models.EmailField("Email")
    title = models.CharField("Тема", max_length=200)
    message = models.TextField("Повідомлення")
    files = models.FileField("Файл", upload_to="upload/", blank=True,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'pdf', 'doc', 'docx', 'jpg',
                                                                 'xlsx', 'xls']), file_size])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Зворотній зв'язок"
        verbose_name_plural = "Зворотній зв'язок"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("contact:contact_create")
