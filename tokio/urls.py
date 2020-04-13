from django.urls import path
from .  import views


urlpatterns = [
    path('', views.hello, name="hello-page"),
]

# urlpatterns = [
#     path('', views.hi, name= 'home-page'),
# ]