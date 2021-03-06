import sys
from abc import ABC, abstractmethod

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from infra.RamDAOFactory import RamDAOFactory
from infra.XmlDAOFactory import XmlDAOFactory
from infra.Singleton import Singleton


class DAOFactory(ABC):
    # Lista de tipos DAO os quais a fábrica
    # oferece suporte:
    RAM = "RAM"
    XML = "XML"

    # Cada fábrica de todos os tipos erá de oferecer um retorno
    # para cada DAO possível de ser criado:
    @abstractmethod
    def getProfissionalDAO(self):
        pass

    @abstractmethod
    def getServicoDAO(self):
        pass

    def getDAOFactory(self, factory_type: str):

        factory_type = Singleton(factory_type)

        if factory_type.nome == self.RAM:
            return RamDAOFactory
        elif factory_type.nome == self.XML:
            return XmlDAOFactory
        else:
            return None
