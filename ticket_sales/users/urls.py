from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from users import views


urlpatterns = [
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/register/", views.UserRegistration.as_view(), name="register"),
]
