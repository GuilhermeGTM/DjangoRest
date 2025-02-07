from rest_framework import permissions

"""
verefica quando o metodo for 'DELETE' se o usuario é superuser ele pode deletar caso contario
ele não pode retorna false para outra ação retorna true
"""


class EhSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True
