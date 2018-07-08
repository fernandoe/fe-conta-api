import os

from django.http import HttpResponse
from django.views import View


class VersionView(View):

    def get(self, request, *args, **kwargs):
        version = os.environ.get('VERSION', 'N/A')
        return HttpResponse(version)
