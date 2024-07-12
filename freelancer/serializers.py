from rest_framework import serializers
from . import models

class ProposalSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Proposal
        fields = '__all__'