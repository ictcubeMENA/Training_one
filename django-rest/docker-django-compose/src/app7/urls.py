from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('actorFLN', views.restActorView)

# router.register('fullname', views.restView)
router.register('rest', views.restView)


urlpatterns = [

    path('first_name_LI/', views.first_name_LI_list.as_view()),
    path('COUNT_name/', views.COUNT_name_list.as_view()),
    path('Alone_name/', views.Alone_name_list.as_view()),
    path('actor_id/', views.actor_id_list.as_view()),
    path('title_l/', views.title_lan_list.as_view()),
    path('first_pay/', views.first_pay_list.as_view()),
    path('actor_count/', views.actor_count_list.as_view()),
    path('Canada_list/', views.Canada_list.as_view()),
    path('Number_of/', views.Number_of.as_view()),
    path('country_11/', views.countryll.as_view()),
    path('Store_City/', views.Store_City11.as_view()),
    path('s_first/', views.s_first_nameSerializert.as_view()),
    path('nameaddress/', views.actor_first_nameSerializert.as_view()),
    path('CONCATList/', views.actor_CONCATList.as_view()),

    path('Staff/', views.StaffView.as_view()),
    path('store/', views.cityView.as_view()),
    path('Alone/', views.AloneView.as_view()),
    path('film/', views.FilmViewSet.as_view()),
    path('Payment/', views.PaymentViewSet.as_view()),
    path('lastname/', views.MyModelViewSet.as_view()),
    path('middle/', views.Snippet1List.as_view()),
    path('Country/', views.Country1.as_view()),
    path('actorname/', views.SnippetList.as_view()),
    path('actorJoe/', views.actorJoe.as_view()),
    path('actorgen/', views.actorgen.as_view()),
    path('actorli/', views.actorli.as_view()),
    path('', include(router.urls))

]