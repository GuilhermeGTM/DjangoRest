import requests


class TestCursos:
    headers = {'Authorization': 'Token df78b54eba033093abd86949eab2a63df7dc8209'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}1/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "teste post pytest",
            "url": "https://www.testepostpytest.com.br/testpostpytest"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)
        """
        tem duas maneira de fazer os assert assim dessa maneira no mesmo metodo
        ou tu pode criar outro metodo para fazer o teste do titulo exemplo
        """
        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "testando put3 com pytest",
            "url": "https://www.testandopytestput.com.br/put"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}8/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}10/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
