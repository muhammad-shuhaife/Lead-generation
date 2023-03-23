from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.loginfront, name="loginfront"),
    path('logoutfront/', views.logoutfront, name="logoutfront"),
    path('loginfrontf/', views.loginfrontf, name="loginfrontf"),
    path('saveregistration/', views.saveregistration, name="saveregistration"),
    path('fhomepage/',views.fhomepage,name="fhomepage"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('id_card/', views.id_card, name="id_card"),
    path('id_details_save/', views.id_details_save, name="id_details_save"),
    path('idcard/<int:id>/', views.idcard, name="idcard"),


]