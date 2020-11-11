from django.urls import path
from .views import LogsViewSet
from rest_framework.routers import DefaultRouter
app_name = "skud_app"
# app_name will help us do a reverse look-up latter.
# urlpatterns = [
    # path('logs/', LogsView.as_view({'get':'list'}) ),
	# path('logs/<int:pk>', LogsView.as_view({'get':'retrieve'})),
# ]

router = DefaultRouter()
router.register(r'logs', LogsViewSet, basename='user')
urlpatterns = router.urls