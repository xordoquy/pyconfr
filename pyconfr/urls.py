from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static

from django.views.generic.simple import redirect_to
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

import symposion.views

WIKI_SLUG = r"(([\w-]{2,})(/[\w-]{2,})*)"

import settings

urlpatterns = patterns("",

    url(r"^$", redirect_to, {"url": "/%s/" % settings.CONFERENCE_YEAR}),
    url(r"^%s/" % settings.CONFERENCE_YEAR,
        include(patterns("",

        url(r"^$", direct_to_template, {
            "template": "homepage.html",
        }, name="home"),
        url(r"^admin/", include(admin.site.urls)),
        
        url(r"^account/signup/$", symposion.views.SignupView.as_view(), name="account_signup"),
        url(r"^account/login/$", symposion.views.LoginView.as_view(), name="account_login"),
        url(r"^account/", include("account.urls")),
        
        url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
        url(r"^speaker/", include("symposion.speakers.urls")),
        url(r"^proposals/", include("symposion.proposals.urls")),
        url(r"^sponsors/", include("symposion.sponsorship.urls")),
        url(r"^boxes/", include("symposion.boxes.urls")),
        url(r"^teams/", include("symposion.teams.urls")),
        url(r"^reviews/", include("symposion.reviews.urls")),
        url(r"^schedule/", include("symposion.schedule.urls")),
        url(r"^markitup/", include("markitup.urls")),
        url(r"^posters/", include("pyconfr.proposals.urls")),
        
        url(r"^", include("symposion.cms.urls")),

    ))),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
