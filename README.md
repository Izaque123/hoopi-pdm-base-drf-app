# Base DRF App - Django 5 + DRF 3.16

[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16.1-red.svg)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![JWT](https://img.shields.io/badge/JWT-Simple--JWT-orange.svg)](https://github.com/jazzband/djangorestframework-simplejwt)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-Spectacular-8A2BE2.svg)](https://github.com/tfranzel/drf-spectacular)
[![CORS](https://img.shields.io/badge/CORS-Enabled-success.svg)](https://github.com/adamchainz/django-cors-headers)

Projeto base modular para desenvolvimento de APIs REST com Django e Django Rest Framework, implementando arquitetura em camadas bem definidas com autenticação JWT, documentação automática e suporte a CORS.

## Objetivo

Fornecer uma base sólida, profissional e escalável para desenvolvimento de APIs, com separação clara de responsabilidades através de camadas arquiteturais (Business, Rules, Helpers, State), incluindo autenticação moderna e documentação automatizada.

## Características

- **Autenticação JWT**: Autenticação stateless com tokens seguros
- **Documentação Automática**: OpenAPI com Swagger UI e ReDoc
- **CORS Configurado**: Pronto para integração com frontends
- **Arquitetura em Camadas**: Business, Rules, Helpers e State
- **Modular**: Fácil extensão com novos apps
- **Reutilizável**: Models, mixins e utilitários base
- **Testável**: Camadas desacopladas facilitam testes
- **Bem Documentado**: Exemplos e guias completos
- **Produção Ready**: Configurações para desenvolvimento e produção
- **Clean Code**: Segue PEP8 e boas práticas Django/DRF

## Quick Start

##  Quick Start

### Instalação

```bash
# Clone o repositório
git clone <repository-url>

# Crie ambiente virtual
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instale dependências
pip install -r requirements.txt

# Execute migrações
python manage.py makemigrations
python manage.py migrate

# Crie superusuário
python manage.py createsuperuser

# Execute o servidor
python manage.py runserver
```

### Criar Novo App

```bash
# Use o script auxiliar
python manage.py startapp nome_do_app

# Ou manualmente
mkdir nome_do_app
cd nome_do_app
# Crie os arquivos: __init__.py, apps.py, models.py, business.py, rules.py, helpers.py
```
