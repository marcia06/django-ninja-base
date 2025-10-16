from abc import ABC

from ..mixins.repository_mixins import (
    CreateRepositoryMixin,
    DeleteRepositoryMixin,
    ListRepositoryMixin,
    PartialUpdateRepositoryMixin,
    RetrieveRepositoryMixin,
    UpdateRepositoryMixin,
)
from ..models.models import BaseModel


class BaseModelRepository(
    ABC,
    RetrieveRepositoryMixin,
    ListRepositoryMixin,
    CreateRepositoryMixin,
    UpdateRepositoryMixin,
    PartialUpdateRepositoryMixin,
    DeleteRepositoryMixin,
):
    def __init__(self):
        self.model: BaseModel | None = None
