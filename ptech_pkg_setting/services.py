from ptech_pkg_setting.models import Setting


def list_settings():
    """Lista todas as configurações armazenadas no banco de dados."""
    return Setting.objects.all()


def create_setting(key, value, description=""):
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
    setting = Setting.objects.create(key=key, value=value, description=description)
    return (
        setting,
        True,
    )  # Retorna a configuração criada e True para indicar que foi criada


def setting_exists(key):
    """Verifica se uma configuração existe no banco de dados."""
    return Setting.objects.filter(key=key.upper()).exists()

def get_setting(key):
    """Recupera uma configuração pelo key. Retorna None se não existir."""
    return Setting.objects.filter(key=key.upper()).first()

def update_setting(key, value, description=None):
    """Atualiza o value e, se fornecido, o description de uma configuração existente. 
    Retorna True se atualizado, False se a configuração não existir."""
    
    setting = Setting.objects.filter(key=key.upper()).first()
    
    if not setting:
        return False  # Retorna False se a configuração não existir

    setting.value = value  # Sempre atualiza o value
    
    if description is not None:
        setting.description = description  # Apenas atualiza se description não for None

    setting.save()
    return True  # Retorna True indicando que a atualização foi bem-sucedida

def delete_setting(key):
    """Remove uma configuração pelo key."""
    try:
        setting = Setting.objects.get(key=key.upper())
        setting.delete()
        return True
    except Setting.DoesNotExist:
        return False
