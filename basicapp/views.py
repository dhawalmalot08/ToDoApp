
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_out
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from . import models, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# Create your views here.



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })








class UserViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = serializers.UserSerializer(queryset, many=True)
        return Response(serializer.data)

    

    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)


    def create(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



        # user = get_object_or_404(queryset, pk=pk)
        # serializer = serializers.UserSerializer(user)


class TaskViewSet(viewsets.ViewSet):

    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


    def list(self, request):
        print(request.user)
        queryset = models.Task.objects.filter(user = request.user)
        serializer = serializers.TaskSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


    def create(self, request, *args, **kwargs):
        post_data = request.data
        post_data['user'] = request.user.id
        print(post_data)
        task_serializer = serializers.TaskSerializer( data=post_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response("Data added Successfully")
        return Response("data invalid")
            
        
        

    def retrieve(self,request, pk):
        id = pk
        if id is not None:
            task = models.Task.objects.get(pk=id)
            print(task)
            serializer = serializers.TaskSerializer(task)
            return Response(serializer.data)

        return HttpResponse("Unable to retrieve")

    def update(self, request, pk):
        id = pk
        task_data = models.Task.objects.get(pk=id)
        serializer = serializers.TaskSerializer(task_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data updated successfully")
        return Response("Unable to update")            


    def destroy(self, request, pk):
       id = pk
       task = models.Task.objects.get(pk=id)
       task.delete()
       return Response("Deleted Successfully")








        





