# Routers provide an easy way of automatically determining the URL conf.
from django.urls import path
from rest_framework import routers
from {{cookiecutter.module_name}}.app.views import MeProfileView

router = routers.DefaultRouter()

urlpatterns = [
    path('me', MeProfileView.as_view()),
]

urlpatterns += router.urls
