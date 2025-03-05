from io import StringIO
from django.core.management import call_command
from django.test import TestCase
from ptech_pkg_setting.models import Setting


class SettingsCommandTest(TestCase):
    def setUp(self):
        """Configuração do ambiente de teste, incluindo captura de stdout e stderr"""
        # Criando objetos StringIO para capturar saída e erro
        self.err = StringIO()
        self.out = StringIO()

    def tearDown(self):
        """Limpeza após cada teste para garantir que não há dados persistentes"""
        Setting.objects.all().delete()

    def test_create_setting(self):
        """Testa a criação de uma configuração"""

        # Testa a criação sem parâmetros obrigatórios
        call_command("settings_command", "create", stderr=self.err)
        self.assertEqual(self.err.getvalue(), "Erro: Para criar uma configuração, forneça --key e --value.\n")

        # Limpa o buffer de erro para o próximo uso
        self.err.seek(0)
        self.err.truncate(0)

        # Testa a criação com apenas a chave
        call_command("settings_command", "create", "--key=TEST_KEY", stderr=self.err)
        self.assertEqual(self.err.getvalue(), "Erro: Para criar uma configuração, forneça --key e --value.\n")

        # Limpa novamente antes de capturar o stdout
        self.err.seek(0)
        self.err.truncate(0)

        # Testa a criação com chave e valor
        call_command("settings_command", "create", "--key=TEST_KEY", "--value=TEST_VALUE", stdout=self.out)
        self.assertEqual(self.out.getvalue(), "Configuração criada. TEST_KEY: TEST_VALUE\n")

    def test_create_duplicate_setting(self):
        """Testa a tentativa de criar uma configuração duplicada"""

        # Cria a configuração inicial
        Setting.objects.create(key="DUPLICATE_KEY", value="VALUE1")

        # Testa a tentativa de criar uma chave duplicada
        call_command("settings_command", "create", "--key=DUPLICATE_KEY", "--value=VALUE2", stdout=self.out)
        self.assertIn("Configuração já existe. DUPLICATE_KEY: VALUE1\n", self.out.getvalue())

        # Recupera a configuração existente
        setting = Setting.objects.get(key="DUPLICATE_KEY")

        # Verifica se a configuração não foi criada novamente
        self.assertEqual(setting.value, "VALUE1")  # O valor não deve ter sido alterado

        # Não deve haver duplicidade na tabela
        self.assertEqual(Setting.objects.filter(key="DUPLICATE_KEY").count(), 1)

    def test_delete_existing_setting(self):
        """Testa a exclusão de uma configuração existente"""

        # Cria uma configuração para ser excluída
        Setting.objects.create(key="DELETE_KEY", value="TO_DELETE")

        # Chama o comando de exclusão
        call_command("settings_command", "delete", "--key=DELETE_KEY")

        # Verifica se a configuração foi realmente excluída
        with self.assertRaises(Setting.DoesNotExist):
            Setting.objects.get(key="DELETE_KEY")

    def test_delete_non_existent_setting(self):
        """Testa a remoção de uma configuração inexistente e verifica a mensagem de erro"""

        # Testa a exclusão sem fornecer a chave
        call_command("settings_command", "delete", stderr=self.err)
        self.assertEqual(self.err.getvalue(), "Erro: Para excluir uma configuração, forneça --key.\n")

        # Limpa o buffer de erro
        self.err.seek(0)
        self.err.truncate(0)

        # Testa a exclusão de uma chave que não existe
        call_command("settings_command", "delete", "--key=NON_EXISTENT_KEY", stderr=self.err)
        self.assertEqual(self.err.getvalue(), "Erro: Configuração 'NON_EXISTENT_KEY' não encontrada.\n")

    def test_list_settings(self):
        """Testa a listagem de configurações"""

        # Verifica se não há configurações antes de criar nenhuma
        call_command("settings_command", "list", stdout=self.out)
        self.assertEqual(self.out.getvalue(), "Nenhuma configuração encontrada.\n")

        # Cria uma configuração para testar a listagem
        Setting.objects.create(key="LIST_KEY", value="LIST_VALUE")

        # Verifica se a configuração foi listada corretamente
        call_command("settings_command", "list", stdout=self.out)
        self.assertIn("LIST_KEY: LIST_VALUE", self.out.getvalue())

    def test_get_setting(self):
        """Testa a recuperação de uma configuração existente"""
        
        call_command("settings_command", "get", stderr=self.err)
        self.assertIn('Erro: Para recuperar uma configuração, forneça --key.\n', self.err.getvalue())
        
        Setting.objects.create(key="EXISTING_KEY", value="EXISTING_VALUE")
        call_command("settings_command", "get", "--key=EXISTING_KEY", stdout=self.out)
        self.assertIn('Configuração encontrada: EXISTING_KEY: EXISTING_VALUE (None)\n', self.out.getvalue())
        
        call_command("settings_command", "get", "--key=NON_EXISTENT_KEY", stderr=self.err)
        self.assertIn("Erro: Configuração 'NON_EXISTENT_KEY' não encontrada.\n", self.err.getvalue())

    def test_setting_exists(self):
        """Testa a verificação da existência de uma configuração"""

        call_command("settings_command", "exists", stderr=self.err)
        self.assertIn('Erro: Para verificar existência, forneça --key.\n', self.err.getvalue())

        Setting.objects.create(key="EXISTING_KEY", value="EXISTING_VALUE")
        call_command("settings_command", "exists", "--key=EXISTING_KEY", stdout=self.out)
        self.assertIn("Configuração 'EXISTING_KEY' existe.\n", self.out.getvalue())
        call_command("settings_command", "exists", "--key=NON_EXISTENT_KEY", stdout=self.out)
        self.assertIn("Configuração 'EXISTING_KEY' existe.\n", self.out.getvalue())

    def test_update_setting(self):
        """Testa a atualização de uma configuração existente"""
        
        call_command("settings_command", "update", stderr=self.err)
        self.assertIn('Erro: Para atualizar uma configuração, forneça --key e --value.\n', self.err.getvalue())
                
        Setting.objects.create(key="UPDATE_KEY", value="OLD_VALUE", description="Old description")
        call_command("settings_command", "update", "--key=UPDATE_KEY", "--value=NEW_VALUE", "--description=New description", stdout=self.out)
        setting = Setting.objects.get(key="UPDATE_KEY")
        self.assertEqual(setting.value, "NEW_VALUE")
        self.assertEqual(setting.description, "New description")
        
        call_command("settings_command", "update", "--key=NON_EXISTENT_KEY", "--value=VALUE", "--description=Description", stderr=self.err)
        self.assertIn("Erro: Configuração 'NON_EXISTENT_KEY' não encontrada.\n", self.err.getvalue())