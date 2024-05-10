from rest_framework.routers import DefaultRouter

from .views import DocumentTypesView, ElectronicFondView

router = DefaultRouter()
router.register(r'documentTypes', DocumentTypesView)
router.register(r'electronicFond', ElectronicFondView)


urlpatterns = router.urls
