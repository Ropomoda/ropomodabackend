from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAcceptable
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



class AddressAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def get(self, request):
        user = self.request.user
        addresses = self.get_queryset().filter(user=user)
        serializer_context={'request': request}
        serializer = AddressSerializer(addresses ,many=True,  context=serializer_context)
        return Response(serializer.data)
    
    def post(self, request):
        user = self.request.user
        try:
            #TODO refactor create method
            address = Address(
                name=request.data["name"],
                description=request.data["description"],
                longitude=request.data["longitude"],
                latitude=request.data["latitude"],
                state=request.data["state"],
                city=request.data["city"],
                post_address=request.data["post_address"],
                plaque=request.data["plaque"],
                floor=request.data["floor"],
                post_code=request.data["post_code"],
            )
        except Exception as e:
            raise NotAcceptable(str(e))
        address.user = user
        address.save()
        serializer_context={'request': request}
        serializer = AddressSerializer(address,  context=serializer_context)
        return Response(serializer.data)

class AddressView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = AddressSerializer
    def get(self, request, id):
        user = self.request.user
        address = get_object_or_404(Address,user=user , id=id)
        serializer_context={'request': request}
        serializer = AddressSerializer(address ,  context=serializer_context)
        return Response(serializer.data)

