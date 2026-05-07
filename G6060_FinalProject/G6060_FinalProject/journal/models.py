from django.db import models
from django.contrib.auth.models import User


# Lab 5: Defining the database schema and relationships
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class JournalEntry(models.Model):
    # Lab 6: Linking to User for private owner-access
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title