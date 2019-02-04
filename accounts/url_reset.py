from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url('^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url('^complete/$', password_reset_complete, name='password_reset_complete')
]

# this was in after 'password_rest_confirm, 'but was through error 'password_reset_confirm() got an unexpected keyword argument 'post_reset_confirm''
# when the passwrod reset link was clicked
#       {'post_reset_confirm': reverse_lazy('password_reset_complete')},