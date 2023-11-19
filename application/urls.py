from django.contrib import admin
from django.urls import path
from .views import home,co,signin,signout,Gfeedback,about,ccontact,register,python,devops,aws,salseforce,java,mean,mern,testing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',ccontact,name='contact'),
    path('co/',co,name='co'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('register/',register,name='register'),
    path('feedback/',Gfeedback,name='feedback'),
    path('python/',python,name='py'),
    path('java/',java,name='java'),
    path('aws/',aws,name='aws'),
    path('devops/',devops,name='dev'),
    path('testing/',testing,name='test'),
    path('mean/',mean,name='mean'),
    path('mern/',mern,name='mern'),
    path('sale/',salseforce,name='sale'),

]