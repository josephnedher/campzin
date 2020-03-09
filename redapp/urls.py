from django.conf.urls import url
from redapp import views
app_name='redapp'
urlpatterns=[
 url(r'^register/$',views.register,name='register'),
 url(r'^images/$',views.image,name='imager'),
 url(r'^logins/$',views.user_login,name='user_login'),
]
