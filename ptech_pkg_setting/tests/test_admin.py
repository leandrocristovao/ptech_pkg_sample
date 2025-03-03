from django.contrib.admin.sites import site
from django.test import TestCase
from ptech_pkg_setting.admin import SettingAdmin
from ptech_pkg_setting.models import Setting
from django.contrib.auth import get_user_model

class SettingAdminTest(TestCase):
    def setUp(self):
        # Criar um superusuário para acessar o admin
        self.user = get_user_model().objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpass"
        )
        
        # Criar um objeto Setting
        self.setting = Setting.objects.create(key="modo_escuro", value="ativo")

        # Criar uma instância do admin do modelo
        self.admin = SettingAdmin(model=Setting, admin_site=site)

    def test_setting_registered_in_admin(self):
        """Testa se o modelo Setting está registrado no Django Admin"""
        self.assertIn(Setting, site._registry)

    def test_list_display(self):
        """Testa se os campos list_display estão corretos"""
        self.assertEqual(self.admin.list_display, ("key", "value"))

    def test_search_fields(self):
        """Testa se os campos search_fields estão corretos"""
        self.assertEqual(self.admin.search_fields, ("key", "value"))

    def test_list_filter(self):
        """Testa se o list_filter está configurado corretamente"""
        self.assertEqual(self.admin.list_filter, ("key",))

    def test_ordering(self):
        """Testa se o ordering está correto"""
        self.assertEqual(self.admin.ordering, ("key",))

    def test_save_model_converts_key_to_uppercase(self):
        """Testa se o método save_model transforma a chave em maiúscula"""
        self.setting.key = "modo_claro"
        self.admin.save_model(None, self.setting, None, None)
        self.assertEqual(self.setting.key, "MODO_CLARO")  # Verifica se foi convertido
