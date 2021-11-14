from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth.models import User

router = DefaultRouter()

router.register(r'tasks', views.TaskViewSet, basename='task')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns  = [
    path('', include(router.urls)),
    # path('auth/', ObtainAuthToken.as_view()),
    path('api-token-auth/', views.CustomAuthToken.as_view())
    # path('logout/', views.logout_view, name='logout')
]