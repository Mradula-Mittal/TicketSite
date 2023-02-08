from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    image = models.ImageField(height_field=150, width_field=150)
    price = models.IntegerField()

#class Ticket(Site):
#    site = models.ForeignKey(Site, on_delete=models.CASCADE)
#    visit_date = models.DateField()
#    num_people = models.IntegerField()
#    fair = models.IntegerField()


