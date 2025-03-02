from django.contrib import admin

from meu_pacote_django.models import Setting

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ("key", "value")  # Exibe esses campos na listagem
    search_fields = ("key", "value")  # Permite pesquisar por esses campos
    list_filter = ("key",)  # Adiciona filtro lateral por 'key'
    ordering = ("key",)  # Ordena pela chave

    def save_model(self, request, obj, form, change):
        obj.key = obj.key.upper()  # Garante que a chave seja salva em maiúsculas
        super().save_model(request, obj, form, change)
