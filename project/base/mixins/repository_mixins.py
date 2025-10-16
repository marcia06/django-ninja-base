from typing import Any

from utils.exceptions import ContentDoesNotExist

from django.shortcuts import get_object_or_404
from django.utils import timezone


class RetrieveRepositoryMixin:
    def get_object(self, pk: Any) -> Any:
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise ContentDoesNotExist


class ListRepositoryMixin:
    def get_queryset(self, kwargs: dict = {}) -> Any:
        return self.model.objects.filter(**kwargs)


class CreateRepositoryMixin:
    def create(self, data: dict) -> Any:
        return self.model.objects.create(**data)


class UpdateRepositoryMixin:
    def update(self, pk: Any, data: dict) -> Any:
        instance = get_object_or_404(self.model, pk=pk)

        for attr, value in data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


class PartialUpdateRepositoryMixin:
    def partial_update(self, pk: Any, data: dict) -> Any:
        instance = get_object_or_404(self.model, pk=pk)

        for attr, value in data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


class DeleteRepositoryMixin:
    def delete(self, pk: Any) -> None:
        instance = get_object_or_404(self.model, pk=pk)

        instance.deleted_at = timezone.now()
        instance.save()

        return {}
