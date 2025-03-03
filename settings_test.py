# settings_test.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "ptech_pkg_setting",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",  # Usa um banco de dados em memória para testes
    }
}

SECRET_KEY = "chave-secreta-para-testes"
