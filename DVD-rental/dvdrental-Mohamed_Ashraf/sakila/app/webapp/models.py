from django.db import models


class countLast(models.Model):
    last_name = models.CharField(max_length=45)
    count = models.IntegerField()

    class Meta:
        db_table = 'countlast'


class actor_info(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'actor_info'


class actor_name(models.Model):
    actor_name = models.TextField()

    class Meta:
        db_table = 'actor_name'


class country2(models.Model):
    id= models.IntegerField(primary_key=True)
    country = models.CharField(max_length=45)

    class Meta:
        db_table = 'country2'


class dollars(models.Model):
    id = models.IntegerField(primary_key=True)
    dollars = models.DecimalField(max_digits=70, decimal_places=2)

    class Meta:
        db_table = 'dollars'


class alone_trip(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'alone_trip'


class customer_list(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    address = models.CharField(max_length=45)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    notes = models.TextField()
    sid = models.SmallIntegerField()

    class Meta:
        db_table = 'customer_list'


class email_canada(models.Model):
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    class Meta:
        db_table = 'email_canada'


class film_actors(models.Model):
    title = models.CharField(max_length=225)
    number_of_actors = models.IntegerField()

    class Meta:
        db_table = 'film_actors'


class film_list(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    category = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=70, decimal_places=2)
    length = models.IntegerField()
    actors = models.TextField()

    class Meta:
        db_table = 'film_list'


class first_last_address(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'first_last_address'


class first_last_name(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'first_last_name'


class gen_name(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'gen_name'


class gross_revenue(models.Model):
    name = models.CharField(max_length=45)
    gross_revenue = models.DecimalField(max_digits=70, decimal_places=2)

    class Meta:
        db_table = 'gross_revenue'


class groupLastName(models.Model):
    last_name = models.CharField(max_length=45)
    count = models.BigIntegerField()

    class Meta:
        db_table = 'grouplastname'


class id_city_country(models.Model):
    store_id = models.IntegerField
    city = models.CharField(max_length=45)
    country = models.CharField(max_length=50)

    class Meta:
        db_table = 'id_city_country'


class LILastName(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'li'


class middle_name(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'middle_na'


class most_frequent(models.Model):
    title = models.CharField(max_length=225)
    rented_movies = models.IntegerField()

    class Meta:
        db_table = 'most_frequent'


class Music(models.Model):
    title = models.CharField(max_length=225)

    class Meta:
        db_table = 'Music'


class name_joe(models.Model):
    actor_id = models.IntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'name_joe'


class nicerbutslower(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=225)
    describtion = models.TextField
    category = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=70, decimal_places=2)
    length = models.SmallIntegerField()
    actors = models.TextField()

    class Meta:
        db_table = 'nicer_but_slower_film_list'


class paymentCustomer(models.Model):
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    total = models.DecimalField(max_digits=70, decimal_places=2)

    class Meta:
        db_table = 'payment_customer'


class salesbyfilmCategory(models.Model):
    category = models.CharField(max_length=50)
    total_sales = models.DecimalField(max_digits=70, decimal_places=2)

    class Meta:
        db_table = 'sales_by_film_category'


class salesByStore(models.Model):
    store = models.TextField()
    manager = models.TextField()
    total_sales = models.DecimalField(max_digits=70, decimal_places=2)

    class Meta:
        db_table = 'sales_by_store'


class top5Gross(models.Model):
    name = models.CharField(max_length=25)
    gross_revenue = models.DecimalField(max_digits=70, decimal_places=2)

    class Meta:
        db_table = 'top5gross'


class staffList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    address = models.CharField(max_length=45)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    sid = models.IntegerField()

    class Meta:
        db_table = 'staff_list'
