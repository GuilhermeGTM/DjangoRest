import requests


# GET Avaliacoes

#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de  status HTTP
#print(avaliacoes.status_code)

# Acessando os dados da resposta
#print(avaliacoes.json())
#print(type(avaliacoes.json()))

# Acessando a quantidade de registros
#print(avaliacoes.json()['count'])

# Acessando a proxima  pagina de resultados
#print(avaliacoes.json()['next'])

# Acessando os resultados  desta pagina
#print(avaliacoes.json()['results'])
#print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
#print(avaliacoes.json()['results'][0])

# Acessando o ultimo elemento da lista de resultados
#print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa da avaliação
#print(avaliacoes.json()['results'][1]['nome'])


# GET Avaliacao
#avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')

#print(avaliacao.json())


# GET Cursos

headers = {'Authorization': 'Token df78b54eba033093abd86949eab2a63df7dc8209'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)

print(cursos.json())
