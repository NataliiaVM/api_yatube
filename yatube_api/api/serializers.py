from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):

   class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )
        model = Group


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='slug',
        required=False,
        queryset=Group.objects.all(),
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        fields = (
            'id',
            'text',
            'pub_date',
            'author',
            'image',
            'group',
        )
        model = Post

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = (
        'id',
        'author',
        'post',
        'text',
        'created'
        )
        model = Comment
        read_only_fields = ('author', 'post')
