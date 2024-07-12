from django.db import models
from freelancer_platform import settings
from buyer.models import ADD_JOB
# Create your models here.
class Proposal(models.Model):
    job = models.ForeignKey(ADD_JOB, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proposal_post = models.TextField()
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.freelancer.username
