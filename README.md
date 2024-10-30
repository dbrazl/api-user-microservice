<h1 align="center">⚙️ Microserviço de usuários</h1>
<br>

![Banner](https://github-dbrazl.s3.us-east-1.amazonaws.com/api-user-microservice/banner.svg?v=1.0.0)

<p align="center">
  Bem-vindo a API de usuário! Este espaço foi criado como um estudo de caso do uso do Flask com boas práticas de programação.
</p>

<br>
<p align="center">
  <img src="https://img.shields.io/badge/autor-@dbrazl-FB8C00?style=flat" alt="Autor: @dbrazl">
</p>
<br>

## 🎯 Objetivo

<p align="justify">
  O objetivo deste projeto é demonstrar o uso de boas práticas de programação, incluindo os princípios SOLID, Clean Code, Clean Architecture e Design Patterns, aplicados ao uso de Python com Flask, para garantir uma estrutura de código organizada, escalável e de fácil manutenção. O serviço é projetado para suportar operações CRUD básicas de usuários e foi estruturado com foco na separação de responsabilidades e inversão de dependências, buscando maximizar a qualidade e a clareza do código.
</p>

## 🛠 Tecnologias

<p align="justify">
  As tecnologias utilizadas nesse projeto foram:
</p>

![Python](https://img.shields.io/badge/Python-333333?style=flat&logo=python&logoColor=green)
![Flask](https://img.shields.io/badge/Flask-333333?style=flat&logo=flask)
![Pydantic](https://img.shields.io/badge/Pydantic-333333?style=flat&logo=pydantic)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat&logo=sqlalchemy&logoColor=red)
![Injector](https://img.shields.io/badge/Injector-333333?style=flat&logo=python&logoColor=lightgreen)
![FlaskInjector](https://img.shields.io/badge/FlaskInjector-333333?style=flat&logo=python&logoColor=lightgreen)
![PyJWT](https://img.shields.io/badge/PyJWT-333333?style=flat&logo=python&logoColor=lightgreen)
![Flask-JWT-Extended](https://img.shields.io/badge/Flask%2d-JWT%2d-Extended-333333?style=flat&logo=python&logoColor=lightgreen)
![Dotenv](https://img.shields.io/badge/Dotenv-333333?style=flat&logo=python&logoColor=lightgreen)

## 📥 Instalação

Sigo os passo abaixo para pode instalar o projeto na máquina alvo.

### Passo 1: Download

<p align="justify">
  O primeiro passo é o download do projeto para a máquina alvo. Para isso é necessário que você tenha o Git instalado e uma conta no GitHub.
</p>
<p align="justify">
  Com esses requisitos atendidos, uma das formas de fazer o download dos arquivos do projeto é via SSH. Caso ainda não tenha, cadastre uma chave SSH na máquina alvo e a chave pública no GitHub, e após faça o clone do projeto seguindo a instrução abaixo:
</p>

```bash
  git clone git@github.com:dbrazl/api-user-microservice.git
```

### Passo 2: Ambiente virtual

<p align="justify">
  Com o projeto na máquina alvo, você pode criar um ambiente virtual para instalação dos pacotes, o que eu fortemente recomendo. Caso não queira, pule essa instrução.
</p>
<p align="justify">
  Para se criar um ambiente virtual, você deve rodar o seguinte comando:
</p>

```bash
  python -m venv .venv
```

<p align="justify">
  Após rodá-lo, um novo diretório nomeado como .venv aparecerá na pasta raiz do projeto. Usaremos esse ambiente para rodar a aplicação Python.
</p>

<p align="justify">
  Para iniciar o ambiente, use o seguinte comando no terminal para máquinas Linux:
</p>

```bash
  source .venv/bin/activate
```

<p align="justify">
  Já para desativá-lo, use o seguinte comando:
</p>

```bash
  deactivate
```

<p align="justify">
  Para o próximo passo, mantenha o ambiente virtual ativo. Usar um ambiente virtual evita conflito de pacotes do Python com outros projetos do seu sistema.
</p>

<p align="justify">
  Após finalizar a aplicação, lembre-se de desativar o ambiente virtual.
</p>

### Passo 3: Instalação de pacotes

<p align="justify">
  Para instalar os pacotes do projeto, use o seguinte comando na raiz do projeto:
</p>

```bash
  pip install -r requirements.txt
```

## 🚀 Como Rodar

<p align="justify">
  Com a etapa de instalação finalizada, crie uma copia do arquivo <strong>.env.example</strong> na raiz do projeto, e o renomeie para <strong>.env</strong>. Após isso, altere as variáveis ambientes para a de sua preferência.
</p>

<p align="justify">
  Por fim, inicie a aplicação rodando o seguinte comando abaixo:
</p>

```bash
  python entry.py
```

## 📚 Documentação

Em breve estará disponível.

## 📬 Contato

<p align="justify">
  Se você tiver dúvidas ou sugestões, pode me encontrar em <a href="mailto:daniel.braz@vyox.io">daniel.braz@vyox.io</a> ou através do <a href="https://www.linkedin.com/in/dbrazl/">LinkedIn</a>.
</p>
