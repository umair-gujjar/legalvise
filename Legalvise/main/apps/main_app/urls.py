from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^surveyStart$', views.surveyStart, name='surveyStart'),
    url(r'^appointmentList$', views.appointmentList, name='appointmentList'),

    url(r'^appointments$', views.appointments, name='appointments'),
    url(r'^live_chat$', views.live_chat, name='live_chat'),
    url(r'^paymentOptions$', views.paymentOptions, name='paymentOptions'),
    url(r'^pricingPreview$', views.pricingPreview, name='pricingPreview'),
    url(r'^schedule$', views.schedule, name='schedule'),
]