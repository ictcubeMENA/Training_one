from rest_framework import serializers

from webapp import models


class countLastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.countLast
        fields = '__all__'


class actor_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.actor_info
        fields = '__all__'


class actor_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.actor_name
        fields = '__all__'


class country2Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.country2
        fields = '__all__'


class dollarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.dollars
        fields = '__all__'


class alone_tripSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.alone_trip
        fields = '__all__'


class customer_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customer_list
        fields = '__all__'


class email_canadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.email_canada
        fields = '__all__'


class film_actorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.film_actors
        fields = '__all__'


class film_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.film_list
        fields = '__all__'


class first_last_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.first_last_address
        fields = '__all__'


class first_last_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.first_last_name
        fields = '__all__'


class gen_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.gen_name
        fields = '__all__'


class gross_revenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.gross_revenue
        fields = '__all__'


class groupLastNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.groupLastName
        fields = '__all__'


class id_city_countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.id_city_country
        fields = '__all__'


class LILastNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LILastName
        fields = '__all__'


class middle_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.middle_name
        fields = '__all__'


class most_frequentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.most_frequent
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = '__all__'


class name_joeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.name_joe
        fields = '__all__'


class nicerbutslowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.nicerbutslower
        fields = '__all__'


class paymentCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.paymentCustomer
        fields = '__all__'


class salesbyfilmCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.salesbyfilmCategory
        fields = '__all__'


class salesByStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.salesByStore
        fields = '__all__'


class top5GrossSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.top5Gross
        fields = '__all__'


class staffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.staffList
        fields = '__all__'
