from .views import LogsViewSet, CardsViewSet, UsersViewSet, LevelsViewSet, ReadersViewSet, SBCsViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
app_name = "skud_app"

router = DefaultRouter()
router.register(r'logs', LogsViewSet)#basename='user'
router.register(r'cards', CardsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'levels', LevelsViewSet)
router.register(r'readers', ReadersViewSet)
router.register(r'sbcs', SBCsViewSet)

urlpatterns = [
    path('', include(router.urls))
    #path('forgot-password/', ForgotPasswordFormView.as_view()),
]

