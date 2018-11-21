from django.conf.urls import url
from . import views

urlpatterns=[
    # url(r'^$',views.View.as_view()),
    url(r'^persona$',views.PersonaView.as_view()),
    url(r'^perro$',views.PerroView.as_view()),
]
