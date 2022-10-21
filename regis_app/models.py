from django.db import models

# Create your models here.
class employee(models.Model):
    emp_name=models.CharField(max_length=10)
    emp_Id=models.IntegerField()
    emp_img=models.ImageField(
        upload_to='images/'
    )
    emp_file=models.FileField(
        upload_to='file/'
    )
    def __str__(self):
        return self.emp_name