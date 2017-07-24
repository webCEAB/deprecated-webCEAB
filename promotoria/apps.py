from __future__ import unicode_literals

from django.apps import AppConfig


class PromotoriaConfig(AppConfig):
    name = 'promotoria'

    def ready(self):
    	from promotoria import signals