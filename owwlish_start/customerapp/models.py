from django.db import models

class Customer(models.Model):
    """
    Class with the customers from csv file
    """
    def __str__(self):
        return str(self.first_name)

    def __repr__(self):
        return str(self.first_name)

    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=100, verbose_name='firstname')
    last_name = models.CharField(max_length=100, verbose_name='lastname')
    email = models.EmailField(verbose_name='email')
    gender = models.CharField(max_length=1, choices=GENDER)
    company = models.CharField(max_length=100, verbose_name='company')
    city = models.CharField(max_length=100, verbose_name='city')
    title = models.CharField(max_length=100, verbose_name='title')
    latitude = models.DecimalField(verbose_name='longitude', max_digits=9, decimal_places=6)
    longitude = models.DecimalField(verbose_name='latitude', max_digits=9, decimal_places=6)


    objects = models.Manager()

    class Meta:
        verbose_name = 'Customer'
        ordering = ['id']
        indexes = [
            models.Index(fields=['first_name'], name='idx_customer_first_name')
        ]

