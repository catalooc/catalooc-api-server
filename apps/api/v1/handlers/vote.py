from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc
from project.libs.rest import Response

class CreateVoteHandler(BaseHandler):
    allowed_methods = ('POST',)

    def create(self, request):
        return Response.http(rc.CREATED, "")

class DestroyVoteHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    def delete(self, request):
        return Response.http(rc.DELETED, "")

create_vote_handler     = Resource(CreateVoteHandler)
destroy_vote_handler    = Resource(DestroyVoteHandler)