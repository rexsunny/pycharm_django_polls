from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


from django.contrib import admin


info_dict = {
    'app_label': 'polls',
    'module_name': 'polls',
}

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^polls/$', 'polls.views.index'),
    (r'^polls/add/$', 'polls.views.add'),
    (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.details'),
    (r'^polls/(?P<poll_id>\d+)/delete/(?P<choice_id>\d+)$', 'polls.views.delete'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    (r'^polls/(?P<poll_id>\d+)/vote/(?P<choice_id>\d+)$', 'polls.views.vote'),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^accounts/profile', 'polls.views.profile'),

)