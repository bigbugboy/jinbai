from django.utils.deprecation import MiddlewareMixin
from django.http.request import HttpRequest
from django.shortcuts import redirect


class SuperUserAdminMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        user = request.user
        if not user.is_authenticated or not user.is_superuser:
            return redirect(to='index')
