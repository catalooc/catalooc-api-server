from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.vote.forms import *

class CreateVoteHandler(BaseHandler):
    allowed_methods = ('POST',)

    @validate(CreateVoteForm, 'POST')
    def create(self, request, photo_id):
        return Response.http(rc.CREATED, "")

class DestroyVoteHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    @validate(DestroyVoteForm, 'DELETE')
    def delete(self, request, photo_id):
        return Response.http(rc.DELETED, "")

create_vote_handler     = Resource(CreateVoteHandler)
destroy_vote_handler    = Resource(DestroyVoteHandler)