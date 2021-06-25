from django.urls import path,include
from website.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('crud_api',views.UserViewSet,basename='studentapi')

urlpatterns=[	
	path('',include(router.urls))
]