from django.urls import path
from myapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),  # Default admin URL
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("about", views.about, name="about"),
    path("bookappointment", views.bookappointment, name="bookappointment"),
    path('viewstatus', views.viewstatus, name='viewstatus'),
        path('alltest/', views.alltest, name='alltest'),


]
