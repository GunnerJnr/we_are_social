"""we_are_social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.flatpages import views
from django.views.static import serve
from paypal.standard.ipn import urls as paypal_urls

from accounts import views as accounts_views
from hello import views as hello_views
from magazines import views as magazine_views
from paypal_store import views as paypal_views
from products import views as product_views
from threads import views as forum_views

from settings.base import MEDIA_ROOT

urlpatterns = [  # pylint: disable-msg=C0103
    # admin backend url
    url(r'^admin/', admin.site.urls),
    # hello urls
    url(r'^$', hello_views.get_index, name='index'),
    # accounts urls
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^about/$', views.flatpage, {'url': '/pages/about/'}, name='about'),
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', accounts_views.subscriptions_webhook, name='subscriptions_webhook'),
    # paypal urls
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return/', paypal_views.paypal_return),
    url(r'^paypal-cancel/', paypal_views.paypal_cancel),
    # products urls
    url(r'^products/$', product_views.all_products),
    # magazines urls
    url(r'^magazines/$', magazine_views.all_magazines),
    # reusable_blog urls
    url(r'^blog/', include('reusable_blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # threads/forum views
    url(r'^forum/$', forum_views.forum),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),
]

# debug_toolbar urls
if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls))),
