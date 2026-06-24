# Project Emily

Sistema web desenvolvido para automação de cálculos de engenharia elétrica, geração de memoriais de cálculo, relatórios técnicos e processamento de documentos.

## 📋 Sobre o Projeto

O Project Emily é uma aplicação desenvolvida utilizando Django como framework principal, permitindo a execução de cálculos técnicos, geração de documentos automatizados e gerenciamento de informações relacionadas a projetos de engenharia.

O sistema foi projetado para aumentar a produtividade das equipes técnicas, reduzindo erros manuais e padronizando a geração de documentos.

---

## 🚀 Tecnologias Utilizadas

### Backend

* Python 3.8+
* Django
* Celery
* Redis

### Banco de Dados

* PostgreSQL
* SQLite (ambiente de desenvolvimento)

### Frontend

* HTML5
* CSS3
* JavaScript
* jQuery
* Bootstrap

### Geração de Documentos

* OpenPyXL
* Pandas
* Templates Excel

### Servidor

* Apache
* WSGI

---

## 📂 Estrutura do Projeto

```text
Project-Emily/
│
├── htdocs/                # Aplicações Django
├── docs/                  # Documentação
├── requirements/          # Dependências do projeto
├── templates/             # Templates HTML
├── static/                # Arquivos estáticos
├── celery/                # Configuração de tarefas assíncronas
├── error_img/             # Imagens de erro
├── manage.py              # Gerenciador Django
└── README.md
```

---

## ⚙️ Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/AlexSanderTht/Project-Emily.git
cd Project-Emily
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuração

### Banco de Dados

Configure as credenciais do banco no arquivo:

```python
settings.py
```

Exemplo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Redis

Inicie o Redis:

```bash
redis-server
```

---

## Celery

Executar worker:

```bash
celery -A projeto worker -l info
```

Executar scheduler:

```bash
celery -A projeto beat -l info
```

---

## ▶️ Executando o Projeto

Aplicar migrações:

```bash
python manage.py migrate
```

Criar superusuário:

```bash
python manage.py createsuperuser
```

Executar servidor:

```bash
python manage.py runserver
```

Acessar:

```text
http://127.0.0.1:8000/
```

---

## 📊 Funcionalidades

* Geração automática de memoriais de cálculo.
* Processamento de arquivos Excel.
* Importação e exportação de dados.
* Relatórios técnicos.
* Execução de tarefas assíncronas.
* Gerenciamento de projetos.
* Interface web responsiva.
* Tratamento de erros personalizados.

---

## 🛠 Boas Práticas

### Branches

```text
feature/nome-funcionalidade
bugfix/correcao
hotfix/correcao-urgente
```

### Commits

```text
feat: nova funcionalidade
fix: correção de erro
refactor: refatoração
docs: documentação
test: testes
```

---

## 📌 Requisitos

* Python 3.8+
* Redis
* PostgreSQL
* Apache (produção)

---

## 👨‍💻 Desenvolvedor

Alex Sander Perini dos Santos

GitHub:
https://github.com/AlexSanderTht

---

## 📄 Licença

Este projeto é de uso interno e possui direitos reservados aos seus respectivos autores.
