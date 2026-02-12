from django.db import models

# Create your models here.
class MyInfo(models.Model):
    name = models.CharField(max_length=100,verbose_name="Имя пользователя")
    photo = models.ImageField(verbose_name="Фото")
    profession = models.CharField(max_length=100,verbose_name="Профессия")
    age = models.IntegerField(verbose_name="Возраст")

    class Meta:
        verbose_name = "Моя информация"
        verbose_name_plural = "Моя информация"

