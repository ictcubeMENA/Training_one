from rest_framework import serializers

from .models import *


class actor_name_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = actor_name_v
        fields = '__all__'


class actors_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = actors_v
        fields = '__all__'


class add_colom_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = add_colom_v
        fields = '__all__'


class all_actors_film_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_actors_film_v
        fields = '__all__'


class all_end_gen_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_end_gen_v
        fields = '__all__'


class all_end_li_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_end_li_v
        fields = '__all__'


class count_last_least_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = count_last_least_v
        fields = '__all__'


class count_last_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = count_last_v
        fields = '__all__'


class country_id_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = country_id_v
        fields = '__all__'


class customer_pay_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer_pay_v
        fields = '__all__'


class email_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = email_v
        fields = '__all__'


class f_l_add_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = f_l_add_v
        fields = '__all__'


class film_number_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = film_number_v
        fields = '__all__'


class frequently_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = frequently_v
        fields = '__all__'


class joe_data_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = joe_data_v
        fields = '__all__'


class music_kris_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = music_kris_v
        fields = '__all__'


class store_business_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = store_business_v
        fields = '__all__'


class store_id_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = store_id_v
        fields = '__all__'


class top_five_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = top_five_v
        fields = '__all__'


class total_amount_rung_vSerializer(serializers.ModelSerializer):
    class Meta:
        model = total_amount_rung_v
        fields = '__all__'
