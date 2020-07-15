from django.db import models

# Create your models here.
class Album(models.Model):
  title = models.CharField(max_length=255, null=True, blank=True)
  artist = models.CharField(max_length=255, null=True, blank=True)
  genre = models.CharField (max_length=255, null=True, blank=True)
  year_released = models.DateField(null=True, blank=True)

# class Comments(models.Model):
#     #User Feedback on the albums
#     comment = models.ForeignKey(Comments,blank=True, null=True, on_delete=models.CASCADE, related_name= "comment")
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         multiple_entries = 'entries'

#     def__str__(self):
#         return f"{self.text[50]}..."