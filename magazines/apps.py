from django.apps import AppConfig


class MagazinesConfig(AppConfig):
    name = 'magazines'

    def ready(self):
        import magazines.signals