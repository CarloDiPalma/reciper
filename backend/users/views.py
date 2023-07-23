from django.shortcuts import render
from rest_framework import viewsets

from .models import User


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (AdminAndSuperUser,)
#     pagination_class = CustomPagination
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('username',)
#     lookup_field = 'username'
#     http_method_names = ['get', 'post', 'patch', 'delete']
#
#     def create(self, request, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.data.get('email')
#             if User.objects.filter(email=email).exists():
#                 return Response(serializer.errors,
#                                 status=status.HTTP_400_BAD_REQUEST)
#             user, created = User.objects.get_or_create(**serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
