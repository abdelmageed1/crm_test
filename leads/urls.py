from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('section1/', views.section1, name='section1'),
    path('section2/', views.section2, name='section2'),
    path('section3/', views.section3, name='section3'),
    path('section4/', views.section4, name='section4'),
    path('section5/', views.section5, name='section5'),
    path('add-lead/', views.add_lead, name='add_lead'),
    path('view-leads/', views.view_leads, name='view_leads'),
]
