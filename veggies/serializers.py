from rest_framework import serializers
from veggies.models import Veggies

class VeggieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veggies
        fields = [
            'id', 'title', 'author','description', 'created_at'
        ]