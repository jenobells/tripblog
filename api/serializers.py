from rest_framework import serializers
from blogs.models import Blog
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    #user = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'description',
            'headerImage', 'location', 'image1', 'image2', 'image3', 'posted_by')
        read_only = ('id','user')

    #def get_author(self, obj):
        #return obj.user.username
