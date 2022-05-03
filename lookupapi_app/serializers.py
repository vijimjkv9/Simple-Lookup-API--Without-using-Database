from rest_framework import serializers


class CommonSerializer(serializers.Serializer):
    """
    using simple serializer
    """
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
