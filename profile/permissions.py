from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
   Доступ разрешен только владельцу объекта.
    """

    def has_object_permission(self, request, view, obj):
        # obj — это экземпляр Profile
        return obj.user == request.user