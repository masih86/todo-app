from rest_framework.routers import DefaultRouter
from . import views

app_name = "api-v1"

router = DefaultRouter()
router.register("tasks", views.TaskModelViewSet, basename="task")

urlpatterns = router.urls