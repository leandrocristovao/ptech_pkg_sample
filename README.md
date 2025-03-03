# ptech_pkg_setting 📦

ptech_pkg_setting é um pacote Django que oferece funcionalidades para gerenciamento de configurações usando o modelo `Setting`.

Este pacote tem objetivo de apresentar o básico para a criação de um pacote reutilizável em DJANGO

[![codecov](https://codecov.io/gh/leandrocristovao/ptech_pkg_setting/graph/badge.svg?token=9P6P2U0K4M)](https://codecov.io/gh/leandrocristovao/ptech_pkg_setting)

## 📌 Requisitos

- Python 3.10+
- Django 5.0+

## ⚙️ Instalação

Clone o repositório e instale as dependências necessárias:

    git clone https://github.com/leandrocristovao/ptech_pkg_setting.git
    cd ptech_pkg_setting
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Para instalar em um projeto existente:

    pip install git+https://github.com/leandrocristovao/ptech_pkg_setting.git

No seu projeto Django, abra o arquivo settings.py e adicione:

    INSTALLED_APPS = [
        ...
        "ptech_pkg_setting",
    ]
    
Aplique as migrações

    python manage.py migrate ptech_pkg_setting

Se houver problemas de migração, tente:

    python manage.py makemigrations ptech_pkg_setting
    python manage.py migrate

## 🚀 Importar e Usar no Código

Agora você pode importar os modelos e funcionalidades do pacote normalmente.
Por exemplo, se o pacote define o model Setting:

    from ptech_pkg_setting.models import Setting

    config = Setting.objects.create(key="modo_escuro", value="ativo")
    print(config)

## 🚀 Manter o Pacote Atualizado

Se houver atualizações no repositório, atualize o pacote com:

    pip install --upgrade git+https://github.com/leandrocristovao/ptech_pkg_setting.git

## ✅ Como Executar os Testes

    pytest

