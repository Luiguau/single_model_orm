from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	notas = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		managed = True
		db_table = 'authors'


class Book(models.Model):
	title = models.CharField(max_length=255)
	desc = models.TextField()
	author = models.ManyToManyField(Author, related_name="authors", blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		managed = True
		db_table = 'books'