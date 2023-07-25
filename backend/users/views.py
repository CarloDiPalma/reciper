from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import User
from .permissions import AdminAndSuperUser
from .serializers import UserCreateSerializer


class UserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # permission_classes = (AdminAndSuperUser,)
    # pagination_class = CustomPagination
    # filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'id'
    http_method_names = ['get', 'post']

    # def retrieve(self, request, *args, **kwargs):
    #     print('AAAAAAAAAAAAAAAAAAAAAAAA')
