from __future__ import annotations
from abc import ABC, abstractmethod


class DbIface(ABC):



    @abstractmethod
    def dbConnect(self):
        pass

    @abstractmethod
    def dbInsert(self, list):
        pass

    @abstractmethod
    def generateQuery(self, list):
        pass