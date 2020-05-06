from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('friend', views.friend, name='friend'),
    path('createfriend', views.createfriend, name='createfriend'),
    path('deletefriend/<int:num>', views.deletefriend, name='deletefriend'),
    path('putfriend', views.putfriend, name='putfriend'),
    path('patient', views.patient, name='patient'),
    path('contact', views.contact, name='contact'),
    path('contact3', views.contact3, name='contact3'),
    path('confirm', views.confirm, name='confirm'),
    path('status', views.status, name='status'),
    path('createstatus', views.createstatus, name='createstatus'),
    path('deletepatient/<int:num>', views.deletepatient, name='deletepatient'),
    path('service', views.service, name='service'),
    path('createservice', views.createservice, name='createservice'),
    path('createservice2', views.createservice2, name='createservice2'),
    path('servicepost', views.servicepost, name='servicepost'),
    ]