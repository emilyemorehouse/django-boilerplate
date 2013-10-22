from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from users.models import UserProfile


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        excludes = ['password']
        #ordering = ['-created_on',]
        resource_name = 'users'
        include_resource_uri = False