from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Signup),
    path('SignUp', views.Signup, name="Reg"),
    path('Login', views.loginpage, name="Loginpage"),
    path('Logout', views.logout, name="Logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
