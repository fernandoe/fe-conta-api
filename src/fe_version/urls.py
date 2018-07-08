from django.urls import path

from fe_version.views import VersionView

urlpatterns = [
    path('', VersionView.as_view(), ),
]
