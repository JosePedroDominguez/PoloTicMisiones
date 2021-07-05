from django.db import models
# Create your models here.
class Tag(models.Model):
    nametag  = models.CharField(max_length=50)

    def __str__(self):
        return self.nametag


class Items(models.Model):
    name = models.CharField(max_length=50)
    imag = models.ImageField( upload_to="productos", null=True)
    tag  = models.ForeignKey(Tag, on_delete=models.PROTECT)
    description = models.TextField()
    price = models.FloatField()
    
    def __str__(self):
        return self.name


