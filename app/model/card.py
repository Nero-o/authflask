from ..services.db import db

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    tipo_de_pessoa = db.Column(db.String(50), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(14), nullable=True)
    cnpj = db.Column(db.String(17), nullable=True)
    estado_civil = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    e_mail = db.Column(db.String(100), nullable=False)
    qual_a_renda_mensal = db.Column(db.String(100), nullable=True)
    faturamento_mensal = db.Column(db.String(100), nullable=True)
    qual_tipo_de_im_vel = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    endere_o = db.Column(db.String(255), nullable=False)
    n_mero = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    qual_valor_do_im_vel = db.Column(db.String(100), nullable=False)
    qual_o_valor_do_empr_stimo = db.Column(db.String(100), nullable=False)
    prazo_para_pagamento = db.Column(db.String(50), nullable=False)
    indica_o = db.Column(db.String(100), nullable=True)
    assessor_respons_vel = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), nullable=True)
    statusFK= db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'tipo_de_pessoa': self.tipo_de_pessoa,
            'nome': self.nome,
            'cpf': self.cpf,
            'cnpj': self.cnpj,
            'estado_civil': self.estado_civil,
            'telefone': self.telefone,
            'e_mail': self.e_mail,
            'qual_a_renda_mensal': self.qual_a_renda_mensal,
            'faturamento_mensal': self.faturamento_mensal,
            'qual_tipo_de_im_vel': self.qual_tipo_de_im_vel,
            'cep': self.cep,
            'endere_o': self.endere_o,
            'n_mero': self.n_mero,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado,
            'qual_valor_do_im_vel': self.qual_valor_do_im_vel,
            'qual_o_valor_do_empr_stimo': self.qual_o_valor_do_empr_stimo,
            'prazo_para_pagamento': self.prazo_para_pagamento,
            'indica_o': self.indica_o,
            'assessor_respons_vel': self.assessor_respons_vel,
            'status': self.status,
            'statusFK': self.statusFK,

        }
