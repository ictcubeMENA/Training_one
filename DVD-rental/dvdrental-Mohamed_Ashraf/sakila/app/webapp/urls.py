from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('countLast', views.countLastView)
router.register('actor_info', views.actor_infoView)
router.register('actor_name', views.actor_nameView)

router.register('country', views.countryView)
router.register('BuisnessIN_Dollars', views.BuisnessIN_DollarsView)
router.register('alone_trip', views.alone_tripView)
router.register('customer_list', views.customer_listView)
router.register('email_canada', views.email_canadaView)
router.register('HOW_ManyActorIN_film', views.HOW_ManyActorIN_filmView)
router.register('film_details', views.film_detailsView)
router.register('first_last_address', views.first_last_addressView)
router.register('nameWITHgen', views.nameWITHgenView)
router.register('gross_revenue', views.gross_revenueView)
router.register('groupLastName', views.groupLastNameView)
router.register('storeDetails', views.storeDetailsView)
router.register('LILastName', views.LILastNameView)
router.register('middle_name', views.middle_nameView)
router.register('most_frequent', views.most_frequentView)
router.register('nicerbutslower', views.nicerbutslowerView)

router.register('paymentCustomer', views.paymentCustomerView)
router.register('salesbyfilmCategory', views.salesbyfilmCategoryView)
router.register('salesByStore', views.salesByStoreView)
router.register('top5Gross', views.top5GrossView)
router.register('staffList', views.staffListView)






urlpatterns = [
    path('', include(router.urls))
]
