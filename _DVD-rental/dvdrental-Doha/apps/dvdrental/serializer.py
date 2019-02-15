from rest_framework import serializers


from dvdrental.models import *


class actorSerializer(serializers.ModelSerializer):
    class Meta:
        model = actor
        fields = ('first_name','last_name')
    def __str__(self):
        return self.first_name


class countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = ('country_id','country')
    def __str__(self):
        return self.country

# add middle column
class actorSerializer2(serializers.ModelSerializer):
    class Meta:
        model = actor
        fields = ('first_name','last_name','middle_name')
    def __str__(self):
        return self.first_name

class countlastSerializer(serializers.ModelSerializer):
    class Meta:
        model =last_name
        fields = ['last_name', 'count']
    def __str__(self):
        return self.first_name

class flimerSerializer(serializers.ModelSerializer):
    class Meta:
        model =film
        fields = ['film_id', 'title']






