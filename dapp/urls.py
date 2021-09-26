from django.urls import path,include
from dapp import views
app_name='dapp'

urlpatterns = [
    path('',views.doc,name='doc'),
    path('doclist', views.doclist, name='doclist'),
    path('<str:c_slug>/',views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProCatDetail, name='ProCatDetail'),
    path('appoinment',views.demo, name='appoinment')
]
