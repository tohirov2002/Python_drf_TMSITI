from rest_framework.routers import DefaultRouter

from .views import DictionaryView

router = DefaultRouter()

router.register(r'dictionary', DictionaryView)

urlpatterns = router.urls
