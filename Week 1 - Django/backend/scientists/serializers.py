from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Scientists


class ScientistSerializer(ModelSerializer):
    class Meta:
        model = Scientists
        fields = ("name", "field")
