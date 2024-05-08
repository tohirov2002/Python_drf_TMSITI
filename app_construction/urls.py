from rest_framework.routers import DefaultRouter

from .views import (
    NewsView,
    AdsView,
    CategoryView,
    SpecialtyView,
    MastersView,
    LeadershipView,
    CnCategoryView,
    ComponentView,
    StandardListView
)

router = DefaultRouter()
router.register(r'news', NewsView)
router.register(r'ads', AdsView)
router.register(r'category', CategoryView)
router.register(r'specialty', SpecialtyView)
router.register(r'masters', MastersView)
router.register(r'leadership', LeadershipView)
router.register(r'cnCategory', CnCategoryView)
router.register(r'component', ComponentView)
router.register(r'standards', StandardListView)


urlpatterns = router.urls
