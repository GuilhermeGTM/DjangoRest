# v1
from rest_framework import generics
from rest_framework.generics import get_object_or_404
# v2
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from.permissions import EhSuperUser

"""
API V1
"""


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""


"""
foi criado um arquivo permissions nonde nele tem uma classe EhSuperUser
com ela eu consigo configurar qual ação o usuario pode fazer,
nota-se que essa classe vem antes para ser lida antes da outra
"""


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
        )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # Decorator para pegar avaliações do cursos/1/avaliacoes
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        # paginação na rota cursos/1/avaliacoes
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""


# comentar qualquer mixins com # e desativar o metodo
class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
