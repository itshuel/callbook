from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='Имя пользователя')
    surname = models.CharField(max_length=30, blank=False, verbose_name='Фамилия пользователя')
    date = models.DateField(blank=False, verbose_name='Дата рождения пользователя')
    status = models.CharField(max_length=15, blank=False, verbose_name='Статус пользователя')
    phonenumber = models.CharField(max_length=11, unique=True, null=False, blank=False, verbose_name='Номер телефона пользователя')
    info = models.TextField(max_length=100, blank=False, verbose_name='Информация о сотруднике')

    def __str__(self):
        return '{}: {} {}, {}, {}, {}'.format(self.status, self.surname, self.name, self.date, self.phonenumber, self.info)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'