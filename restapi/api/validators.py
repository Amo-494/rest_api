# In the same module as the serializer or another module that is imported
from . import serializers


def validate_name_is_string(value):
    if not isinstance(value, str):
        raise serializers.ValidationError("Name must be a string.")
