from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer

# Create your views here.


# ***************** Function based view without id **************
@api_view(['GET','POST','PUT','DELETE'])
def CourseView(request):
    if request.method=='GET':
        obj=Course.objects.all()
        seri=CourseSerializer(obj,many=True)
        return Response(seri.data)
    elif request.method=='POST':
        seri=CourseSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)


# ************* Functions based view along with Id ***********************
@api_view(['GET','POST','PUT','DELETE','PATCH'])
def CourseViewWithId(request,pk):
    if request.method=='GET':
        obj=Course.objects.get(id=pk)
        seri=CourseSerializer(obj)
        return Response(seri.data)
    elif request.method=='POST':
        seri=CourseSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
    elif request.method=='PUT':
        obj=Course.objects.get(id=pk)
        seri=CourseSerializer(obj,data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
    elif request.method=='DELETE':
        obj=Course.objects.get(id=pk)
        obj.delete()

    elif request.method=='PATCH':
        obj=Course.objects.get(id=pk)
        seri=CourseSerializer(obj,data=request.data,partial=True)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)

# ******************** class based views without Id ***************

class ClassCourseView(APIView):
    def get_object(self,pk):
        try:
            return Course.objects.get(id=pk)
        except Course.DoesNotExit:
            return Http404

    def get(self,request,pk):
        obj=Course.objects.get(id=pk)
        seri=CourseSerializer(obj)
        return Response(seri.data)
    def post(self,request):
        seri=CourseSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
    def put(self,request,pk):
        obj=Course.objects.get(id=pk)
        seri=CourseSerializer(obj,data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
    def delete(self,request,pk):
        obj=Course.objects.get(id=pk)
        obj.delete()

    def patch(self,request,pk):
        obj=Course.objects.get(id=pk)
        seri=CourseSerializer(obj,data=request.data,partial=True)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)

# ***************** Mixin based view *******************
class CurdMixinView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request,pk):
        return self.list(request)

    def post(self,request,pk):
        return self.create(request)

    def put(self,request,pk):
        return self.update(request)

    def delete(self,request,pk):
        return self.destroy(request)


# ***************** Generic based Views **********************

class GenericBasedView(generics.ListAPIView,generics.CreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
