# tests/test_models.py
from ptech_pkg_sample.models import Setting
import pytest
from django.test import TestCase


@pytest.mark.django_db
class SettingModelTest(TestCase):

    def test_create_setting(self):
        """Testa a criação de um objeto Setting e verifica se a chave é armazenada em maiúsculas."""
        setting = Setting.objects.create(key="modo_escuro", value="ativo")
        self.assertEqual(setting.key, "MODO_ESCURO")
        self.assertEqual(setting.value, "ativo")

    def test_read_setting(self):
        """Testa a leitura de um objeto Setting do banco de dados."""
        setting = Setting.objects.create(key="idioma", value="Português")
        fetched = Setting.objects.get(key="IDIOMA")  # A chave é salva em maiúsculas
        self.assertEqual(fetched.value, "Português")

    def test_update_setting(self):
        """Testa a atualização do valor de um Setting existente."""
        setting = Setting.objects.create(key="volume", value="50")
        setting.value = "80"
        setting.save()
        updated = Setting.objects.get(key="VOLUME")
        self.assertEqual(updated.value, "80")

    def test_delete_setting(self):
        """Testa a remoção de um objeto Setting."""
        setting = Setting.objects.create(key="notificações", value="ativado")
        setting.delete()
        self.assertEqual(Setting.objects.count(), 0)

    def test_key_uppercase_on_save(self):
        """Testa se a chave é automaticamente convertida para maiúsculas antes de salvar."""
        setting = Setting.objects.create(key="tema", value="claro")
        self.assertEqual(setting.key, "TEMA")

    def test_unique_key_constraint(self):
        """Testa a restrição de unicidade da chave."""
        Setting.objects.create(key="cache", value="ativado")
        with self.assertRaises(Exception):  # Deveria levantar uma exceção de unicidade
            Setting.objects.create(key="cache", value="desativado")
