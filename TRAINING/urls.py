from django.contrib import admin
from django.urls import path

from app1 import views
from app1.views import PersonCreateView
from app1.views import home



urlpatterns = [
    path('boringshutup/', admin.site.urls),

    path('',PersonCreateView.as_view()),

    path('home/',home,name="home"),
    path('delete/<int:id>', views.delete),

]
