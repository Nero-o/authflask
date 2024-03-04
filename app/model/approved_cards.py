from .. import db

class ApprovedCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_pessoa = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    cpf_cnpj = db.Column(db.String(255), nullable=False)
    estado_civil = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    renda_mensal = db.Column(db.Float, nullable=False)
    tipo_terreno = db.Column(db.String(255), nullable=False)
    cep = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(255), nullable=False)
    bairro = db.Column(db.String(255), nullable=False)
    cidade = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    valor_propriedade = db.Column(db.Float, nullable=False)
    valor_emprestimo = db.Column(db.Float, nullable=False)
    prazo_pagamento = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "tipo_pessoa": self.tipo_pessoa,
            "nome": self.nome,
            "cpf_cnpj": self.cpf_cnpj,
            "estado_civil": self.estado_civil,
            "telefone": self.telefone,
            "email": self.email,
            "renda_mensal": self.renda_mensal,
            "tipo_terreno": self.tipo_terreno,
            "cep": self.cep,
            "endereco": self.endereco,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "valor_propriedade": self.valor_propriedade,
            "valor_emprestimo": self.valor_emprestimo,
            "prazo_pagamento": self.prazo_pagamento,
            "status": self.status
        }