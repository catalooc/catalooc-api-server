from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc
from project.libs.rest import Response
from django.contrib.auth.models import User

class SearchUsersHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class ShowUsersHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request):
        return Response.http(rc.ALL_OK,"")

search_users_handler    = Resource(SearchUsersHandler)
show_users_handler      = Resource(ShowUsersHandler)