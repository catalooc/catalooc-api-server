from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.vote.forms import *
from project.apps.photos.mongo import Photos

class CreateVoteHandler(BaseHandler):
    allowed_methods = ('POST',)

    @validate(CreateVoteForm, 'POST')
    def create(self, request, photo_id):
        request.form.cleaned_data.update({
            'user'      : request.user.id,
            'photo_id'  : photo_id
        })
        return Photos.managers.save(request.form.cleaned_data)

class DestroyVoteHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    @validate(DestroyVoteForm, 'DELETE')
    def delete(self, request, photo_id):
        return Response.http(rc.DELETED, Photos.managers.update(
            {
                'user'      : request.user.id,
                'photo_id'  : photo_id
            },
            { 'is_deleted'  : True }
        ))

create_vote_handler     = Resource(CreateVoteHandler)
destroy_vote_handler    = Resource(DestroyVoteHandler)