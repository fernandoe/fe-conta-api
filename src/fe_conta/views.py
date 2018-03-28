from rest_framework import views
from rest_framework.response import Response


class MEAPIView(views.APIView):
    def get(self, request, format=None):
        user = request.user
        data = {
            'email': str(user.email),
        }
        if user.entity:
            data['entity'] = str(user.entity.pk)
        return Response(data)
