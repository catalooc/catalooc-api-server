from django.conf.urls.defaults import patterns, include, url
from project.apps.api.v1.handlers.account import *
from project.apps.api.v1.handlers.comments import *
from project.apps.api.v1.handlers.favorites import *
from project.apps.api.v1.handlers.followers import *
from project.apps.api.v1.handlers.photos import *
from project.apps.api.v1.handlers.post import *
from project.apps.api.v1.handlers.search import *
from project.apps.api.v1.handlers.users import *
from project.apps.api.v1.handlers.vote import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^account/verify_credentials.(?P<emitter_format>.+)$', verify_credentials_account_handler),
    url(r'^account/end_session.(?P<emitter_format>.+)$', end_session_account_handler),
    url(r'^account/update_profile.(?P<emitter_format>.+)$', update_profile_account_handler),
    url(r'^account/update_profile_image.(?P<emitter_format>.+)$', update_profile_image_account_handler),
    url(r'^account/totals.(?P<emitter_format>.+)$', totals_account_handler),
    url(r'^account/settings.(?P<emitter_format>.+)$', settings_account_handler),
    
    url(r'^comments/(?P<photo_id>\w+)/list.(?P<emitter_format>.+)$', list_comments_handler),
    url(r'^comments/(?P<photo_id>\w+)/create.(?P<emitter_format>.+)$', create_comments_handler),
    url(r'^comments/(?P<photo_id>\w+)/lock.(?P<emitter_format>.+)$', lock_comments_handler),
    url(r'^comments/(?P<photo_id>\w+)/unlock.(?P<emitter_format>.+)$', unlock_comments_handler),
    url(r'^comments/destroy.(?P<emitter_format>.+)$', destroy_comments_handler),
    
    url(r'^favorites/list.(?P<emitter_format>.+)$', list_favorites_handler),
    url(r'^favorites/create.(?P<emitter_format>.+)$', create_favorites_handler),
    url(r'^favorites/destroy.(?P<emitter_format>.+)$', destroy_favorites_handler),
    
    url(r'^followers/ids.(?P<emitter_format>.+)$', followers_ids_handler),
    url(r'^followers/create.(?P<emitter_format>.+)$', create_followers_handler),
    url(r'^followers/destroy.(?P<emitter_format>.+)$', destroy_followers_handler),
    
    url(r'^photos/part_of/(?P<post_id>\w+).(?P<emitter_format>.+)$', photos_part_of_handler),
    url(r'^photos/(?P<post_id>\w+)/create.(?P<emitter_format>.+)$', create_photos_handler),
    url(r'^photos/mark_feature.(?P<emitter_format>.+)$', show_photos_handler),
    url(r'^photos/show.(?P<emitter_format>.+)$', show_photos_handler),
    url(r'^photos/destroy.(?P<emitter_format>.+)$', destroy_photos_handler),
    
    url(r'^post/public_timeline.(?P<emitter_format>.+)$', public_timeline_handler),
    url(r'^post/home_timeline.(?P<emitter_format>.+)$', home_timeline_handler),
    url(r'^post/user_timeline.(?P<emitter_format>.+)$', user_timeline_handler),
    url(r'^post/suggestions_post.(?P<emitter_format>.+)$', suggestions_post_handler),
    url(r'^post/destroy.(?P<emitter_format>.+)$', destroy_post_handler),
    url(r'^post/create.(?P<emitter_format>.+)$', create_post_handler),
    
    url(r'^search/find.(?P<emitter_format>.+)$', find_search_handler),
    url(r'^search/users.(?P<emitter_format>.+)$', users_search_handler),
    
    url(r'^users/show.(?P<emitter_format>.+)$', show_users_handler),
    
    url(r'^vote/(?P<photo_id>\w+)/create.(?P<emitter_format>.+)$', create_vote_handler),
    url(r'^vote/(?P<photo_id>\w+)/destroy.(?P<emitter_format>.+)$', destroy_vote_handler),
)
