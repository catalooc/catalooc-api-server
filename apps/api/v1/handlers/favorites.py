from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.favorites.forms import *
from project.apps.favorites.mongo import Favorites

class ListFavoritesHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        return Favorites.managers.filter({ 'user' : request.user.id })

class CreateFavoritesHandler(BaseHandler):
    allowed_methods = ('POST',)

    @validate(CreateFavoritesForm, 'POST')
    def create(self, request):
        request.form.cleaned_data.update({ 'user' : request.user.id })
        return Favorites.managers.save(request.form.cleaned_data)

class DestroyFavoritesHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    @validate(DestroyFavoritesForm, 'DELETE')
    def delete(self, request):
        return Response.http(rc.DELETED, Favorites.managers.update(
            { '_id'         : request.form.cleaned_data['id'] },
            { 'is_deleted'  : True }
        ))

list_favorites_handler      = Resource(ListFavoritesHandler)
create_favorites_handler    = Resource(CreateFavoritesHandler)
destroy_favorites_handler   = Resource(DestroyFavoritesHandler)