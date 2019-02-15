from django.db import models


# Create your models here.
class actor_name_v(models.Model):
    Actor_name = models.CharField(max_length=100)

    class Meta:
        db_table = "actor_name_v"

    def __str__(self):
        return str(self.Actor_name)


class actors_v(models.Model):
    actor_id = models.IntegerField
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = "actors_v"

    def __str__(self):
        return str(self.first_name)


class add_colom_v(models.Model):
    actor_id = models.IntegerField
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_update = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    class Meta:
        db_table = "add_colom_v"

    def __str__(self):
        return str(self.first_name)


class all_actors_film_v(models.Model):
    actor_id = models.IntegerField
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = "all_actors_film_v"

    def __str__(self):
        return str(self.first_name)


class all_end_gen_v(models.Model):
    actor_id = models.IntegerField
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = "all_end_gen_v"

    def __str__(self):
        return str(self.first_name)


class all_end_li_v(models.Model):
    actor_id = models.IntegerField
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = "all_end_li_v"

    def __str__(self):
        return str(self.first_name)


class count_last_least_v(models.Model):
    last_name = models.CharField(max_length=100)
    Count = models.IntegerField

    class Meta:
        db_table = "count_last_least_v"

    def __str__(self):
        return str(self.last_name)


class count_last_v(models.Model):
    Count = models.IntegerField
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = "count_last_v"

    def __str__(self):
        return str(self.last_name)


class country_id_v(models.Model):
    country_id = models.IntegerField
    country = models.CharField(max_length=100)

    class Meta:
        db_table = "country_id_v"

    def __str__(self):
        return str(self.country)


class customer_pay_v(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    TOTAL = models.DecimalField

    class Meta:
        db_table = "customer_pay_v"

    def __str__(self):
        return str(self.first_name)


class email_v(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = "email_v"

    def __str__(self):
        return str(self.first_name)


class f_l_add_v(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "f_l_add_v"

    def __str__(self):
        return str(self.first_name)


class film_number_v(models.Model):
    title = models.CharField(max_length=100)
    TOTAL = models.IntegerField

    class Meta:
        db_table = "film_number_v"

    def __str__(self):
        return str(self.title)


class frequently_v(models.Model):
    title = models.CharField(max_length=100)
    Count = models.IntegerField

    class Meta:
        db_table = "frequently_v"

    def __str__(self):
        return str(self.title)


class joe_data_v(models.Model):
    actor_id = models.IntegerField
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = "joe_data_v"

    def __str__(self):
        return str(self.first_name)


class music_kris_v(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = "music_kris_v"

    def __str__(self):
        return str(self.title)


class store_business_v(models.Model):
    store_id = models.IntegerField()
    dollars = models.FloatField()

    class Meta:
        db_table = "store_business_v"

    def __str__(self):
        return str(self.store_id)


class store_id_v(models.Model):
    store_id = models.IntegerField
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = "store_id_v"

    def __str__(self):
        return str(self.city)


class top_five_v(models.Model):
    Gross = models.FloatField
    Top_Five = models.CharField(max_length=100)

    class Meta:
        db_table = "top_five_v"

    def __str__(self):
        return str(self.Top_Five)


class total_amount_rung_v(models.Model):
    TOTAL = models.FloatField
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = "total_amount_rung_v"

    def __str__(self):
        return str(self.first_name)
