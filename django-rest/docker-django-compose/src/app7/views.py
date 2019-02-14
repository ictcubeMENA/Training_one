from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Avg, Max, Min, Sum,Count

from .models import *

from .serializers import *

from django.http import HttpResponse
from django.db import connection
from django.db.models import Value as V
from django.db.models.functions import Concat

from rest_framework.views import APIView

from django.db.models import Q
from django.db.models import Value



class restActorView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = actorFLNSerializer


class restView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = TrackSerializer





class actorJoe(APIView):

    def get(self, request, format=None):
        queryset = Actor.objects.filter(first_name='Joe')
        serializer = actorJoeSerializer(queryset, many=True)
        return Response(serializer.data)


class actorgen(APIView):

    def get(self, request, format=None):
        queryset = Actor.objects.filter( last_name__contains='gen')
        serializer = actorJoeSerializer(queryset, many=True)
        return Response(serializer.data)

class actorli(APIView):

    def get(self, request, format=None):
        queryset = Actor.objects.filter( last_name__contains='li').order_by('last_name','first_name' )
        serializer = actorJoeSerializer(queryset, many=True)
        return Response(serializer.data)

class Country1(APIView):

    def get(self, request, format=None):
        queryset = Country.objects.filter( country__in=('Afghanistan', 'Bangladesh', 'China'))
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)
class Snippet1List(APIView):

    def get(self, request, format=None):
        queryset = Actor.objects.all()
        serializer = middleSerializer(queryset, many=True)
        return Response({"user": serializer.data})

class last1List(APIView):

    def get(self, request, format=None):
        queryset = Actor.objects.all()
        ll=Actor.objects.all().count()
        serializer = last_nameSerializer(queryset, many=True)
        return Response({'Last Name Count':ll,"Last Name": serializer.data})

class MyModelViewSet(APIView):
    # The usual stuff here
    model = Actor

    def get(self, request, format=None):
        queryset = Actor.objects.values('first_name')
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

class PaymentViewSet(APIView):


    def get(self, request, format=None):
        queryset = Payment.objects.filter(payment_date__contains='2007-02')
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data)

class FilmViewSet(APIView):


    def get(self, request, format=None):
        queryset = Film.objects.filter(language__name='English').filter(title__startswith='K' or 'Q')
        serializer = FilmSerializer(queryset, many=True)
        return Response(serializer.data)


class AloneView(APIView):


    def get(self, request, format=None):
        queryset = Film.objects.filter(title='Alone Trip')
        serializer = TrackSerializer(queryset, many=True)
        return Response(serializer.data)

class cityView(APIView):


    def get(self, request, format=None):
        queryset = Store.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

class StaffView(APIView):


    def get(self, request, format=None):
        queryset = Staff.objects.all()
        serializer = StaffSerializer(queryset, many=True)
        return HttpResponse(queryset)

class SnippetList(APIView):

    def get(self, request, format=None):
        queryset = acror_test.objects.all()


        serializer = actorFLNSerializer(queryset, many=True)

        # return HttpResponse(queryset)
        return Response(serializer.data)

class actor_CONCATList(APIView):

    def get(self, request, format=None):
        queryset = actor_CONCAT.objects.all()
        serializer = actor1Serializer(queryset, many=True)
        return Response(serializer.data)

class actor_first_nameSerializert(APIView):

    def get(self, request, format=None):
        queryset = actor_first_name.objects.all()
        serializer = actor_first_nameSerializer(queryset, many=True)
        return Response(serializer.data)

class s_first_nameSerializert(APIView):

    def get(self, request, format=None):
        queryset = S_first_name.objects.all()
        serializer = s_first_nameSerializer(queryset, many=True)
        return Response(serializer.data)

class Store_City11(APIView):

    def get(self, request, format=None):
        queryset = Store_City.objects.all()
        serializer = Store_CitySerializer(queryset, many=True)
        return Response(serializer.data)


class countryll(APIView):

    def get(self, request, format=None):
        queryset = country_ll.objects.all()
        serializer = country_llSerializer(queryset, many=True)
        return Response(serializer.data)

class Number_of(APIView):

    def get(self, request, format=None):
        queryset = Number_of_times.objects.all()
        serializer = Number_of_timesSerializer(queryset, many=True)
        return Response(serializer.data)

class Canada_list(APIView):

    def get(self, request, format=None):
        queryset = Canada_n.objects.all()
        serializer = Canada_nSerializer(queryset, many=True)
        return Response(serializer.data)

class actor_count_list(APIView):

    def get(self, request, format=None):
        queryset = actor_count.objects.all()
        serializer = actor_countSerializer(queryset, many=True)
        return Response(serializer.data)

class first_pay_list(APIView):

    def get(self, request, format=None):
        queryset = first_pay.objects.all()
        serializer = first_paySerializer(queryset, many=True)
        return Response(serializer.data)

class title_lan_list(APIView):

    def get(self, request, format=None):
        queryset = title_lan.objects.all()
        serializer = title_lanSerializer(queryset, many=True)
        return Response(serializer.data)

class actor_id_list(APIView):

    def get(self, request, format=None):
        queryset = actor_id.objects.all()
        serializer = actor_idSerializer(queryset, many=True)
        return Response(serializer.data)

class Alone_name_list(APIView):

    def get(self, request, format=None):
        queryset = Alone_name.objects.all()
        serializer = Alone_nameSerializer(queryset, many=True)
        return Response(serializer.data)

class COUNT_name_list(APIView):

    def get(self, request, format=None):
        queryset = COUNT_name.objects.all()
        serializer = COUNT_nameSerializer(queryset, many=True)
        return Response(serializer.data)

class first_name_LI_list(APIView):

    def get(self, request, format=None):
        queryset = first_name_LI.objects.all()
        serializer = first_name_LISerializer(queryset, many=True)
        return Response(serializer.data)