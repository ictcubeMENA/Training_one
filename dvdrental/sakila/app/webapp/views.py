from rest_framework import viewsets
from webapp import models
from webapp import serializers


class countLastView(viewsets.ModelViewSet):
    queryset = models.countLast.objects.all()
    serializer_class = serializers.countLastSerializer


class actor_infoView(viewsets.ModelViewSet):
    queryset = models.actor_info.objects.all()
    serializer_class = serializers.actor_infoSerializer


class actor_nameView(viewsets.ModelViewSet):
    queryset = models.actor_name.objects.all()
    serializer_class = serializers.actor_nameSerializer


class countryView(viewsets.ModelViewSet):
    queryset = models.country2.objects.all()
    serializer_class = serializers.country2Serializer


class BuisnessIN_DollarsView(viewsets.ModelViewSet):
    queryset = models.dollars.objects.all()
    serializer_class = serializers.dollarsSerializer


class alone_tripView(viewsets.ModelViewSet):
    queryset = models.alone_trip.objects.all()
    serializer_class = serializers.alone_tripSerializer


class customer_listView(viewsets.ModelViewSet):
    queryset = models.customer_list.objects.all()
    serializer_class = serializers.customer_listSerializer


class email_canadaView(viewsets.ModelViewSet):
    queryset = models.email_canada.objects.all()
    serializer_class = serializers.email_canadaSerializer


class HOW_ManyActorIN_filmView(viewsets.ModelViewSet):
    queryset = models.film_actors.objects.all()
    serializer_class = serializers.film_actorsSerializer


class film_detailsView(viewsets.ModelViewSet):
    queryset = models.film_list.objects.all()
    serializer_class = serializers.film_listSerializer


class first_last_addressView(viewsets.ModelViewSet):
    queryset = models.first_last_address.objects.all()
    serializer_class = serializers.first_last_addressSerializer


class actor_FullNameView(viewsets.ModelViewSet):
    queryset = models.first_last_name.objects.all()
    serializer_class = serializers.first_last_nameSerializer


class nameWITHgenView(viewsets.ModelViewSet):
    queryset = models.gen_name.objects.all()
    serializer_class = serializers.gen_nameSerializer


class gross_revenueView(viewsets.ModelViewSet):
    queryset = models.gross_revenue.objects.all()
    serializer_class = serializers.gross_revenueSerializer


class groupLastNameView(viewsets.ModelViewSet):
    queryset = models.groupLastName.objects.all()
    serializer_class = serializers.groupLastNameSerializer


class storeDetailsView(viewsets.ModelViewSet):
    queryset = models.id_city_country.objects.all()
    serializer_class = serializers.id_city_countrySerializer


class LILastNameView(viewsets.ModelViewSet):
    queryset = models.LILastName.objects.all()
    serializer_class = serializers.LILastNameSerializer


class middle_nameView(viewsets.ModelViewSet):
    queryset = models.middle_name.objects.all()
    serializer_class = serializers.middle_nameSerializer


class most_frequentView(viewsets.ModelViewSet):
    queryset = models.most_frequent.objects.all()
    serializer_class = serializers.most_frequentSerializer


class name_joeView(viewsets.ModelViewSet):
    queryset = models.name_joe.objects.all()
    serializer_class = serializers.name_joeSerializer


class nicerbutslowerView(viewsets.ModelViewSet):
    queryset = models.nicerbutslower.objects.all()
    serializer_class = serializers.nicerbutslowerSerializer


class paymentCustomerView(viewsets.ModelViewSet):
    queryset = models.paymentCustomer.objects.all()
    serializer_class = serializers.paymentCustomerSerializer


class salesbyfilmCategoryView(viewsets.ModelViewSet):
    queryset = models.salesbyfilmCategory.objects.all()
    serializer_class = serializers.salesbyfilmCategorySerializer


class salesByStoreView(viewsets.ModelViewSet):
    queryset = models.salesByStore.objects.all()
    serializer_class = serializers.salesByStoreSerializer


class top5GrossView(viewsets.ModelViewSet):
    queryset = models.top5Gross.objects.all()
    serializer_class = serializers.top5GrossSerializer


class staffListView(viewsets.ModelViewSet):
    queryset = models.staffList.objects.all()
    serializer_class = serializers.staffListSerializer
