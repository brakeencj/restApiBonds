from decimal import Decimal
import requests
from rest_framework import serializers

from bonds.models import Bond, User

usd = ""


class RestApiSerializerMixin(object):
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(RestApiSerializerMixin, self).get_field_names(
            declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            fields = expanded_fields + self.Meta.extra_fields
        else:
            fields = expanded_fields
        if 'id' not in fields:
            fields += ['id']
        return fields


class UserSerializer(RestApiSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ()


class UserSerializerSmall(RestApiSerializerMixin,
                          serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ('created', 'updated')


class BondSerializer(RestApiSerializerMixin, serializers.HyperlinkedModelSerializer):
    """ Serializador de bonos mostrando la relación con la tabla de usuarios """
    seller = UserSerializerSmall(read_only=True)
    sellerId = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), source='seller',
        label='seller')
    buyer = UserSerializerSmall(read_only=True)
    buyerId = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), source='buyer',
        allow_null=True, label='buyer')

    class Meta:
        model = Bond
        exclude = ()


class BondSerializerGeneric(serializers.ModelSerializer):

    class Meta:
        model = Bond
        exclude = ('created', 'updated', 'seller', 'buyer', 'status')


class BondSerializerUSD(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('get_price_usd')

    def get_price_usd(self, obj):
        global usd
        if usd in ["", "1"]:
            body = requests.get(url="https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno?token=afed4ee4a50978cc4faa9688c63fb62ab43a2ede81e3c825793a7bb70f59126f",
                                headers={
                                    "Accept": "application/json",
                                    "Bmx-Token": "afed4ee4a50978cc4faa9688c63fb62ab43a2ede81e3c825793a7bb70f59126f"
                                })
            if (body.status_code == 200):
                json = body.json()
                usd = json['bmx']['series'][0]['datos'][0]['dato']
            else:
                usd = "1"
        return format(obj.price / Decimal(usd.replace(',', '.')), '.4f')

    class Meta:
        model = Bond
        exclude = ('created', 'updated', 'seller', 'buyer', 'status')
