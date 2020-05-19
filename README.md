### DESCRIÇÃO

Aplicação web desenvolvida para registro e o gerenciamento dos proprietários de veículos e seus veículos.


### REQUISITOS

Para o funcionamento correto desta aplicação em Django, são necessárias algumas configurações da máquina:

- Instalar o Docker
- Instalar o Docker Compose
    

#### INSTALAÇÃO E CONFIGURAÇÃO LINUX
1 - criar um diretório onde o sistema será alocado;<br />
2 - clonar o repositório https://github.com/HeltonPenariol/vehicle_management dentro da pasta criada;
3 - abrir um terminal e ir até a pasta onde foi clonado o projeto
4 - rodar o seguinte comando: docker-compose up --build -d<br />
5 - criar um usuário admistrador;para isso, no mesmo terminal ja aberto, rodar o seguinte comando docker-compose run web python manage.py createsuperuser e preencher o formulario que irá aparecer;<br />
6 - sistema já está pronto para uso.<br />

  
#### OPERAÇÕES DISPONÍVEIS

_Gestão de proprietários_
1 - Autenticação (via token, esse token tem duração de 2 horas, após esse prazo, necessário nova autenticação)<br />
2 - Lista todos os proprietários cadastrados<br />
3 - Criação de novos proprietários<br />
4 - Consulta de prprietário pelo documento<br />
5 - Consulta de propritário pela matricula (gerada automaticamente quando proprietário é cadastrado)<br />

_Gestão de vepiculos_
6 - Listagem de modelos de veículos cadastrados<br />
7 - Listagem de marcas de veículos cadastradas<br />
8 - Listagem de tipos de veículos cadastrados<br />
9 - Listagem de veículos cadastrados (apresenta apenas os veículos cadastrados que o usuário autenticado criou)<br />
10 - Consulta de veículo por placa (apresenta apenas os veículos cadastrados que o usuário autenticado criou)<br />
11 - Consulta de veículo por chassis (apresenta apenas os veículos cadastrados que o usuário autenticado criou)<br />
12 - Consulta de veículo por documento do proprietário (apresenta apenas os veículos cadastrados que o usuário autenticado criou)<br />
13 - Cadastro de novo veículo<br />


#### ROTAS
**1 - Autenticação**<br />
Rota: auth/

Tipo de chamada: POST

Exemplo de chamada:<br />
{<br />
    "username": "username", ---> nome do usuário do sitema<br />
    "password": "password"  ---> senha do usuário<br />
}

Retorno:<br />
{<br />
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImpvYW8iLCJleHAiOjE1NzQzNDI4ODYsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE1NzQzMzU2ODZ9.c9ouoiOfCtiSLAYpIK0fj8y6O2dpfBaYyeiz-CDhMK8"<br />
}<br />
PS.: este token (autorização) é necessáio para utilização das demais funções!

**2 - lista de todos proprietários cadastrados**<br />
Rota:  proprietario/

Tipo de chamada: GET

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o token gerado na autenticação.

Retorno:<br />
[<br />
    {<br />
        "name": "Helton",<br />
        "doc_number": "132456789",<br />
        "user": 1,<br />
        "registration": "PROP105d"<br />
    }<br />
]

**3 - Criação de novos proprietários:**<br />
Rota: criar/proprietario/

Tipo de chamada: POST

Exemplo de chamada:<br />
{
	"name": "Pedro",  ---# Nome do proprietário<br />
	"doc_number": "321654987" ---# Numero do documento do proprietário<br />
}

Retorno:<br />
{<br />
    "status_code": 200,<br />
    "message": "Successfully created",<br />
    "result": {<br />
        "name": "Talita",<br />
        "doc_number": "321654987",<br />
        "user": 1<br />
    }<br />
}
**4 - Consulta de proprietário pelo documento:**<br />
Rota: doc/proprietario/#numero do documento#<br />
Substituir #numero do documento# pelo documento que deseja consultar.

Tipo de chamada: GET

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o numero de documento na URL.<br />

Retorno:<br />
[<br />
    {<br />
        "name": "Talita",<br />
        "doc_number": "321654987",<br />
        "user": 1,<br />
        "registration": "PROP205d"<br />
    }<br />
]

**5 - Consulta de propritário pela matricula**<br />
Rota:  mat/proprietario/#numero da matricula#<br />
Substituir #numero da matricula# pela matricula que deseja consultar.

Tipo de chamada: GET

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o numero da matricula na URL.

Retorno:<br />
[<br />
    {<br />
        "name": "Helton",<br />
        "doc_number": "132456789",<br />
        "user": 1,<br />
        "registration": "PROP105d"<br />
    }<br />
]


**6 - Listagem de modelos de veículos cadastrados**<br />
Rota: modelos/<br />

Tipo de chamada: GET

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o token gerado na autenticação.

Retorno:<br />
[<br />
    {<br />
        "id": 2,<br />
        "name": "Civic",<br />
        "slug": "civic"<br />
    },<br />
    {<br />
        "id": 3,<br />
        "name": "Fox",<br />
        "slug": "fox"<br />
    },<br />
    {<br />
        "id": 1,<br />
        "name": "Tempra",<br />
        "slug": "tempra"<br />
    }<br />
]

**7 - Listagem de marcas de veículos cadastrados**<br />
Rota: marcas/

Tipo de chamada: GET

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o token gerado na autenticação.

Retorno:<br />
[<br />
    {<br />
        "id": 1,<br />
        "name": "Honda",<br />
        "slug": "honda"<br />
    },<br />
    {<br />
        "id": 3,<br />
        "name": "Volkswagem",<br />
        "slug": "volkswagem"<br />
    },<br />
    {<br />
        "id": 2,<br />
        "name": "Fiat",<br />
        "slug": "fiat"<br />
    }<br />
]

