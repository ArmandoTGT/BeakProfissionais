import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from infra.DAOFactory import DAOFactory
from infra.RamProfissionalDAO import RamProfissionalDAO
from infra.RamServicoDAO import RamServicoDAO
from infra.RamOrcamentoDAO import RamOrcamentoDAO

class RamDAOFactory(DAOFactory):
    def getProfissionalDAO(self) -> RamProfissionalDAO:
        return RamProfissionalDAO()

    def getServicoDAO(self) -> RamServicoDAO:
        return RamServicoDAO()

    def getOrcamentoDAO(self) -> RamOrcamentoDAO:
        return RamOrcamentoDAO()