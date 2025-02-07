from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            # write_only só na hora do cadastro apresentar o email
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

    # validando para que avaliação não passe do valor 5
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError(
            'Avaliação precisa ser um inteiro entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    """
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field

    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail'
    )
    """
    # Primary key Related Field, mostra o id de todas avaliações
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    # calcula a média das avaliações, maneira correta é criar um model com media
    # esse metodo faz um calculo cada vez que a pagina é atualizada
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2
