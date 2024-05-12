from rest_framework.routers import DefaultRouter

from .views import CityPlansCategoryView, CitySubPlansView, CityMinPlansView

router = DefaultRouter()

router.register(r'cityPlansCategory', CityPlansCategoryView)
router.register(r'cityPlans', CitySubPlansView)
router.register(r'cityMinPlans', CityMinPlansView)

urlpatterns = router.urls
