from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets

from django.db.models.functions import Lower

from dvdrental.models import *
from dvdrental.serializer import *

from django.db.models import Q, Count


#1
class actorViewSet(viewsets.ModelViewSet):
    queryset = actor.objects.all()
    serializer_class = actorSerializer

#2
class actorViewSet2(viewsets.ModelViewSet):
   # queryset = actor.objects.filter(
   #     first_name__startswith='R'
   # ) | actor.objects.filter(
   #     last_name__startswith='D'
   # )



    queryset = actor.objects.filter(Q(first_name__startswith='R') | Q(last_name__startswith='D'))
    serializer_class = actorSerializer


#3  ##upper_case
class actorViewSet3(viewsets.ModelViewSet):
    queryset = actor.objects.order_by()
    serializer_class = actorSerializer

    def list(self, request, *args, **kwargs):
        q = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(q, many=True)
        res = []
        for item in serializer.data:
            res.append(str.upper(item.get("first_name") + " " + item.get("last_name")))
        return Response(res)


#4 ## starts with GEN
class actorViewSet4(viewsets.ModelViewSet):
    queryset = actor.objects.filter(last_name__icontains='GEN')
    serializer_class = actorSerializer


# try next time (upper case)
# class actorViewSet5(viewsets.ModelViewSet):
#     queryset=  actor.objects.all().order_by(Lower('last_name')).values_list('last_name', flat=True)
#     serializer_class = actorSerializer

#5
class actorViewSet5(viewsets.ModelViewSet):

    queryset = actor.objects.filter(last_name__icontains='LI').order_by('-first_name','-last_name')
    serializer_class = actorSerializer

#6 ## get country id and country

class countryViewSet(viewsets.ModelViewSet):
    queryset = country.objects.filter(country__in =['Afghanistan', 'Bangladesh', 'China'])
    serializer_class = countrySerializer


#7 ## add column
class actorViewSet6(viewsets.ModelViewSet):
    queryset = actor.objects.all()
    serializer_class = actorSerializer2

#8 ## count last name
class actorViewSet7(viewsets.ModelViewSet):
    queryset = actor.objects.values('last_name').annotate(count=Count('last_name'))
    serializer_class = countlastSerializer

#10 ## join
class film_actorViewSet(viewsets.ModelViewSet):
    queryset =film.objects.select_related('film').all()
    serializer_class = flimerSerializer