8 - Listagem de tipos de veículos cadastrados**<br />
Rota: tipos/

Tipo de chamada: GET

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o token gerado na autenticação.

Retorno:<br />
[
    {
        "id": 1,<br />
        "name": "Carro",<br />
        "slug": "carro"<br />
    },<br />
    {<br />
        "id": 2,<br />
        "name": "Moto",<br />
        "slug": "moto"<br />
    }<br />
]

**9 - Listagem de veículos cadastrados (necessário haver veículo cadastrado)**<br />
Rota: veiculos/

Tipo de chamada: GET

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o token gerado na autenticação.<br />

Retorno:<br />
[<br />
    {<br />
        "id": 1,<br />
        "slug": "abc1234",<br />
        "model_year": "2017",<br />
        "fabric_year": "2018",<br />
        "vehicle_plate": "abc1234",<br />
        "vehicle_chassis": "adf123654ghj",<br />
        "date_created": "2019-11-21T08:54:43.811356-03:00",<br />
        "owner": 2,<br />
        "user": 1,<br />
        "brand": 1,<br />
        "model": 2,<br />
        "type": 1<br />
    }<br />
]

**10 - Consulta de veículo por placa (necessário haver veículo cadastrado)**<br />
Rota: placa/veiculos/#placa#<br />
Substituir #placa# pela placa do veículo que deseja consultar.

Tipo de chamada: GET

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o numero da placa do veículo na URL.

Retorno:<br />
[<br />
    {<br />
        "id": 1,<br />
        "slug": "abc1234",<br />
        "model_year": "2017",<br />
        "fabric_year": "2018",<br />
        "vehicle_plate": "abc1234",<br />
        "vehicle_chassis": "adf123654ghj",<br />
        "date_created": "2019-11-21T08:54:43.811356-03:00",<br />
        "owner": 2,<br />
        "user": 1,<br />
        "brand": 1,<br />
        "model": 2,<br />
        "type": 1<br />
    }<br />
]

**11 - Consulta de veículo pelo chassis (necessário haver veículo cadastrado)**<br />
Rota: chass/veiculos/#chassis#<br />
Substituir #chassis# pelo chassis do veículo que deseja consultar.<br />

Tipo de chamada: GET

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o numero do chassis do veículo na URL.<br />

Retorno:<br />
[<br />
    {<br />
        "id": 1,<br />
        "slug": "abc1234",<br />
        "model_year": "2017",<br />
        "fabric_year": "2018",<br />
        "vehicle_plate": "abc1234",<br />
        "vehicle_chassis": "adf123654ghj",<br />
        "date_created": "2019-11-21T08:54:43.811356-03:00",<br />
        "owner": 2,<br />
        "user": 1,<br />
        "brand": 1,<br />
        "model": 2,<br />
        "type": 1<br />
    }<br />
]

**12 - Consulta de veículo pelo documento do proprietário (necessário haver veículo cadastrado)**<br />
Rota: doc/veiculos/#doc#<br />
Substituir #doc# pelo numero do documento do proprietário do veículo que deseja consultar.

Tipo de chamada: GET<br />

Exemplo de chamada:<br />
Sem argumentos, apenas necessário inserir o numero do documento do proprietário do veículo na URL.

Retorno:<br />
[<br />
    {<br />
        "id": 1,<br />
        "slug": "abc1234",<br />
        "model_year": "2017",<br />
        "fabric_year": "2018",<br />
        "vehicle_plate": "abc1234",<br />
        "vehicle_chassis": "adf123654ghj",<br />
        "date_created": "2019-11-21T08:54:43.811356-03:00",<br />
        "owner": 2,<br />
        "user": 1,<br />
        "brand": 1,<br />
        "model": 2,<br />
        "type": 1<br />
    }<br />
]

**13 - Cadastro de novo veículo**<br />
Rota: criar/veiculos/<br />

Tipo de chamada: POST

Exemplo de chamada:<br />
{<br />
	"owner": "Helton",  ---> deve ser um proprietário já cadastrado, e o nome deve ser igual ao cadastro<br />
	"brand": "Fiat",  ---> deve ser uma marca já cadastrada, e o nome deve ser igual ao cadastro<br />
	"model": "Tempra",  ---> deve ser um modelo já cadastrado, e o nome deve ser igual ao cadastro<br />
	"type": "Carro",  ---> deve ser um tipo já cadastrado, e o nome deve ser igual ao cadastro<br />
	"model_year": "1997",<br />
	"fabric_year": "1997",<br />
	"vehicle_plate": "abc123",<br />
	"vehicle_chassis": "12312fd1321"<br />
}

Retorno:<br />
{<br />
    "status_code": 200,<br />
    "message": "Successfully created",<br />
    "result": {<br />
        "owner": 1,<br />
        "brand": 3,<br />
        "model": 1,<br />
        "type": 1,<br />
        "model_year": "1997",<br />
        "fabric_year": "1997",<br />
        "vehicle_plate": "abc123",<br />
        "vehicle_chassis": "12312fd1321",<br />
        "user": 1<br />
    }<br />
}


#### OBSERVAÇÕES
1- ao iniciar o sistema pela primeira vez, é criado apenas o usuário administrador, para cadastro de novos usuários, 
 necessário acessar o sistema pela interface (url/admin).
 
2 - Para cadastro de Marcas, Modelos e Tipos, é necessário ser feito pela interface (url/admin)
 
3 - Para cadastro de novos veículos, ideal é consultar via api de modelo, tipo e marca para pegar as informações corretas. <br />
    Para propritário (owner) utilzar o campo name, para tipo, modelo e marca utilizar o campo slug.

4 - Estes endpoints podem ser consumidos por aplicações ou interface (front end) customizados.    
