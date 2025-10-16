from typing import Any


class RetrieveServiceMixin:
    def retrieve(self, pk: Any) -> Any:
        return self.repository.get_object(pk=pk)


class ListServiceMixin:
    def list(self, kwargs: dict = {}) -> Any:
        return self.repository.get_queryset(**kwargs)


class CreateServiceMixin:
    def create(self, data: dict) -> Any:
        return self.repository.create(**data)


class UpdateServiceMixin:
    def update(self, pk: Any, data: dict) -> Any:
        return self.repository.update(pk=pk, data=data)


class PartialUpdateServiceMixin:
    def partial_update(self, pk: Any, data: dict) -> Any:
        return self.repository.partial_update(pk=pk, data=data)


class DestroyServiceMixin:
    def destroy(self, pk: Any) -> None:
        return self.repository.delete(pk=pk)
