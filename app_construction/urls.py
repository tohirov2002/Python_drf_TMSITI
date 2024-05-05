from rest_framework.routers import DefaultRouter

from .views import NewsView, AdsView

router = DefaultRouter()
router.register(r'news', NewsView)
router.register(r'ads', AdsView)


urlpatterns = router.urls
