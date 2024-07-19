# todo/views.py

from argparse import Action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing, creating, retrieving, updating, and deleting todos.
    """
    
    def list(self, request):
        """
        List all todos or filter by user ID if provided.

        GET /todos/
        """
        uid = request.query_params.get('user_id')
        if uid:
            queryset = Todo.objects.filter(user_id=uid)
        else:
            queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new todo.

        POST /todos/
        """
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific todo by ID.

        GET /todos/{id}/
        """
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a specific todo by ID.

        PUT /todos/{id}/
        """
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        Partially update a specific todo by ID.

        PATCH /todos/{id}/
        """
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a specific todo by ID.

        DELETE /todos/{id}/
        """
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # @api_view(['DELETE'])
    # def clear_db(self, request):
    #     """
    #     Delete all todos.

    #     DELETE /todos/clear_db/
    #     """
    #     deleted_count, _ = Todo.objects.all().delete()
    #     return Response({'message': f'{deleted_count} todos deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
