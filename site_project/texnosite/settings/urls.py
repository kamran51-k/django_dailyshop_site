from django.urls import path
from .views import home_view, style_view
urlpatterns = [
    path('',home_view,name='home_page'),
    path('style/',style_view,name='style_page')
]