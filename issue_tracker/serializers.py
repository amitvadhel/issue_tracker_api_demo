from rest_framework import serializers
from issue_tracker.models import Bug, Comment
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for comments
    """
    class Meta:
        model = Comment
        fields = ('title', 'body')


class BugSerializer(WritableNestedModelSerializer):
    """
    Serializer for bug along with comments
    """
    comment_bug = CommentSerializer(many=True)
    class Meta:
        model = Bug
        fields = ('title', 'body', 'status', 'comment_bug', 'assignee')
