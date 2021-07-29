from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import action


from bonds.models import Bond, User
from bonds.serializers import BondSerializer, BondSerializerGeneric, BondSerializerUSD, UserSerializer


class BondViewSet(viewsets.ModelViewSet):
    serializer_class = BondSerializer
    queryset = Bond.objects.all()
    throttle_classes = [UserRateThrottle]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], throttle_classes=[UserRateThrottle])
    def on_sale_mx(self, request):
        bonds = self.get_queryset().filter(status="o")
        serializer = BondSerializerGeneric(bonds, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], throttle_classes=[UserRateThrottle])
    def on_sale_usd(self, request):
        bonds = self.get_queryset().filter(status="o")
        serializer = BondSerializerUSD(bonds, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], throttle_classes=[UserRateThrottle])
    def sold(self, request):
        bonds = self.get_queryset().filter(status="p")
        serializer = BondSerializerGeneric(bonds, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    throttle_classes = [UserRateThrottle]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
