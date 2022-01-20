from django.db import models

# Create your models here.
class Stock(models.Model):
	item_name = models.CharField(max_length=50, blank=False, null=True)
	quantity = models.IntegerField(default='0', blank=False, null=True)
	export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.item_name + ' ' + str(self.quantity)