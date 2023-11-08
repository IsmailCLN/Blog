from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews
from posts.views import register,HomeRedirectView,RegisterView
from django.views.generic import RedirectView
from rest_framework import routers
from posts.api.views import UserViewSet,PostViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('posts.urls')),
    path('profile/', include('accounts.urls')),
    path('login/', authViews.LoginView.as_view(),name="login"),
    path('password/change/', authViews.PasswordChangeView.as_view(template_name='registration/password-change.html'),name="password_change"),
    path('password/change/done', authViews.PasswordChangeDoneView.as_view(template_name='registration/password-change-done.html'),name="password_change_done"),
    path('register/', RegisterView.as_view() ,name="register"),
    path('go-to-home',HomeRedirectView.as_view(),name="go-home"),


    path('logout/',authViews.LogoutView.as_view(),name="logout"),
    path('api-auth/', include('rest_framework.urls'))


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)