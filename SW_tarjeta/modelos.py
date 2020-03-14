from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Tarjeta(db.Model):
    __tablename__ = 'tarjeta'
    id = db.Column(db.Integer,
                   primary_key=True)
    tipo = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    numero = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    cods= db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        tarjetas = Tarjeta.query.all()
        return tarjetas

    def __repr__(self):
        return '<Tarjeta {}, {}, {}>'.format(self.tipo, self.numero, self.cods)
