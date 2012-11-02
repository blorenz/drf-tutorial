# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer2
from rest_framework.views import APIView
from django.http import Http404


class SnippetList(APIView):
    """List all snippets or create a new one"""

    def get(self, request, format=None):
        """get the snippets"""
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer2(instance=snippets)
        return Response(serializer.data)

    def post(self, request, format=None):
        """post the snippets"""
        serializer = SnippetSerializer(request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """Retrieve, udpate or delete a snippet instance."""
    def get_object(self, pk):
        """get an object"""
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """get a detail snippet"""
        snippet = self.get_object(pk)
        serializer = SnippetSerializer2(instance=snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """put a new snippet"""
        snippet = self.get_object(pk)
        serializer = SnippetSerializer2(request.DATA, instance=snippet)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """delete one"""
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """List all code snippets, or create a new snippet."""
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer2(instance=snippets)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer2(request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """Retrieve, update, or delete a code snippet"""
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer2(instance=snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer2(request.DATA, instance=snippet)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

