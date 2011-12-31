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
        return Response.http(rc.ALL_OK,"")

find_search_handler  = Resource(FindSearchHandler)
users_search_handler = Resource(UsersSearchHandler)