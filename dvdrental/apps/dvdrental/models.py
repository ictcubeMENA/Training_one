from django.db import models

# Create your models here.
class actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 255 )
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=45)
    last_update = models.DateField('Date', blank=True, null=True)

    class Meta:
        db_table = 'actor'
    def __str__(self):
        return self.first_name


class country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length =50)
    last_update = models.DateField('Date', blank=True, null=True)

    class Meta:
        db_table = 'country'

    def __str__(self):
        return self.country

class last_name(models.Model):
    last_name=models.CharField(max_length=45)
    count=models.IntegerField()
    class Mets:
        db_table='actor'

class city(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    city  = models.CharField(max_length =50 )
    country_id = models.ForeignKey(country, on_delete=models.CASCADE, db_column='country_id')
    last_update = models.DateField('Date', blank=True, null=True)

    class Meta:
        db_table = 'city'

# class address(models.Model):
#     address_id = models.IntegerField(primary_key=True)
#     address =  models.CharField(max_length =50 )
#     district = models.CharField(max_length =20 )
#     city_id  = models.ForeignKey(city, on_delete=models.CASCADE, db_column='city_id')
#
#     postal_code = models.CharField(max_length =10 )
#     phone = models.CharField(max_length =20 )
#     last_update = models.DateField('Date', blank=True, null=True)
#
#     class Meta:
#         db_table = 'address'


# class store (models.Model):
#     store_id = models.IntegerField(primary_key=True)
#     manager_staff_id = models.SmallIntegerField()
#     address_id = models.ForeignKey(address, on_delete=models.CASCADE, db_column='address_id')
#     last_update = models.DateField('Date', blank=True, null=True)
#     class Meta:
#         db_table = 'store'
#


# class customer(models.Model):
#     customer_id = models.IntegerField(primary_key=True)
#     store_id = models.ForeignKey(store, on_delete=models.CASCADE, db_column='store_id')
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length =50)
#     address_id= models.ForeignKey(address, on_delete=models.CASCADE, db_column='store_id')
#     activebool = models.BooleanField()
#     create_date = models.DateField()
#     last_update = models.DateField('Date', blank=True, null=True)
#     active = models.IntegerField()
#
#     class Meta:
#         db_table = 'customer'

# class language (models.Model):
#     language_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length =20)
#     last_update = models.DateField('Date', blank=True, null=True)
#
#     class Meta:
#         db_table = 'language'


class film(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length =255)
    description = models.TextField()
    release_year = models.DateTimeField()
    ##language_id = models.ForeignKey(language, on_delete=models.CASCADE, db_column='language_id')
    rental_duration = models.SmallIntegerField()
    rental_rate = models.IntegerField()
    length = models.SmallIntegerField()
    replacement_cost = models.IntegerField()
    last_update = models.DateField('Date', blank=True, null=True)
    special_features = models.TextField()

    class Meta:
        db_table = 'film'

    def __str__(self):
        return self.title


# class inventory (models.Model):
#     inventory_id = models.IntegerField(primary_key=True)
#     film_id = models.ForeignKey(film, on_delete=models.CASCADE, db_column='film_id')
#     store_id = models.ForeignKey(store, on_delete=models.CASCADE, db_column='store_id')
#     last_update = models.DateField('Date', blank=True, null=True)
#
#     class Meta:
#         db_table = 'inventory'


# class staff(models.Model):
#     staff_id = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     address_id = models.ForeignKey(address, on_delete=models.CASCADE, db_column='address_id')
#     email = models.CharField(max_length=50)
#     store_id =  models.ForeignKey(store, on_delete=models.CASCADE, db_column='store_id')
#     active = models.IntegerField()
#     username = models.CharField(max_length=16)
#     password = models.CharField(max_length=40)
#     last_update = models.DateField('Date', blank=True, null=True)
#
#     class Meta:
#         db_table = 'staff'
#
#
#

# class rental(models.Model):
#     rental_id = models.IntegerField(primary_key=True)
#     rental_date = models.DateField()
#     inventory_id = models.ForeignKey(inventory, on_delete=models.CASCADE, db_column='inventory_id')
#     customer_id =  models.ForeignKey(customer, on_delete=models.CASCADE, db_column='customer_id')
#     return_date = models.DateField()
#     staff_id = models.ForeignKey(staff, on_delete=models.CASCADE, db_column='staff_id')
#     last_update = models.DateField('Date', blank=True, null=True)
#
#     class Meta:
#         db_table = 'payment'


class film_actor(models.Model):
    actor=  models.ForeignKey(actor, on_delete=models.CASCADE, db_column='actor_id')
    film_id= models.ForeignKey(film, on_delete=models.CASCADE, db_column='film_id')
    last_update = models.DateField('Date', blank=True, null=True)
    # joined=  models.ManyToManyField(film)

    class Meta:
        db_table = 'film_actor'



# class film_category(models.Model):
#     film_category = models.IntegerField()######
#     film_id =  models.ForeignKey(film, on_delete=models.CASCADE, db_column='actor_id')
#    #### category_id = models.ForeignKey(category, on_delete=models.CASCADE, db_column='category_id') ###
#     last_update = models.DateField('Date', blank=True, null=True)
#
#     class Meta:
#         db_table = 'film_category'
#         unique_together = (('category', 'film'),)
#
#



# class payment(models.Model):
#     payment_id = models.IntegerField(primary_key=True)
#     customer_id = models.ForeignKey(customer, on_delete=models.CASCADE, db_column='film_id')
#     staff_id = models.ForeignKey(staff, on_delete=models.CASCADE, db_column='film_id')
#     rental_id = models.ForeignKey(rental, on_delete=models.CASCADE, db_column='film_id')
#     amount = models.IntegerField()
#     payment_date = models.DateField()
#
#     class Meta:
#         db_table = 'payment'














