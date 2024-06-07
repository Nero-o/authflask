# **PlataformaMaps Backend Documentation**

## **1. Visão Geral**

### **1.1. Objetivo**
A PlataformaMaps é uma aplicação desenvolvida para facilitar o cadastro e acompanhamento de propostas dos produtos Home Equity e Constru Maps oferecidos pela empresa Maps Crédito. A plataforma permite o gerenciamento eficiente dessas propostas, integrando-se com o Pipefy para a gestão interna e oferecendo uma interface intuitiva para os usuários.

### **1.2. Funcionalidades Principais**
- **Cadastro de Propostas**: Cadastro de novas propostas para os produtos da empresa.
- **Acompanhamento de Propostas**: Integração com o Pipefy para acompanhar o status das propostas.
- **Autenticação de Usuários**: Login e registro de usuários com autenticação baseada em JWT.
- **Pesquisa de Propostas**: Busca de propostas por ID e visualização de todas as propostas cadastradas.

---

## **2. Configuração e Instalação**

### **2.1. Requisitos**
- **Python 3.8+**
- **PostgreSQL**
- **Virtualenv**
- **Dependências especificadas em `requirements.txt`**

### **2.2. Instalação**
1. **Clonar o Repositório**:
    ```bash
    git clone https://github.com/usuario/projeto-plataformaMaps.git
    cd projeto-plataformaMaps
    ```

2. **Criar e Ativar o Ambiente Virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Instalar Dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar o Banco de Dados**:
    - Crie um banco de dados PostgreSQL e configure a URI de conexão no `config.py`.

5. **Executar as Migrações**:
    ```bash
    flask db upgrade
    ```

6. **Iniciar a Aplicação**:
    ```bash
    flask run
    ```

---

## **3. Estrutura do Projeto**

### **3.1. Arquitetura**
O projeto segue a arquitetura MVC (Model-View-Controller), separando claramente a lógica de negócios, manipulação de dados e as rotas de API.

### **3.2. Diretórios e Arquivos Principais**
```plaintext
plataformaMaps/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── card.py
│   │   ├── approved_cards.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_services.py
│   │   ├── pipefy_services.py
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── card_controller.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   ├── card_routes.py
│   │
│   ├── __init__.py
│   └── config.py
│
├── migrations/
├── venv/
├── config.py
├── run.py
└── requirements.txt
```

### 3.3. Descrição dos Arquivos e Diretórios
- app/__init__.py: Inicializa a aplicação Flask.
- app/models/: Contém os modelos do banco de dados.
- user.py: Modelo de usuário.
- card.py: Modelo de proposta.
- approved_cards.py: Modelo de propostas aprovadas.
- app/services/: Implementa a lógica de negócios e serviços externos.
- auth_services.py: Gerencia autenticação e autorização.
- pipefy_services.py: Integração com o Pipefy.
- app/controllers/: Lógica de controle entre as rotas e serviços.
- card_controller.py: Controla as operações de propostas.
- app/routes/: Define as rotas da API.
- auth_routes.py: Rotas de autenticação.
- card_routes.py: Rotas de gerenciamento de propostas.
- config.py: Configurações da aplicação.
- run.py: Ponto de entrada da aplicação.
- requirements.txt: Lista de dependências do projeto.

## 4. Configurações (config.py)

### 4.1. Parâmetros de Configuração
Este arquivo contém as configurações centrais da aplicação, incluindo:
- `SECRET_KEY`: Utilizada para a criptografia de tokens JWT e outros mecanismos de segurança.
- `SQLALCHEMY_DATABASE_URI`: URI de conexão com o banco de dados PostgreSQL.
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Desabilita as notificações de modificação do SQLAlchemy para performance.

## 5. Ponto de Entrada (`run.py`)
### 5.1. Inicialização da Aplicação
Responsável por iniciar a aplicação Flask. Configura a aplicação para rodar em modo de depuração durante o desenvolvimento.

## 6. Modelos (`app/models/`)

### 6.1. User (app/models/user.py)
Modelo de usuário, armazenando informações básicas para autenticação e identificação.

### 6.2 Card (app/models/card.py)
Modelo para armazenar informações das propostas cadastradas na plataforma.

### 6.3A pproved Card (app/models/approved_cards.py)
Modelo para armazenar informações de propostas aprovadas.

## 7. Serviços (app/services/)

### 7.1. Auth Services (app/services/auth_services.py)
Responsável pela autenticação de usuários, registro e gerenciamento de tokens JWT.

#### 7.1.1. Registro de Usuário
Função register_user para validar e registrar novos usuários.

#### 7.1.2. Login de Usuário
Função login_user para autenticar usuários e gerar tokens JWT.

### 7.2. Pipefy Services (app/services/pipefy_services.py)
Gerencia a integração com o Pipefy para envio e acompanhamento de propostas.

### 7.3. Database Service (app/services/db.py)
Configuração e inicialização do SQLAlchemy para manipulação do banco de dados.

## 8. Controladores (app/controllers/)
### 8.1. Card Controller (app/controllers/card_controller.py)
Gerencia a lógica de controle para as operações relacionadas a propostas.

#### 8.1.1. Criação de Propostas
Função create_pipefy_cards para validar e criar propostas, tanto na plataforma quanto no Pipefy.

#### 8.1.2. Recuperação de Propostas
Função get_cards para recuperar todas as propostas cadastradas.

#### 8.1.3. Recuperação de Proposta por ID
Função get_card_by_id para recuperar uma proposta específica pelo ID.

#### 8.1.4. Aprovação de Propostas
Função approve_cards para aprovar propostas e movê-las para a tabela de propostas aprovadas.

## 9. Rotas (app/routes/)
### 9.1. Auth Routes (app/routes/auth_routes.py)
Define as rotas para autenticação de usuários, como registro e login.

### 9.2. Card Routes (app/routes/card_routes.py)
Define as rotas para gerenciamento de propostas, incluindo criação, listagem e aprovação.

## 10. Segurança e Boas Práticas

- Utilize variáveis de ambiente para armazenar informações sensíveis, como chaves de API e credenciais de banco de dados.
- Garanta a segurança das senhas dos usuários utilizando hashes.
- Valide e sanitize as entradas do usuário para prevenir injeções SQL e outros ataques.

