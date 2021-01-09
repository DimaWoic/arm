from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import telebot


class Transport(models.Model):
    name = models.CharField(max_length=50, verbose_name='вид транспорта', default='', unique=True)

    class Meta:
        verbose_name = 'Вид транспорта'
        verbose_name_plural = 'Виды транспорта'
    
    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=2, verbose_name='номер маршрута', default='', unique=True)
    
    class Meta:
        verbose_name = 'номер маршрута'
        verbose_name_plural = 'номера маршрутов'

    def __str__(self):
        return str(self.name)
    

class NumCar(models.Model):
    name = models.CharField(verbose_name='Номер машины', max_length=10, unique=True)

    class Meta:
        verbose_name = 'номер машины'
        verbose_name_plural = 'номера машины'

    def __str__(self):
        return self.name
     

class Record(models.Model):
    date = models.DateField(verbose_name='дата заявки', auto_now_add=True, null=True)
    time = models.TimeField(verbose_name='время заявки', auto_now_add=True, null=True)
    from_who = models.CharField(verbose_name='от кого', max_length=250, default='', null=True)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, verbose_name='вид транспорта')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='номер маршрута')
    description = models.TextField(verbose_name='заявка', default='', null=True)
    note = models.TextField(verbose_name='примечание', default='', null=True)
    brigade = models.CharField(max_length=50, verbose_name='бригада', default='', null=True)
    num_car = models.ForeignKey(NumCar, verbose_name='номер машины', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'
    
    def __str__(self):
        return self.description


class Company(models.Model):
    name = models.CharField(verbose_name='Предприятие', max_length=100, default='')

    class Meta:
        verbose_name = 'предприятие'
        verbose_name_plural = 'предприятие'

    def __str__(self):
        return self.name


class CompanyUnit(models.Model):
    name = models.CharField(max_length=100, verbose_name='подразделение')
    company = models.ForeignKey(Company, verbose_name="предприятие", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'

    def __str__(self):
        return self.name


class PhoneNumbers(models.Model):
    unit = models.ForeignKey(CompanyUnit, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100, verbose_name='абонент', default='')
    position = models.CharField(max_length=100, verbose_name='должность', default='')
    work = models.CharField(max_length=12, verbose_name='рабочий номер', default='')
    mobile = models.CharField(max_length=12, verbose_name='мобильный телефон', default='')

    class Meta:
        verbose_name = 'Номера телефонов'
        verbose_name_plural = 'Номеров телефонов'

    def __str__(self):
        return self.name


bot = telebot.TeleBot(token='1263816311:AAHtoS8SYIDL6i1LBPH8Csmf7k985MbpcgA', parse_mode='HTML')


def send_massage(message):
    bot.send_message(chat_id='@sget_energo', text=message, disable_web_page_preview=True, parse_mode='HTML')


@receiver(post_save, sender=Record)
def sender_record(sender, **kwargs):
    if kwargs['created']:
        message = str(kwargs['instance'].route.name) + ' ' + \
                  kwargs['instance'].transport.name + ' ' + kwargs['instance'].description + ' ' + kwargs[
                      'instance'].brigade + ' ' + kwargs['instance'].num_car.name
        send_massage(message)

