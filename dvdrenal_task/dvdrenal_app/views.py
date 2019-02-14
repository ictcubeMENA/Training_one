from rest_framework import viewsets

from .serializers import *


class actor_name_vViewSet(viewsets.ModelViewSet):
    queryset = actor_name_v.objects.all()
    serializer_class = actor_name_vSerializer


class actors_vViewSet(viewsets.ModelViewSet):
    queryset = actors_v.objects.all()
    serializer_class = actors_vSerializer


class add_colom_vViewSet(viewsets.ModelViewSet):
    queryset = add_colom_v.objects.all()
    serializer_class = add_colom_vSerializer


class all_actors_film_vViewSet(viewsets.ModelViewSet):
    queryset = all_actors_film_v.objects.all()
    serializer_class = all_actors_film_vSerializer


class all_end_gen_vViewSet(viewsets.ModelViewSet):
    queryset = all_end_gen_v.objects.all()
    serializer_class = all_end_gen_vSerializer


class all_end_li_vViewSet(viewsets.ModelViewSet):
    queryset = all_end_li_v.objects.all()
    serializer_class = all_end_li_vSerializer


class count_last_least_vViewSet(viewsets.ModelViewSet):
    queryset = count_last_least_v.objects.all()
    serializer_class = count_last_least_vSerializer


class count_last_vViewSet(viewsets.ModelViewSet):
    queryset = count_last_v.objects.all()
    serializer_class = count_last_vSerializer


class country_id_vViewSet(viewsets.ModelViewSet):
    queryset = country_id_v.objects.all()
    serializer_class = country_id_vSerializer


class customer_pay_vViewSet(viewsets.ModelViewSet):
    queryset = customer_pay_v.objects.all()
    serializer_class = customer_pay_vSerializer


class email_vViewSet(viewsets.ModelViewSet):
    queryset = email_v.objects.all()
    serializer_class = email_vSerializer


class f_l_add_vViewSet(viewsets.ModelViewSet):
    queryset = f_l_add_v.objects.all()
    serializer_class = f_l_add_vSerializer


class film_number_vViewSet(viewsets.ModelViewSet):
    queryset = film_number_v.objects.all()
    serializer_class = film_number_vSerializer


class frequently_vViewSet(viewsets.ModelViewSet):
    queryset = frequently_v.objects.all()
    serializer_class = frequently_vSerializer


class joe_data_vViewSet(viewsets.ModelViewSet):
    queryset = joe_data_v.objects.all()
    serializer_class = joe_data_vSerializer


class music_kris_vViewSet(viewsets.ModelViewSet):
    queryset = music_kris_v.objects.all()
    serializer_class = music_kris_vSerializer


class store_business_vViewSet(viewsets.ModelViewSet):
    queryset = store_business_v.objects.all()
    serializer_class = store_business_vSerializer


class store_id_vViewSet(viewsets.ModelViewSet):
    queryset = store_id_v.objects.all()
    serializer_class = store_id_vSerializer


class top_five_vViewSet(viewsets.ModelViewSet):
    queryset = top_five_v.objects.all()
    serializer_class = top_five_vSerializer


class total_amount_rung_vViewSet(viewsets.ModelViewSet):
    queryset = total_amount_rung_v.objects.all()
    serializer_class = total_amount_rung_vSerializer
