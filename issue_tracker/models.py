from django.db import models
from django.contrib.auth.models import User

class Bug(models.Model):
    """
    Model for issues
    """
    STATUS_CHOICES = (
        ('resolved', 'resolved'),
        ('unresolved', 'unresolved'),
    )

    title = models.CharField(max_length=250, null=True)
    body = models.TextField(null=True)
    author = models.ForeignKey(
        User,
        related_name='bug_author',
        null=True,
        on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        User,
        related_name='bug_assignee',
        null=True,
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    It will store comments of bug
    """
    title = models.CharField(max_length=250, null=True)
    body = models.TextField(null=True)
    bug = models.ForeignKey(
        Bug,
        related_name='comment_bug',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
