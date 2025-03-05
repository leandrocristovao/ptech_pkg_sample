from django.core.management.base import BaseCommand
from ptech_pkg_setting.services import (
    list_settings, create_setting, delete_setting, update_setting, get_setting, setting_exists
)


class Command(BaseCommand):
    help = "Gerencia configurações na tabela Setting (listar, criar, excluir, atualizar, verificar existência, recuperar)"

    def add_arguments(self, parser):
        parser.add_argument(
            "action",
            type=str,
            choices=["list", "create", "delete", "update", "exists", "get"],
            help="Ação a ser executada",
        )
        parser.add_argument(
            "--key",
            type=str,
            help="Chave da configuração (obrigatório para create, delete, update, exists, get)",
        )
        parser.add_argument(
            "--value", type=str, help="Valor da configuração (obrigatório para create e update)"
        )
        parser.add_argument(
            "--description", type=str, help="Descrição da configuração (opcional para update)"
        )

    def handle(self, *args, **options):
        action = options["action"]

        if action == "list":
            settings = list_settings()
            if settings:
                for setting in settings:
                    self.stdout.write(f"{setting.key}: {setting.value} ({setting.description})")
            else:
                self.stdout.write("Nenhuma configuração encontrada.")

        elif action == "create":
            key = options.get("key")
            value = options.get("value")
            description = options.get("description", "")

            if not key or not value:
                self.stderr.write(
                    "Erro: Para criar uma configuração, forneça --key e --value."
                )
                return

            setting, created = create_setting(key, value, description)
            msg = "Configuração criada." if created else "Configuração já existe."
            self.stdout.write(f"{msg} {setting.key}: {setting.value}")

        elif action == "update":
            key = options.get("key")
            value = options.get("value")
            description = options.get("description")

            if not key or not value:
                self.stderr.write(
                    "Erro: Para atualizar uma configuração, forneça --key e --value."
                )
                return

            updated = update_setting(key, value, description)
            if updated:
                self.stdout.write(f"Configuração '{key.upper()}' atualizada.")
            else:
                self.stderr.write(f"Erro: Configuração '{key.upper()}' não encontrada.")

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

        elif action == "exists":
            key = options.get("key")

            if not key:
                self.stderr.write("Erro: Para verificar existência, forneça --key.")
                return

            exists = setting_exists(key)
            if exists:
                self.stdout.write(f"Configuração '{key.upper()}' existe.")
            else:
                self.stdout.write(f"Configuração '{key.upper()}' não existe.")

        elif action == "get":
            key = options.get("key")

            if not key:
                self.stderr.write("Erro: Para recuperar uma configuração, forneça --key.")
                return

            setting = get_setting(key)
            if setting:
                self.stdout.write(f"Configuração encontrada: {setting.key}: {setting.value} ({setting.description})")
            else:
                self.stderr.write(f"Erro: Configuração '{key.upper()}' não encontrada.")
