from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.photos.forms import *
from project.apps.photos.mongo import Photos

class PhotosPartOfHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, post_id):
        return Photos.managers.filter({ 'post_id' : post_id })

class ShowPhotosHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    @validate(ShowPhotosForm, 'GET')
    def read(self, request):
        return Photos.managers.get( { '_id' : request.cleaned_data['id'] } )

class CreatePhotosHandler(BaseHandler):
    allowed_methods = ('POST',)
    
    @validate(CreatePhotosForm, 'POST')
    def create(self, request, post_id):
        request.form.cleaned_data.update({ 'user' : request.user.id })
        return Photos.managers.save(request.form.cleaned_data)

class DestroyPhotosHandler(BaseHandler):
    allowed_methods = ('DELETE',)
    
    @validate(DestroyPhotosForm, 'DELETE')
    def create(self, request):
        return Response.http(rc.DELETED, Photos.managers.update(
            { '_id'         : request.form.cleaned_data['id'] },
            { 'is_deleted'  : True }
        ))

photos_part_of_handler  = Resource(PhotosPartOfHandler)
show_photos_handler     = Resource(ShowPhotosHandler)
create_photos_handler   = Resource(CreatePhotosHandler)
destroy_photos_handler  = Resource(DestroyPhotosHandler)