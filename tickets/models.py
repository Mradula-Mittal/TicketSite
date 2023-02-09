from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/image')
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Ticket(Site):
    site = models.ForeignKey(Site, related_name='tickets' , on_delete=models.CASCADE)
    visit_date = models.DateField()
    num_people = models.IntegerField()
    fair = models.IntegerField()

    def __str__(self):
        return self.site
