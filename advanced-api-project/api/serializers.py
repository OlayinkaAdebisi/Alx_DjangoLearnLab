from rest_framework import serializers
from .models import Author,Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_publication_year(self, data):
        year = date.today().year
        if data > year:
            raise serializers.ValidationError("Date must not be in the future")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        field = ['name','books']
#Basically i serialized both Book and Author model 
#i nested the BookSerlizer into the AuthorSerialier this allows for 
#the display of the contents of the books to be serialized along with that of author 