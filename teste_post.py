import requests

headers = {'Authorization': 'Token df78b54eba033093abd86949eab2a63df7dc8209'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


novo_curso = {
    "titulo": "Testando post",
    "url": "https://testeandopost.com.br/post"
}

resultado = requests.post(url=url_base_cursos, headers=headers,
                          data=novo_curso)


"""
Testando o código de  status HTTP 201
"""
assert resultado.status_code == 201


"""
Testando se o titulo do curso retornado é o mesmo do informado
"""
assert resultado.json()['titulo'] == novo_curso['titulo']
