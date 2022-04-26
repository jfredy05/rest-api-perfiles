# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProfilesApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles_project.apps.profiles_api'
    verbose_name = _("Profiles API")
