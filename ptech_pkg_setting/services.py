from ptech_pkg_setting.models import Setting


def list_settings():
    """Lista todas as configurações armazenadas no banco de dados."""
    return Setting.objects.all()


def create_setting(key, value):
    """Cria uma nova configuração se não existir. Retorna (Setting, True) se criada, ou (Setting, False) se já existir."""
    key = key.upper()

    # Verifica se a configuração já existe
    setting = Setting.objects.filter(key=key).first()

    if setting:
        return (
            setting,
            False,
        )  # Retorna a configuração existente e False para indicar que não foi criada

    # Cria uma nova configuração se não existir
    setting = Setting.objects.create(key=key, value=value)
    return (
        setting,
        True,
    )  # Retorna a configuração criada e True para indicar que foi criada


def delete_setting(key):
    """Remove uma configuração pelo key."""
    try:
        setting = Setting.objects.get(key=key.upper())
        setting.delete()
        return True
    except Setting.DoesNotExist:
        return False
