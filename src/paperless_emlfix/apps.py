from django.apps import AppConfig
from django.conf import settings

from paperless_emlfix.signals import emlfix_consumer_declaration


class PaperlessEmlFixConfig(AppConfig):
    name = "paperless_emlfix"

    def ready(self):
        from documents.signals import document_consumer_declaration

        if settings.TIKA_ENABLED:
            document_consumer_declaration.connect(emlfix_consumer_declaration)
        AppConfig.ready(self)
