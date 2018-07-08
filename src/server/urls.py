from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from django.urls import include
from fe_conta.views import MEAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('verify/', verify_jwt_token),
    path('me', MEAPIView.as_view(), name='me'),

    path('version', include('fe_version.urls')),

]
