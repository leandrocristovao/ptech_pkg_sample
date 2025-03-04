from django.core.management.base import BaseCommand
from ptech_pkg_setting.services import list_settings, create_setting, delete_setting


class Command(BaseCommand):
    help = "Gerencia configurações na tabela Setting (listar, criar, excluir)"

    def add_arguments(self, parser):
        parser.add_argument(
            "action",
            type=str,
            choices=["list", "create", "delete"],
            help="Ação a ser executada",
        )
        parser.add_argument(
            "--key",
            type=str,
            help="Chave da configuração (obrigatório para create/delete)",
        )
        parser.add_argument(
            "--value", type=str, help="Valor da configuração (obrigatório para create)"
        )

    def handle(self, *args, **options):
        action = options["action"]

        if action == "list":
            settings = list_settings()
            if settings:
                for setting in settings:
                    self.stdout.write(f"{setting.key}: {setting.value}")
            else:
                self.stdout.write("Nenhuma configuração encontrada.")

        elif action == "create":
            key = options.get("key")
            value = options.get("value")

            if not key or not value:
                self.stderr.write(
                    "Erro: Para criar uma configuração, forneça --key e --value."
                )
                return

            setting, created = create_setting(key, value)
            msg = "Configuração criada." if created else "Configuração atualizada."
            self.stdout.write(f"{msg} {setting.key}: {setting.value}")

        elif action == "delete":
            key = options.get("key")

            if not key:
                self.stderr.write("Erro: Para excluir uma configuração, forneça --key.")
                return

            deleted = delete_setting(key)
            if deleted:
                self.stdout.write(f"Configuração '{key.upper()}' removida.")
            else:
                self.stderr.write(f"Erro: Configuração '{key.upper()}' não encontrada.")
