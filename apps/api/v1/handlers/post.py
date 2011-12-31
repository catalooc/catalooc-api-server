from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.post.forms import *

class PublicTimelineHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class HomeTimelineHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class UserTimelineHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    @validate(UserTimelineForm, 'GET')
    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class SuggestionsPostHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class DestroyPostHandler(BaseHandler):
    allowed_methods = ('DELETE',)
    
    @validate(DestroyPostForm, 'DELETE')
    def delete(self, request):
        return Response.http(rc.DELETED)

class CreatePostHandler(BaseHandler):
    allowed_methods = ('POST',)
    
    @validate(CreatePostForm, 'POST')
    def create(self, request):     
        return Response.http(rc.CREATED,"")

public_timeline_handler     = Resource(PublicTimelineHandler)
home_timeline_handler       = Resource(HomeTimelineHandler)
user_timeline_handler       = Resource(UserTimelineHandler)
suggestions_post_handler    = Resource(SuggestionsPostHandler)
destroy_post_handler        = Resource(DestroyPostHandler)
create_post_handler         = Resource(CreatePostHandler)