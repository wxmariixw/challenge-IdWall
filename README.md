# Challenge IdWall

## Desafio

Esse ano fomos desafiados pela IdWall para criarmos uma aplicação web que ajudasse a combater a lavagem de dinheiro e o financiamento de práticas terroristas, gerenciando as duas listas de pessoas procuradas da Interpol e do FBI.

### 1º parte

Na primeria parte do projeto nós criamos um sistema privado das duas organizações e filiadas, realizando um login criado a partir de um usuário administrador, onde será possível realizar uma busca por nome e contendo filtros por idade, crime, local de nascimento, local do crime e insituição registrado. Também será disponibilizado um dashboard contendo gráficos de comparação de estatísticas.

### 2º parte

Agora na segunda parte nos foi proposto criar um crawler que colete os dados nas duas insitituições, alimente o banco de dados e desenvolver o back-end da aplicação idealizada, utilizando técnicas aprendidas durante o curso e criando um sistema funcional.

---

## To-do

- [x] Documentação detalhada

  - [x] Descrever técnicas que foram utilizadas para realizar a coleta de dados com o crawler
  - [x] Bibliotecas que foram utilizadas
  - [x] Descrever desafios a serem encarados

- [x] Implementação

  - [x] Codigo fonte
    - [x] Crawler
    - [x] Ingestão no banco de dados
    - [x] Back-end da aplicação

- [x] Apresentação
  - [x] Video demonstrando a API ativa

## Linguagens e ferramentas utilizadas

### Linguagem

- Python

### Framework

- FastAPI

### Bibliotecas

- Pandas
- Request
- SQLalchemy
- typing
- datetime
- pydantic

### Banco de dados

- PostgreSQL

## Como utilizar a aplicação

### Preparando o ambiente virutal

<details>
  <summary>Windows</summary>
  <ol>
    <li>
      <p>Crie o ambiente vitual</p>
      <code style="white-space:nowrap;">python3 -m venv venv</code>
    </li>
    <li>
      <p>Ative o ambiente virtual</p>
      <code style="white-space:nowrap;">venv\Scripts\activate.bat</code>
    </li>
  </ol>
</details>

<details>
  <summary>Linux</summary>
  <ol>
    <li>
      <p>Crie o ambiente vitual</p>
      <code style="white-space:nowrap;">virtualenv venv</code>
    </li>
    <li>
      <p>Ative o ambiente virtual</p>
      <code style="white-space:nowrap;">cd venv</code>
      <p></p>
      <code style="white-space:nowrap;">source bin/activate</code>
    </li>
  </ol>
</details>

**Instale os requisitos**

```
pip install -r requirements.txt
```

**Caso realize alguma alteração sempre anote no requirements**

```
pip freeze > requirements.txt
```

### Rodando o app

- Para rodar o app, rode o seguinte comando no terminal

```
uvicorn main:app --reload
```

### Documentação

Para acessar a documentação das rotas, basta dicionar a rota `/docs`

## Desenvolvedores

[André Luz](https://github.com/andreluz)

[Eduardo Nunes](https://github.com/edununes22)

[Juan Marco Camacho](https://github.com/juanmqc22)

[Mariana Abreu](https://github.com/wxmariixw)

[Miguel Marcondes](https://github.com/miguelmarcondes)

## Link para este repositório

[Repositório Git](https://github.com/wxmariixw/challenge-IdWall)