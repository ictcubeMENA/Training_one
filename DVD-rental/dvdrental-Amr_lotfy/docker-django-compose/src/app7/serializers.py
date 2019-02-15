import time
from rest_framework import serializers

from .models import *
from django.db.models import Value as V
from django.db.models.functions import Concat

from django.db.models import Q
from django.db.models import Value

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmActor
        fields = ('actor',)

class TrackSerializer(serializers.ModelSerializer):
    tracks = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Film
        fields = ('film_id','title', 'description','release_year','tracks')


class fullnameSerializer(serializers.ModelSerializer):

    ActorName = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ('ActorName',)

    def get_ActorName(self, Actor):

        return f" {Actor.first_name.upper()} {Actor.last_name.upper()}"

class actorFLNSerializer(serializers.ModelSerializer):

    class Meta:
        model = acror_test
        fields = '__all__'

class actorJoeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('actor_id','first_name','last_name')

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('country_id','country')

class middleSerializer(serializers.ModelSerializer):

    middle_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ('first_name','middle_name','last_name')

    def get_middle_name(self, Actor):

        return

class last_nameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('last_name',)

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor

        fields = ('first_name',)

class PaymentSerializer(serializers.ModelSerializer):
    # total = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ('staff','amount')

    def get_total(self, Payment):


        return

        # depth=1

class FilmSerializer(serializers.ModelSerializer):


    class Meta:
        model = Film
        fields = ('film_id','title', 'description','release_year')

class CitySerializer(serializers.ModelSerializer):


    class Meta:
        model = Store
        fields = ('store_id','address', )
        depth=3

class StaffSerializer(serializers.ModelSerializer):


    class Meta:
        model = Staff
        fields = ('store_id','first_name','staff_id','address', )
        depth=3

class joinSerializer(serializers.ModelSerializer):


    class Meta:
        model = Staff
        fields = ('store_id','first_name','staff_id','address', )
        depth=3

class actor1Serializer(serializers.ModelSerializer):

    class Meta:
        model = actor_CONCAT
        fields = '__all__'


class actor_first_nameSerializer(serializers.ModelSerializer):

    class Meta:
        model = actor_first_name
        fields = '__all__'


class s_first_nameSerializer(serializers.ModelSerializer):

    class Meta:
        model = S_first_name
        fields = '__all__'



class Store_CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Store_City
        fields = '__all__'

class country_llSerializer(serializers.ModelSerializer):

    class Meta:
        model = country_ll
        fields = '__all__'
        # fields = ('country',)

class Number_of_timesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Number_of_times
        fields = '__all__'
        # fields = ('country',)

class Canada_nSerializer(serializers.ModelSerializer):

    class Meta:
        model = Canada_n
        fields = '__all__'

class actor_countSerializer(serializers.ModelSerializer):

    class Meta:
        model = actor_count
        fields = '__all__'

class first_paySerializer(serializers.ModelSerializer):

    class Meta:
        model = first_pay
        fields = '__all__'

class title_lanSerializer(serializers.ModelSerializer):

    class Meta:
        model = title_lan
        fields = '__all__'

class actor_idSerializer(serializers.ModelSerializer):

    class Meta:
        model = actor_id
        fields = '__all__'

class Alone_nameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alone_name
        fields = '__all__'

class COUNT_nameSerializer(serializers.ModelSerializer):

    class Meta:
        model = COUNT_name
        fields = '__all__'

class first_name_LISerializer(serializers.ModelSerializer):

    class Meta:
        model = first_name_LI
        fields = '__all__'