from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

class MyUserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        fields =['id', 'email', 'first_name', 'username', 'password']