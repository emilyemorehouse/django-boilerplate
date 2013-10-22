from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from django.views.generic import TemplateView
from django.conf.urls.defaults import *
from django_boilerplate.api import UserResource
from tastypie.api import Api
from registration.backends.default.views import RegistrationView
from users.forms import RegistrationForm
from django.conf.urls.static import static
from django.conf import settings

# Create admin page of your choosing
# import xadmin
# xadmin.autodiscover()
from django.contrib import admin
admin.autodiscover()

# Create V1 api endpoints
v1_api = Api(api_name='v1')
v1_api.register(UserResource())


from users.views import UserProfileDetailView, UserProfileEditView,\
                        CustomRegistrationView

urlpatterns = patterns('',

    # Allow admin page
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^xadmin/', include(xadmin.site.urls)),

    # API pages:
    url(r'^api/', include(v1_api.urls)),

    # User registration pages
    url(r"^login/$", "django.contrib.auth.views.login", name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login", name="logout"),
    url(r'accounts/register/$', RegistrationView.as_view(form_class = RegistrationForm), 
        name = 'registration_register'),
    url(r"^accounts/", include("registration.backends.default.urls")),
    # url(r"^accounts/", CustomRegistrationView.as_view(), name="registration_register"),
    url(r"^users/(?P<slug>\w+)/$", auth(UserProfileDetailView.as_view()), {'template_name': 'users/userdeets.html'},
            name="profile"),
    url(r"edit_profile/$", auth(UserProfileEditView.as_view()),
            {'template_name': 'registration/edit_profile'}, name="edit_profile"),

    # Basic pages
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),


)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
