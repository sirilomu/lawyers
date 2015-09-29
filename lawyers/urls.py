from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	#Examples:
    #url(r'^$', coreviews.SplashView.as_view()),
    #url(r'^$/', coreviews.LandingView.as_view())

    url(r'^admin/', include(admin.site.urls)),
    (r'', include('core.urls')), 
)
