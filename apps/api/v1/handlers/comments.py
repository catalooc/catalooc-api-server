from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.comments.forms import *
from project.apps.comments.mongo import Comments
from project.apps.photos.mongo import Photos

class ListCommentsHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request, photo_id):
        return Comments.managers.filter({ 'photo_id' : photo_id })

class CreateCommentsHandler(BaseHandler):
    allowed_methods = ('POST',)

    @validate(CreateCommentsForm, 'POST')
    def create(self, request, photo_id):
        request.form.cleaned_data.update({
            'user'      : request.user.id,
            'photo_id'  : photo_id
        })
        return Comments.managers.save(request.form.cleaned_data)

class DestroyCommentsHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    @validate(DestroyCommentsForm, 'DELETE')
    def delete(self, request):
        return Response.http(rc.DELETED, Comments.managers.update(
            { '_id'         : request.form.cleaned_data['id'] },
            { 'is_deleted'  : True }
        ))

class LockCommentsHandler(BaseHandler):
    allowed_methods = ('PUT',)

    @validate(LockCommentsForm, 'PUT')
    def update(self, request, photo_id):
        return Photos.managers.update(
            { '_id' : photo_id },
            { 'is_comments_locked' : True }
        )

class UnlockCommentsHandler(BaseHandler):
    allowed_methods = ('PUT',)

    @validate(UnlockCommentsForm, 'PUT')
    def update(self, request, photo_id):
        return Photos.managers.update(
            { '_id' : photo_id },
            { 'is_comments_locked' : False }
        )

list_comments_handler       = Resource(ListCommentsHandler)
create_comments_handler     = Resource(CreateCommentsHandler)
destroy_comments_handler    = Resource(DestroyCommentsHandler)
lock_comments_handler       = Resource(LockCommentsHandler)
unlock_comments_handler     = Resource(UnlockCommentsHandler)