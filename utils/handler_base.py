from abc import ABC, abstractmethod


class BaseHandler(ABC):
    @abstractmethod
    def login_click(self) -> None:
        pass

    @abstractmethod
    def register_click(self) -> None:
        pass