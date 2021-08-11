from rest_framework import serializers
from blog.models import attr_blog, attr_flag, attr_tag

class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = attr_flag
        fields = ("name")

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = attr_tag
        fields = ("name")

class BlogSerializer(serializers.ModelSerializer):
    flag = serializers.CharField(source='flag.name')
    tag = serializers.CharField(source='tag.name')
    user = serializers.CharField(source='user.email')
    class Meta:
        model = attr_blog
        fields = (
            "id",
            "user",
            "creation_date",
            "title",
            "description",
            "tag",
            "flag"
        )