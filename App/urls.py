from django.urls import path,include
from django.contrib import admin
from App import views
from django.http import HttpResponseRedirect

urlpatterns=[
		path('',views.index),
		path('index',views.index),
		path('about',views.about),
		path('admin',views.admin),
		path('adminhome',views.adminhome),
		path('appointment',views.appointment),
		path('accessoriess',views.accessoriess),
		path('dbappointment',views.dbappointment),
		path('appointmentend',views.appointmentend),
		path('viewbooking',views.viewbooking),
		path('ouroffers',views.ouroffers),
		path('postservices',views.postservices),
		path('barbers',views.barbers),
		path('contact',views.contact),
		path('services',views.services),
		path('logincheck',views.logincheck,name='logincheck'),
		path('postoffer',views.postoffer),
		path('postaccessories',views.postaccessories),
		path('storepostaccessories',views.storepostaccessories),
		path('vieworder',views.vieworder),
		path('feedforms',views.dblfeedget),
		path('customerfeed',views.customerfeed),
		path('adcustomerfeed',views.adcustomerfeed),
		path('storefeedback/<int:id>',views.storefeedback),
		path('adminfeedbackans/<int:id>',views.adminfeedbackans),


		


		




]