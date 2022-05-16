from rest_framework.routers import DefaultRouter
from logistic.views import ProductViewSet, StockViewSet, StockProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)


urlpatterns = router.urls
