from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.comments.forms import *

class ListCommentsHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request, photo_id):
        return Response.http(rc.ALL_OK, "")

class CreateCommentsHandler(BaseHandler):
    allowed_methods = ('POST',)

    @validate(CreateCommentsForm, 'POST')
    def create(self, request, photo_id):
        return Response.http(rc.CREATED,"")

class DestroyCommentsHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    @validate(DestroyCommentsForm, 'DELETE')
    def delete(self, request):
        return Response.http(rc.DELETED,"")

class LockCommentsHandler(BaseHandler):
    allowed_methods = ('PUT',)

    @validate(LockCommentsForm, 'PUT')
    def update(self, request, photo_id):
        return Response.http(rc.ALL_OK,"")

class UnlockCommentsHandler(BaseHandler):
    allowed_methods = ('PUT',)

    @validate(UnlockCommentsForm, 'PUT')
    def update(self, request, photo_id):
        return Response.http(rc.ALL_OK,"")

list_comments_handler       = Resource(ListCommentsHandler)
create_comments_handler     = Resource(CreateCommentsHandler)
destroy_comments_handler    = Resource(DestroyCommentsHandler)
lock_comments_handler       = Resource(LockCommentsHandler)
unlock_comments_handler     = Resource(UnlockCommentsHandler)