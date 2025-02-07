#  DjangoRest
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/GuilhermeGTM/ProjetoFilmes/blob/main/LICENSE) 

# Sobre o projeto
Esse projeto foi a primeira interação minha com DRF, na primeira etapa foi usado o models serializer, APIViews para os metodos HTTP. Na segunda etapa foi criado um CRUD genérico onde foi sobrescrito os metodos isso tudo na versão api/v1, na api/v2 foi utilizado os viewsets e routers, assim diminuindo muito as linhas de codigos, foi customizado os viewsets, relacionamentos entre os models e paginação de dados. Na terceira etapa foi feita autenticação via token, uso de permissões para determinados usuarios, limitador de numero de requisições com Throttling e customização de validação/serialização de dados atravez de funções. Na ultima etapa fizemos os testes com modulo requests e jsonpath, foi testado os métodos GET/POST/PUT/DELETE manualmente e por fim usando o pytest de forma automática. 

## Layout web
![Web 3](https://github.com/GuilhermeGTM/DjangoRest/blob/main/demo/3.png)
![Web 1](https://github.com/GuilhermeGTM/DjangoRest/blob/main/demo/1.png)
![Web 2](https://github.com/GuilhermeGTM/DjangoRest/blob/main/demo/2.png)
![Web 4](https://github.com/GuilhermeGTM/DjangoRest/blob/main/demo/4.png)
![Web 5](https://github.com/GuilhermeGTM/DjangoRest/blob/main/demo/5.png)
![Web 6](https://github.com/GuilhermeGTM/DjangoRest/blob/main/demo/6.png)

# Tecnologias utilizadas

## Back end
- Python-3.12.3

## Front end

## Framework
- Django==4.2.18

## DB
- SQLite3

## Implantação em produção

# Como executar o projeto

```bash
instalar o venv na pasta do projeto
--->python -m venv .venv
ativando venv
--->.\.venv\Scripts\Activate
baixando as dependencias
--->python -m pip install -r requirements.txt
--->python manage.py migrate
criar um superuser
--->python manage.py createsuperuser
executando o projeto
-->python manage.py runserver
```

# Autor

Guilherme Timm Moreira

