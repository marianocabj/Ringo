from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from webadmin import views


urlpatterns = [
    # Visits
    url(r'^$', views.index, name='index'),
    url(r'^visits/$', views.visit_list, name='visit_list'),
    url(r'^visit/(?P<visit_id>[0-9]+)/$', views.visit_detail, name='visit_detail'),

    # Visitors
    url(r'^visitors/$', views.visitor_list, name='visitor_list'),
    url(r'^visitors/(?P<visitor_id>[0-9]+)/$', views.visitor_details, name='visitor_details'),
    url(r'^visitors/(?P<pk>[0-9]+)/edit$', login_required(views.VisitorUpdate.as_view()), name='update_visitor'),
    url(r'^visitors/create/$', login_required(views.VisitorCreate.as_view()), name='create_visitor'),

    url(r'^contact/$', views.contact, name='contact')
]
