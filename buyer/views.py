from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from freelancer.serializers import ProposalSerializers
from freelancer.models import Proposal
# Create your views here.

class All_JOB_LIST_API_VIEW(APIView):

    def get(self, request, format=None):
        jobs = models.ADD_JOB.objects.all()
        serializer = serializers.JobSerializers(jobs, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.JobSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def proposals(self, request, pk=None):
        jobs = self.get_object()
        if jobs.freelancer != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        proposals = Proposal.objects.filter(jobs=jobs)
        serializer = ProposalSerializers(proposals, many=True)
        return Response(serializer.data)


class JOB_DETAILS_API_VIEW(APIView):

    def get_objects(self, pk):
        try:
            return models.ADD_JOB.objects.get(pk = pk)
        except models.ADD_JOB.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        job = self.get_objects(pk=pk)
        serializer = serializers.JobSerializers(job)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
         job = self.get_objects(pk=pk)
         serializer = serializers.JobSerializers(job, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ReveiwListAPIView(APIView):
    def get_object(self, pk):
        try:
            return models.Reveiw.objects.get(pk=pk)
        except models.Reveiw.DoesNotExist:
            return Http404
    
    def get(self, request,pk, format= None):
        reviwe = self.get_object(pk)
        serializer = serializers.ReviewSerializers(reviwe)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        reviwe = self.get_object(pk)
        serializer = serializers.ReviewSerializers(reviwe, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
         reviwe = self.get_object(pk)
         reviwe.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    
class AllReveiwListAPIView(APIView):

    def post(self, request, format = None):
        serializer = serializers.ReviewSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request ,format = None):
        jobs = models.Reveiw.objects.all()
        serializer = serializers.ReviewSerializers(jobs, many= True)
        return Response(serializer.data)
    

    
class AllCategoryListAPIView(APIView):
    def get(self, request ,format = None):
        category = models.Category.objects.all()
        serializer = serializers.CategorySerializers(category, many= True)
        return Response(serializer.data)

# class CategorySlugListAPIView(APIView):

#     def get_object(self, category_slug):
#         try:
#             return models.Category.objects.get(category_slug=category_slug)
#         except models.Category.DoesNotExist:
#             return Http404
        
#     def get(self, request, category_slug = None, format=None):
#         category = self.get_object(category_slug)
#         job = models.ADD_JOB.objects.all()
#         categories = serializers.CategorySerializers(category, many= True)
#         Jobs = serializers.CategorySerializers(job, many= True)

#         return Response({
#             'jobs':Jobs.data,
#             'categories':categories.data,
#         })
    
class CategorySlugListAPIView(APIView):

    def get_object(self, slug):
        try:
            return models.Category.objects.get(slug=slug)
        except models.Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug=None, format=None):
        category = self.get_object(category_slug)
        jobs = models.ADD_JOB.objects.filter(job_category=category)
        job_serializer = serializers.JobSerializers(jobs, many=True)

        return Response(job_serializer.data)
