

from abc import ABC,abstractmethod


class AbstractClass(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def greet_diff_lang(self):
        raise NotImplementedError("Subclasses should implement this!")