# API de um portal de noticias
## Descrição
O backend é desenvolvido em Python 3.9 usando FastAPI, Mongo, REST e Clean Architecture.

## SETUP
Antes de rodar a aplicação configure o .env com a url do Mongo

## Rodando com docker (http://localhost:8081/)
Primeiro de tudo deve ter o docker e o docker-compose instalado
Deve acessar a pasta do docker, para isso execute os comandos:
```console
$ cd docker
```
```console
$ docker-compose up --b -d
```
## Rodando com o uvicorn (http://localhost:8000/) 
Necessita do Python 3.7 ou superior e o uvicorn instalado na máquina, tendo isso em mente execute os seguintes comandos:
```console
$ pip3 install src/requirements.txt
```
```console
$ uvicorn src.main:app --reload
```

## Acessando a DOCUMENTAÇÃO
Após a aplicação rodando é possível acessar uma documentação pela rota /docs
http://localhost:8000/docs -> UVICORN
http://localhost:8081/docs -> DOCKER
![https://i.imgur.com/l5MliBd.png](https://i.imgur.com/l5MliBd.png)


## Análise de código
Submeti o código a uma analise automática no Better Code Hub e atende todos os requisitos
![https://i.imgur.com/DL12SEh.png](https://i.imgur.com/DL12SEh.png)


## BANCO DE DADOS 
O Banco de dados utilizado foi o Mongo, usando a lib pymongo para manipular os dados
##### Modelagem
News:
* _id: uuid
* title: string
* newsText: string
* author: uuid (Chave para entidade Author)
* timestamp: integer

Author:
* _id: uuid
* firstName: string
* lastName: string

## Clean Architeture
É uma forma programar usando alguns patterns, separando a aplicada em camadas visando o desacoplamento facilidando a sustentação do sistema a longo prazo.
https://medium.com/luizalabs/descomplicando-a-clean-architecture-cf4dfc4a1ac6

## Casos de uso
1. Cadastrar uma noticia (http://localhost:8000/docs#/default/create_news_news_post)
2. Consultar Noticias (http://localhost:8000/docs#/default/find_news_find_news__search__get)
    Através de um parâmetro na URL e busca dados em duas tabelas News e Author
3. Listar Noticias (http://localhost:8000/docs#/default/list_news_news_get)
    Lista todas as noticias no DB
4. Atualizar Noticias (http://localhost:8000/docs#/default/update_news_news_put)
    Enviando um PUT mas passando o id da Noticia, deve ser enviado o payload completo
5. Deletar Noticias (http://localhost:8000/docs#/default/delete_news_news___id__delete)
    Passando o UUID do usuário na url

