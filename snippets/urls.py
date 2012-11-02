from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
    # code...

# For function views
"""urlpatterns = patterns('snippets.views',
        url(r'^snippets/$', 'snippet_list'),
        url(r'^snippets/(?P<pk>[0=9]+)/$', 'snippet_detail')
)"""

# For class-based views
urlpatterns = patterns('',
        url(r'^snippets/$', views.SnippetList.as_view()),
        url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
        url(r'^users/$', views.UserList.as_view()),
        url(r'^users/(?P<pk>[0-9]+)/$', views.UserInstance.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
        url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')))

