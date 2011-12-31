from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.followers.forms import *

class FollowersIdsHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class CreateFollowersHandler(BaseHandler):
    allowed_methods = ('POST',)

    @validate(CreateFollowersForm, 'POST')
    def create(self, request):
        return Response.http(rc.CREATED,"")

class DestroyFollowersHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    @validate(DestroyFollowersForm, 'DELETE')
    def create(self, request):
        return Response.http(rc.DELETED,"")

followers_ids_handler       = Resource(FollowersIdsHandler)
create_followers_handler    = Resource(CreateFollowersHandler)
destroy_followers_handler   = Resource(DestroyFollowersHandler)