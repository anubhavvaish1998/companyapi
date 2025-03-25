from rest_framework import serializers # type: ignore
from api.models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields="__all__"