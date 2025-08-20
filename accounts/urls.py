from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, MeView, AdminOnlyView, StaffOnlyView

urlpatterns = [
    # Auth
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/me/", MeView.as_view(), name="me"),
    # Roles demo
    path("admin-only/", AdminOnlyView.as_view(), name="admin_only"),
    path("staff-only/", StaffOnlyView.as_view(), name="staff_only"),
]
