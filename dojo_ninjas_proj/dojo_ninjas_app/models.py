from django.db import models

# Create your models here.
class Dojo(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc = models.CharField(max_length=255, default="dojo antiguo")

	class Meta:
		managed = True
		db_table = "dojos"


class Ninja(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	dojo_id = models.ForeignKey(Dojo, related_name="dojos", on_delete=models.CASCADE)

	class Meta:
		managed = True
		db_table = "ninjas"