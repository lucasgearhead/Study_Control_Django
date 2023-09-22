# API de Controle Estudantil

Esta é uma API desenvolvida em Django para ajudar no gerenciamento de alunos, disciplinas e tarefas. A API permite a criação, atualização, exclusão e consulta destes.

## Índice

- [Configuração do Ambiente](#configuração-do-ambiente)
- [Modelos de Dados](#modelos-de-dados)
- [Documentação da API](#documentação-da-api)
- [Testando a API](#testando-a-api)
- [Manipulação de Erros](#manipulação-de-erros)
- [Validação de Dados](#validação-de-dados)

## Configuração do Ambiente

Para configurar o ambiente de desenvolvimento, siga estes passos:

1. Clone este repositório: `git clone https://github.com/lucasgearhead/Study_Control_Django.git`
2. Crie um ambiente virtual: `python -m venv .env`
3. Ative o ambiente virtual: `source .env/bin/activate` (Linux/macOS) ou `.env\Scripts\activate` (Windows)
4. Instale as dependências: `pip install -r requirements.txt`
5. Crie os arquivos de preparação para migrações: `python manage.py makemigrations`
5. Atualize os modelos no banco de dados aplicando as migrações: `python manage.py migrate`
6. Inicie a aplicação: `python manage.py runserver`

(obs) Importante o nome do Ambiente Virtual ser: `.env`!

## Modelos de Dados

A aplicação possui três modelos de dados principais:

- **Aluno**: Representa um aluno com `nome` e `email`.
- **Disciplina**: Representa uma disciplina com `nome` e `descrição`.
- **Tarefa**: Representa uma tarefa com campos `titulo`, `descrição`, `data de entrega` e se `concluida` associada ao aluno.

## Documentação da API

A documentação da API está disponível no arquivo `endpoints.postman_collections.json`. Ela tem informações detalhadas sobre como usar cada endpoint, incluindo exemplos de solicitações. Certifique-se de consultar a documentação para entender e usar todas as operações disponíveis na API de forma eficaz.

## Testando a API

Você pode testar a API usando [Postman](https://www.postman.com/). Certifique-se de seguir a documentação para fazer solicitações corretamente.

## Manipulação de Erros

A API lida adequadamente com erros, fornecendo respostas de erro apropriadas com códigos de status HTTP significativos.

## Validação de Dados

A API realiza validações adequadas dos dados de entrada, incluindo a verificação de datas, formatos de e-mail, campos obrigatórios e outros requisitos específicos para cada entidade.