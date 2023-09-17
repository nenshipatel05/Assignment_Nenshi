#urls.py 
from rest_framework.routers import DefaultRouter,SimpleRouter
from django.urls.conf import  path,include
from . import views

router = DefaultRouter()
# registering viewset with router
router.register("blog", views.BlogModelViewSet, basename="blog")
urlpatterns = [
    path('', include(router.urls))
]