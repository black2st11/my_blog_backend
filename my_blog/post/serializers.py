from rest_framework import serializers
from .models import Post




class PostSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id','title', 'tag', 'file', 'created_at', 'updated_at')

    def get_tag(self, obj):
        tag_list = obj.tag_cabinet.all()   
        return [{"name" : tag_cabinet.tag.name} for tag_cabinet in tag_list]