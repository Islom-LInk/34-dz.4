from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
    name = models.CharField(max_length = 250,verbose_name = 'Название компании')
    about = models.TextField(verbose_name = 'Описание компании')
    logo = models.ImageField(verbose_name  = 'логотип компании')
    address = models.CharField(max_length = 250, verbose_name = 'адрес компании')
    email = models.EmailField(verbose_name = 'контактный email')
    phone = models.CharField(max_length=50,verbose_name="Телефон")
    working_hours  = models.CharField(max_length=100,verbose_name="Время работы")



    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компании"