class Email:
    def envioEmail(self, email, texto):
        #9 digitos zeros para RG
        #11 digitos zeros para CPF
        if (email == "gmail"):
            return True
        else:
            return False
            
    def recebimentoEmail(self):
        return "Email confirmado"