from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CommonSerializer
from .lookup import departments


class DepartmentViewSet(viewsets.ViewSet):
    serializer_class = CommonSerializer()

    def list(self, request):
        """
        passing the departments attribute (import from lookup.py) to serializer
        """
        serializer = CommonSerializer(
            instance=departments.values(), many=True)
        return Response(serializer.data)
