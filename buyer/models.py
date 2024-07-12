from django.db import models
from freelancer_platform import settings
from . import constraints

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class ADD_JOB(models.Model):
    comapany_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=constraints.JOB_TYPE)
    job_category =models.ManyToManyField(Category)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['salary']

    def __str__(self):
        return self.title
    

class Reveiw(models.Model):
    project = models.ForeignKey(ADD_JOB, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.CharField(max_length=10,choices=constraints.RATING)
    reveiw_text = models.TextField()

    def __str__(self):
        return self.freelancer.username
    