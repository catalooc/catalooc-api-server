from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.followers.forms import *
from project.apps.followers.mongo import Followers

class FollowersIdsHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        return Followers.managers.filter({ 'user' : request.user.id })

class CreateFollowersHandler(BaseHandler):
    allowed_methods = ('POST',)

    @validate(CreateFollowersForm, 'POST')
    def create(self, request):
        request.form.cleaned_data({ 'user' : request.user.id })
        return Followers.managers.save(request.form.cleaned_data)

class DestroyFollowersHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    @validate(DestroyFollowersForm, 'DELETE')
    def create(self, request):
        return Response.http(rc.DELETED, Followers.managers.update(
            {
                'user'      : request.user.id,
                'id'        : form.request.cleaned_data['id']
            },
            { 'is_deleted'  : True }
        ))

followers_ids_handler       = Resource(FollowersIdsHandler)
create_followers_handler    = Resource(CreateFollowersHandler)
destroy_followers_handler   = Resource(DestroyFollowersHandler)