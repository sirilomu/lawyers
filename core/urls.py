from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews

urlpatterns = patterns('',
	#Examples:
    #url(r'^$', coreviews.SplashView.as_view()),
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^$', coreviews.LandingView.as_view()),
)
