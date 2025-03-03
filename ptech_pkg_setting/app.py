from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PtechPkgSettingConfig(AppConfig):
    name = 'ptech_pkg_setting'  # O nome do seu pacote
    verbose_name = _('PTECH')  # O nome que aparecerá no Django Admin
