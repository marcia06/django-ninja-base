from abc import ABC

from ..repositories.repositories import BaseModelRepository


class BaseService(ABC):
    def __init__(self, repository: BaseModelRepository) -> None:
        self.repository = repository
