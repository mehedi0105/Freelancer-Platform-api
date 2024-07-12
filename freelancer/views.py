from django.shortcuts import render
from . import serializers
from .models import Proposal
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.
User = get_user_model()

class Proposal_Veiw_set(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = serializers.ProposalSerializers

    # def accept(self, request, pk= None):
    #     proposal = self.get_object()
    #     if proposal.job.freelancer != request.user:
    #         return Response(status=status.HTTP_403_FORBIDDEN)
    #     proposal.is_accepted = True
    #     proposal.save()
    #     return Response(status=status.HTTP_200_OK,data={"data":"Proposal accepted and email sent."})

class ProposalSigleitemAPIView(APIView):
    def get_object(self, pk):
        try:
            return Proposal.objects.get(pk=pk)
        except Proposal.DoesNotExist:
            return Http404
    
    def put(self,request,pk,format=None):
        proposal = self.get_object(pk)
        serializer = serializers.ProposalSerializers(proposal, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
