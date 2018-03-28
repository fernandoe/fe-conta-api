import factory
from django.contrib.auth import get_user_model
from fe_core.models import Entity

User = get_user_model()


class EntityFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Entidade Nome: {0}'.format(n))

    class Meta:
        model = Entity


class UserFactory(factory.django.DjangoModelFactory):
    entity = factory.SubFactory(EntityFactory)
    email = factory.Sequence(lambda n: u'{0}@test.com'.format(n))
    is_staff = False
    is_active = True

    class Meta:
        model = User

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user
