from rest_framework import serializers

from bonds.models import Bond, User, Purchase


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


class BondSerializer(RestApiSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bond
        exclude = ()


class UserSerializer(RestApiSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ()


class PurchaseSerializer(RestApiSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase
        exclude = ()
