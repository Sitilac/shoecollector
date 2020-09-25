from django.db import models
from django.urls import reverse
from datetime import date
CLEANED = (
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('E', 'Evening')
)
class Outfit(models.Model):
  name = models.CharField(max_length=50)
  top = models.CharField(max_length=50)
  bottom = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('outfits_detail', kwargs={'pk': self.id})

class Shoe(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  price = models.IntegerField()
  
  outfits = models.ManyToManyField(Outfit)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'shoe_id': self.id})
  


class Cleaning(models.Model):
  date = models.DateField()
  shoe_clean = models.CharField(
    max_length=1,
    choices=CLEANED,
    default=CLEANED[0][0]
  )
  def __str__(self):
  # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_shoe_clean_display()} on {self.date}"
  
  shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
