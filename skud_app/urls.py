from .views import LogsViewSet, CardsViewSet, UsersViewSet, LevelsViewSet, ReadersViewSet, SBCsViewSet
#from .views import    RegisterView, LoginView, LogoutView, UserView
#from .views import RegistrationAPIView, LoginAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
#from django.urls import re_path
from rest_framework_simplejwt.views import TokenVerifyView

app_name = "skud_app"

router = DefaultRouter()
router.register(r'logs', LogsViewSet)#basename='user'
router.register(r'cards', CardsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'levels', LevelsViewSet)
router.register(r'readers', ReadersViewSet)
router.register(r'sbcs', SBCsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('forgot-password/', ForgotPasswordFormView.as_view()),
    #path(r'register', RegisterView.as_view(), name='user-register'),
    #path(r'login', LoginView.as_view(), name='user-login'),
    #path(r'logout', LogoutView.as_view(), name='user-logout'),
    #path(r'current', UserView.as_view(), name='user-current'),   
#    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
#    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

