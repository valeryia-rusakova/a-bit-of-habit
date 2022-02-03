from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def get_queryset(self, request, request_type):
        pass

    @abstractmethod
    def create(self, request):
        pass

    @abstractmethod
    def delete(self, request):
        pass

    @abstractmethod
    def update(self, request):
        pass
