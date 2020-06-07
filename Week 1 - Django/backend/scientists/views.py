from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from .serializers import ScientistSerializer
from .models import Scientists


class ScientistView(APIView):
    def get(self, request):

        # Get all the scientists from our model
        data = Scientists.objects.all()

        # Turn Python into JSON
        serializer = ScientistSerializer(data=data, many=True)
        serializer.is_valid()

        # Return our data to the API
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        # Extract data attr from request obj
        data = request.data

        # Add the scientist to our db
        new_scientist = Scientists.objects.create(**data)

        new_scientist.save()

        serializer = ScientistSerializer(new_scientist)
        # serializer.is_valid()

        return Response(serializer.data)


# {
#     "name": "Richard Feynman",
#     "field": "Bongo Drums"
# }
