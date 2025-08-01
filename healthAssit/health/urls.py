from django.urls import path
from .views import UserRegister,UserLogin,HealthRecordView,SkinDiseaseView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', UserRegister.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('bot/', HealthRecordView.as_view(), name='health-record'),
    path('skin/', SkinDiseaseView.as_view(), name='skin-disease'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
