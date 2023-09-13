from rest_framework import serializers
from .models import Person
from .validators import validate_name_is_string

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_name_is_string])

    class Meta:
        model = Person
        fields = '__all__'

    def validate_name(self, value):
        # Check if the "name" field is a string
        if not isinstance(value, str):
            raise serializers.ValidationError("Name must be a string.")
        return value

    def validate_age(self, value):
        # Check if the "age" field is an integer
        if not isinstance(value, int):
            raise serializers.ValidationError("Age must be an integer.")
        return value

