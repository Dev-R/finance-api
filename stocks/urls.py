from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stocks import views



router = DefaultRouter()
router.register(r'stocks', views.StockViewSet, basename="stocks")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]