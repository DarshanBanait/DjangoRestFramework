from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticated
from todos.models import Todo
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from todos.pagination import CustomPageNumberPagination

class TodosAPIView(ListCreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'is_complete', 'title', 'desc']
    search_fields = ['id', 'title', 'desc', 'is_complete']
    ordering_fields = ['id', 'is_complete', 'title', 'desc', 'created_at', 'updated_at']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)