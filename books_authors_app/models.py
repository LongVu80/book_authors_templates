from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return (f"ID: {self.id} - Title: {self.title}")

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(default = '')
    books = models.ManyToManyField(Books, related_name = "authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return (f"ID: {self.id} - {self.first_name} {self.last_name}")
