from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.models import Profile

class ProfileDetail(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class = ProfileSerializer
    def get(self, request):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        serializer_context={'request': request}
        serializer = ProfileSerializer(profile , context=serializer_context)
        return Response(serializer.data)


class UserDetail(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class = UserSerializer
    def get(self, request):
        user = self.request.user
        serializer_context={'request': request}
        serializer = UserSerializer(user , context=serializer_context)
        return Response(serializer.data)



class AddressDetail(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class = AddressSerializer
    def get(self, request, id):
        user = self.request.user
        address = get_object_or_404(Address,user=user , id=id)
        serializer_context={'request': request}
        serializer = AddressSerializer(address ,  context=serializer_context)
        return Response(serializer.data)

