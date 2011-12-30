from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc
from project.libs.rest import Response

class CreateCommentsHandler(BaseHandler):
    allowed_methods = ('POST',)

    def create(self, request):
        return Response.http(rc.CREATED,"")

class DestroyCommentsHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    def delete(self, request):
        return Response.http(rc.DELETED,"")

class LockCommentsHandler(BaseHandler):
    allowed_methods = ('PUT',)

    def update(self, request):
        return Response.http(rc.ALL_OK,"")

create_comments_handler     = Resource(CreateCommentsHandler)
destroy_comments_handler    = Resource(DestroyCommentsHandler)
lock_comments_handler       = Resource(LockCommentsHandler)