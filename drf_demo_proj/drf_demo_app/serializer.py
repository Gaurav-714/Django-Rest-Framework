# New File Created...

from rest_framework import serializers
from .models import Todo, TodoTiming
import re # regex
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer): 

    slug = serializers.SerializerMethodField() # Get Foreign Key Data

    class Meta:
        model = Todo
        fields = ['user','uuid','title','slug','description']
        #exclude = ['is_done']
    
    def get_slug(self, obj):
        return slugify(obj.title)
        #return "Harry"

    def validate_title(self, data):
        if data:
            regex = re.compile('[@_!#$%^&*()<>?/|\}{~:]')
            if not regex.search(data) == None:
                raise serializers.ValidationError("Todo Title cannot contain special characters")
        return data
    
""" def validate(self, validated_data):
        print(validated_data)
        if validated_data.get('title'):
            title = validated_data['title']
            regex = re.compile('[@_!#$%^&*()<>?/|\}{~:]')
            if not regex.search(title) == None:
                raise serializers.ValidationError("Todo Title cannot contain special characters")
        return validated_data   """


class TodoTimingSerializer(serializers.ModelSerializer):
    
    todo = TodoSerializer()
    class Meta:
        model = TodoTiming
        exclude = ['created_at', 'updated_at']
        # depth = 1 # To get the data of a Foreign Key...