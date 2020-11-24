from django.db import models

class Transport(models.Model):
    name = models.CharField(max_length=50, verbose_name='вид транспорта', default='')

    class Meta:
        verbose_name = 'Вид транспорта'
        verbose_name_plural = 'Виды транспорта'
    
    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='номер маршрута', default=0)
    
    class Meta:
        verbose_name = 'номер маршрута'
        verbose_name_plural = 'номера маршрутов'

    def __str__(self):
        return str(self.name)
    

class NumCar(models.Model):
    name = models.CharField(verbose_name='Номер машины', max_length=100)

    class Meta:
        verbose_name = 'номер машины'
        verbose_name_plural = 'номера машины'

    def __str__(self):
        return self.name
     

class Record(models.Model):
    date = models.DateField(verbose_name='дата заявки', auto_now_add=True, null=True)
    time = models.TimeField(verbose_name='время заявки', auto_now_add=True, null=True)
    from_who = models.CharField(verbose_name='от кого', max_length=250, default='')
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, verbose_name='вид транспорта')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='номер маршрута')
    description = models.TextField(verbose_name='заявка', default='')
    note = models.TextField(verbose_name='примечание', default='')
    brigade = models.CharField(max_length=50, verbose_name='бригада', default='')
    num_car = models.ForeignKey(NumCar, verbose_name='номер машины',on_delete=models.CASCADE)

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
    work = models.CharField(max_length=12, verbose_name='рабочий номер', default='')
    mobile = models.CharField(max_length=12, verbose_name='мобильный телефон', default='')

    class Meta:
        verbose_name = 'Номера телефонов'
        verbose_name_plural = 'Номеров телефонов'

    def __str__(self):
        return self.name
