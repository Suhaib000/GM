from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import PostJobViewSet ,ApplyJobViewSet,UserViewSet
# ,LoginView
from . import views

router = DefaultRouter()
router.register(r'postjob', PostJobViewSet,basename="postjob")
router.register(r'applyjob', ApplyJobViewSet,basename="applyjob")
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', LoginView.as_view(), name='login'),
    # path('signup/', views.UserCreateAPIView.as_view(), name='user_signup'),
    # path('login/', views.UserLoginAPIView.as_view(), name='user_login'),
    # path('signup/', views.signup, name='signup'),
    # path('login/',  views.login_view, name='login'),
]



