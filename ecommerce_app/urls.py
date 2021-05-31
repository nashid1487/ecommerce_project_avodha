from django.urls import path
from . import views
app_name='ecommerce_app'
urlpatterns= [
    path('', views.allProdCat, name='allProdCart'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.prodCatDet, name= 'prodCatDetail'),
]