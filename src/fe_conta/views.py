from django.contrib.auth import get_user_model
from fe_core.models import Entity
from rest_framework import generics, status, permissions
from rest_framework import views
from rest_framework.response import Response

User = get_user_model()


class MEAPIView(views.APIView):
    def get(self, request, format=None):
        user = request.user
        data = {
            'email': str(user.email),
        }
        if user.entity:
            data['entity'] = str(user.entity.pk)
        return Response(data)


class RegisterCreateAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        entity = request.data.get("entity", None)

        if entity:
            try:
                entity = Entity.objects.get(uuid=entity)
            except Entity.DoesNotExist:
                data = {'message': 'A entidade informada não existe'}
                return Response(status=status.HTTP_400_BAD_REQUEST, data=data)

        if not email and not password:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            User.objects.get(email=email)
            data = {'message': 'Já existe um usuário registrado com esse e-mail'}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)
        except User.DoesNotExist:
            user = User.objects.create_user(email=email, password=password, entity=entity)
            user.save()
            data = {'email': user.email}
            return Response(status=status.HTTP_201_CREATED, data=data)
