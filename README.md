# ptech-pkg-sample 📦

ptech-pkg-sample é um pacote Django que oferece funcionalidades para gerenciamento de configurações usando o modelo `Setting`.

Este pacote tem objetivo de apresentar o básico para a criação de um pacote reutilizável em DJANGO

## 📌 Requisitos

- Python 3.8+
- Django 5.0+

## ⚙️ Instalação

Clone o repositório e instale as dependências necessárias:

    git clone https://github.com/seu-usuario/meu_pacote_django.git
    cd meu_pacote_django
    pip install -r requirements.txt```

Para instalar em um projeto existe:

    pip install git+https://github.com/leandrocristovao/ptech-pkg-sample.git

No seu projeto Django, abra o arquivo settings.py e adicione:

    INSTALLED_APPS = [
        ...
        "meu_pacote_django",
    ]
    
Aplique as migrações

    python manage.py migrate meu_pacote_django

Se houver problemas de migração, tente:

    python manage.py makemigrations meu_pacote_django
    python manage.py migrate

## 🚀 Importar e Usar no Código

Agora você pode importar os modelos e funcionalidades do pacote normalmente.
Por exemplo, se o pacote define o model Setting:

    from meu_pacote_django.models import Setting

    config = Setting.objects.create(key="modo_escuro", value="ativo")
    print(config)

## 🚀 Manter o Pacote Atualizado

Se houver atualizações no repositório, atualize o pacote com:

    pip install --upgrade git+https://github.com/leandrocristovao/ptech-pkg-sample.git

## ✅ Como Executar os Testes

    pytest