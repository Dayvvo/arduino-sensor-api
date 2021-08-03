from Rest_API.viewsets import APIViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('get-parameters',APIViewset)

