from rest_framework import permissions


class BaseAuthPermApi(permissions.BasePermission):
    def has_permission(self, request, view):
        for grupo in request.user.groups.all():
            if grupo.name in self._PERMISSIONS:
                return True
        return False


class IsAdmin(BaseAuthPermApi):
    _PERMISSIONS = ["Administradores"]


class IsClient(BaseAuthPermApi):
    _PERMISSIONS = ["Clientes"]
