import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from infra.ProfissionalDAO import ProfissionalDAO
from business.model.Profissional import Profissional
from business.control.Exceptions.NotFoundException import NotFoundException


class RamProfissionalDAO(ProfissionalDAO):
    def __init__(self):
        self.profissional_list = []

    def insere_profissional(self, profissional: Profissional):
        self.profissional_list.append(profissional)

    def atualiza_profissional(self, profissional: Profissional):
        index = 0

        # Procura em cada elemento da lista:
        for profissional_list_element in self.profissional_list:
            # Caso encontre o Profisssional igual na lista:
            if profissional_list_element == profissional:
                # Remove a versão antiga
                self.profissional_list.pop(index)
                # e adiciona a nova instância do objeto?
                self.profissional_list.insert(index, profissional)

                return None

            # Incrementa o índice:
            index += 1

        # Caso passe pelo for retorna uma exceção
        # indicando que a operação Falhou
        raise NotFoundException("profissional")

    def remove_profissional(self, profissional_id: str):
        index = 0

        # Procura em cada elemento da lista:
        for profissional in self.profissional_list:
            # Caso encontre o Profisssional com o email fornecido
            if profissional.get_id() == profissional_id:
                # Deleta ele e retorna seu valor:
                return self.profissional_list.pop(index)
            # Incrementa o índice:
            index += 1

        # Caso passe pelo for, retorna uma exceção
        # indicando que a operação Falhou
        raise NotFoundException("profissional")

    def busca_profissional_id(self, profissional_id: str) -> Profissional:
        index = 0

        # Procura em cada elemento da lista:
        for profissional in self.profissional_list:
            # Caso encontre o Profisssional com o email fornecido
            if profissional.get_id() == profissional_id:
                # Retorna o objeto encontrado:
                return profissional
            # Incrementa o índice:
            index += 1

        # Caso passe pelo for retorna uma exceção
        # indicando que a operação Falhou
        raise NotFoundException("profissional")

    def busca_profissional_email(self, email: str) -> Profissional:
        index = 0

        # Procura em cada elemento da lista:
        for profissional in self.profissional_list:
            # Caso encontre o Profisssional com o email fornecido
            if profissional.get_email() == email:
                # Retorna o objeto encontrado:
                return profissional
            # Incrementa o índice:
            index += 1

        # Caso passe pelo for retorna uma exceção
        # indicando que a operação Falhou
        raise NotFoundException("profissional")