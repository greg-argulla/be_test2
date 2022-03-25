from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "be_test2.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import be_test2.users.signals  # noqa F401
        except ImportError:
            pass
