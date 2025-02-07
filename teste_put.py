import requests

headers = {'Authorization': 'Token df78b54eba033093abd86949eab2a63df7dc8209'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "Testando o PUT2",
    "url": "https://www.testandoput.com.br/put2"
}

"""
buscando o curso
"""
# curso = requests.get(url=f'{url_base_cursos}8/', headers=headers)
# print(curso.json())


resultado = requests.put(url=f'{url_base_cursos}8/', headers=headers,
                         data=curso_atualizado)


"""
Testando o código de status HTTP
"""
assert resultado.status_code == 200


"""
Testando o titulo
"""
assert resultado.json()['titulo'] == curso_atualizado['titulo']
