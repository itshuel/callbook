from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия пользователя')
    date = models.DateField(verbose_name='Дата рождения пользователя')
    status = models.CharField(max_length=15, verbose_name='Статус пользователя')
    phonenumber = models.CharField(max_length=11, verbose_name='Номер телефона пользователя')
    info = models.TextField(max_length=100, verbose_name='Информация о сотруднике')

    def __str__(self):
        return '{}: {} {}, {}, {}, {}'.format(self.status, self.surname, self.name, self.date, self.phonenumber, self.info)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# for i in range(len(fi)):
#    ...:     Person.objects.create(name=''.format(fi[i].split()[0]), surname=''.format(fi[i].split()[1]), date='{}-{}-{}'.format(random.randint(1970, 2000), random.randint(1, 12), random.randint(1, 28
#    ...: )), status='Пользователь', phonenumber='{}'.format(random.randint(89000000000, 89009999999)), info='Обычный пользователь')