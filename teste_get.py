import requests

headers = {'Authorization': 'Token df78b54eba033093abd86949eab2a63df7dc8209'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())


"""
Testando se o endpoint está correto
"""
assert resultado.status_code == 200
# print(resultado.status_code)


"""
Testando a quantidade de registros
"""
assert resultado.json()['count'] == 4


"""
Testando se o titulo do primeiro curso está correto
"""
assert resultado.json()['results'][0]['titulo'] == 'Criação de APIs Rest com Django REST Framework'
