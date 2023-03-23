from django.urls import path
from backend import views

urlpatterns = [
    path('', views.viewlogin, name="viewlogin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('indexpage/', views.indexpage, name="indexpage"),
    path('viewlead/', views.viewlead, name="viewlead"),
    path('deletelead/<int:dataid>/', views.deletelead, name="deletelead"),
    path('viewid/', views.viewid, name="viewid"),
    path('deleteid/<int:dataid>/', views.deleteid, name="deleteid"),
    path('messageview/', views.messageview, name="messageview"),
    path('deletemessage/<int:dataid>/', views.deletemessage, name="deletemessage"),

]