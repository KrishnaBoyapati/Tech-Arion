from django.db import models

# Create your models here.
class MainPage(models.Model):
    class Meta:
        db_table = 'main_page'
    page_id =  models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    thickness = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    product_image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.name)


