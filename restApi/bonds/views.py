from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view


from bonds.models import Bond, User
from bonds.serializers import BondSerializer, BondSerializerGeneric, BondSerializerUSD, UserSerializer


class BondViewSet(viewsets.ModelViewSet):
    serializer_class = BondSerializer
    queryset = Bond.objects.all()

    @action(detail=False, methods=["get"])
    def on_sale_mx(self, request):
        bonds = self.get_queryset().filter(status="o")
        serializer = BondSerializerGeneric(bonds, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def on_sale_usd(self, request):
        bonds = self.get_queryset().filter(status="o")
        serializer = BondSerializerUSD(bonds, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def sold(self, request):
        bonds = self.get_queryset().filter(status="p")
        serializer = BondSerializerGeneric(bonds, many=True)
        return Response(serializer.data)


# @api_view(['GET'])
# def bond_api_view(request):
#     if request.method == 'GET':
#         bonds = Bond.objects.all()
#         print(bonds)
#         bond_serializer = BondSerializerUSD(bonds, many=True)
#         return Response(bond_serializer.data)

# class BondsApiView(APIView):
#     def get(self, request):
#         bonds = Bond.objects.all()
#         bond_serializer = BondSerializerUSD(bonds, many=True)
#         return Response(bond_serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
