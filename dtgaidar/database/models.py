from django.db import models


class Base(models.Model):
    number = models.CharField('Номер', max_length=20)
    old_number = models.CharField('Старый номер', max_length=20)
    title = models.CharField('Название', max_length=255)
    about = models.TextField('Описание')
    etc = models.CharField('Заметка', max_length=255)
    cab = models.CharField('Кабинет', max_length=50)
    date = models.DateField('Дата принятия')
    balanse = models.CharField('Баланс', max_length=100)
    balanse_now = models.CharField('Остаточная', max_length=100)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name='Инвентарная база'
        verbose_name_plural='Инвентарные базы'
