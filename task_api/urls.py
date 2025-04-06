from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from app.views import SignupAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('app.urls')),
    path('api/signup/', SignupAPIView.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
