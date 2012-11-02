# Create your views here.
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer2, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    """List all snippets or create a new one"""
    model = Snippet
    serializer_class = SnippetSerializer2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, udpate or delete a snippet instance."""
    model = Snippet
    serializer_class = SnippetSerializer2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer


class UserInstance(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
