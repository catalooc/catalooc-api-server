from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.apps.post.forms import *
from project.apps.post.mongo import Post

class PublicTimelineHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request):
        return Post.managers.all(request.GET)

class HomeTimelineHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request):
        return Post.managers.filter(
            request.GET,
            {}
        )

class UserTimelineHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    @validate(UserTimelineForm, 'GET')
    def read(self, request):
        return Post.managers.filter(
            request.GET,
            { 'user' : request.form.cleaned_data['id'] }
        )

class SuggestionsPostHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request):
        return Post.managers.filter(
            request.GET,
            { 'is_featured' : True }
        )

class DestroyPostHandler(BaseHandler):
    allowed_methods = ('DELETE',)
    
    @validate(DestroyPostForm, 'DELETE')
    def delete(self, request):
        return Response.http(rc.DELETED, Post.managers.update(
            { '_id'         : request.form.cleaned_data['id'] },
            { 'is_deleted'  : True }
        ))

class CreatePostHandler(BaseHandler):
    allowed_methods = ('POST',)
    
    @validate(CreatePostForm, 'POST')
    def create(self, request):
        return request.form.cleaned_data.update({ 'user' : request.user.id })

public_timeline_handler     = Resource(PublicTimelineHandler)
home_timeline_handler       = Resource(HomeTimelineHandler)
user_timeline_handler       = Resource(UserTimelineHandler)
suggestions_post_handler    = Resource(SuggestionsPostHandler)
destroy_post_handler        = Resource(DestroyPostHandler)
create_post_handler         = Resource(CreatePostHandler)