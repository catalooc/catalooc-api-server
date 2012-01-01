from django.contrib.auth.models import User
from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.search.forms import *

class FindSearchHandler(BaseHandler):
    allowed_methods = ('GET',)

    @validate(FindSearchForm, 'GET')
    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class UsersSearchHandler(BaseHandler):
    allowed_methods = ('GET',)

    @validate(UsersSearchForm, 'GET')
    def read(self, request):
        return User.objects.filter(
            username__startswith    = request.form.cleaned_data['query'],
            is_active               = True
        )

find_search_handler  = Resource(FindSearchHandler)
users_search_handler = Resource(UsersSearchHandler)