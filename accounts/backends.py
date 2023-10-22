from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.http.request import HttpRequest
from .models import User


# class EmailOrUsernameBackend(ModelBackend):
#     def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any):
#         # return super().authenticate(request, username, password, **kwargs)
#         try:
#             User.objects.get(username=username)
#             try:
#                 pass
#             except:
#                 pass
#         except User.DoesNotExist:
#             try:
#                 User.objects.get(email=username)
#             except User.DoesNotExist:
#                 return None
        
