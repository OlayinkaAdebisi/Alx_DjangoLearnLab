from rest_framework import serializers
from .models import Book
from datetime import datetime, timezone

class BookSerializer(serializers.ModelSerializer):
    day_created = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'

    def get_day_created(self, obj):
        now = datetime.now(timezone.utc)
        difference = now - obj.date_created
        return difference.days