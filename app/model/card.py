from ..services.db import db


class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    tipo_de_pessoa = db.Column(db.String(50), nullable=False)
    nome_raz_o_social = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(14), nullable=True)
    estado_civil = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    e_mail = db.Column(db.String(100), nullable=False)
    valor_total_da_compra = db.Column(db.String(100), nullable=False)
    qual_tipo_de_im_vel = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    endere_o = db.Column(db.String(255), nullable=False)
    n_mero = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    qual_valor_do_im_vel = db.Column(db.String(100), nullable=False)
    qual_o_valor_do_empr_stimo = db.Column(db.String(100), nullable=False)
    prazo_pagamento = db.Column(db.String(50), nullable=False)
    indica_o = db.Column(db.String(100), nullable=True)
    assessor_respons_vel = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        return {
            "tipo_de_pessoa": self.tipo_de_pessoa,
            "nome_raz_o_social": self.nome_raz_o_social,
            "cpf": self.cpf,
            "estado_civil": self.estado_civil,
            "telefone": self.telefone,
            "e_mail": self.e_mail,
            "valor_total_da_compra": self.valor_total_da_compra,
            "qual_tipo_de_im_vel": self.qual_tipo_de_im_vel,
            "cep": self.cep,
            "endere_o": self.endere_o,
            "n_mero": self.n_mero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "qual_valor_do_im_vel": self.qual_valor_do_im_vel,
            "qual_o_valor_do_empr_stimo": self.qual_o_valor_do_empr_stimo,
            "prazo_pagamento": self.prazo_pagamento,
            "indica_o": self.indica_o,
            "assessor_respons_vel": self.assessor_respons_vel,
            "status": self.status,
        }
