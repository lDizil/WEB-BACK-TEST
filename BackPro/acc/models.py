from django.db import models


class Data(models.Model):
    # CharField - cтрока не больше 250 символов
    Login = models.CharField('Логин', max_length=20)
    Status = models.CharField('Статус', max_length=100)
    About = models.TextField('О себе')
    Date = models.DateTimeField('Дата регистрации')

    def __str__(self):
        return f'Данные пользователя: {self.Login}'
#выводит не нумерацию данных из бд, а корректную информацию

    def get_absolute_url(self):
        return f'/account/{self.id}'

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'