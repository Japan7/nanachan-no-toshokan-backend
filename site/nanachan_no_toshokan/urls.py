from django.conf import settings
from django.urls import include, path

# from demo.urls import router as demo_router
# from demo2.urls import router as demo2_router
from django.views.generic import RedirectView

from utils import routers

router = routers.DefaultRouter()
# router.extend(demo_router)
# router.extend(demo2_router)

urlpatterns = [
    path(settings.API_ROOT, include(router.urls)),
]

if settings.DEBUG:
    urlpatterns.extend([
        path('', RedirectView.as_view(pattern_name='api-root')),
    ])
