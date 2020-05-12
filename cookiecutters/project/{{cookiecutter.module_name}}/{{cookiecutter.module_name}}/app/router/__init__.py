# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from {{cookiecutter.module_name}}.app.viewsets.user import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
