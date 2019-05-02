class Orcamento:
    # CONSTRUTOR:
    def __init__(self, id, nome: str, profissional, orcamento, idServico):
        self.id = id
        self.nome = nome
        self.profissional = profissional
        self.orcamento = orcamento
        self.idServico = idServico

    # Override do equals para fazer com que a comparação ==
    # entre dois objetos do tipo Profissional retorne True
    # caso os dois objetos possuam os mesmos atributos
    # que sejam únicos no sistema:
    def __eq__(self, other):
        return self.id == other.id

    # MÈTODOS GET:
    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_profissional(self):
        return self.profissional

    def get_orcamento(self):
        return self.orcamento

    def get_idServico(self):
        return self.id

    # MÈTODOS SET:
    def set_nome(self, nome):
        self.nome = nome

    def set_orcamento(self, orcamento):
        self.orcamento = orcamento
 