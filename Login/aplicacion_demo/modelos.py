from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

tarjeta_persona = Table('association', Base.metadata,
                          Column('tarjeta_id', Integer, ForeignKey('tarjeta.id')),
                          Column('persona_id', Integer, ForeignKey('persona.id'))
                          )

tarjeta_venta = Table('association2', Base.metadata,
                          Column('tarjeta_id', Integer, ForeignKey('tarjeta.id')),
                          Column('venta_id', Integer, ForeignKey('venta.id'))
                          )

persona_venta = Table('association3', Base.metadata,
                          Column('persona_id', Integer, ForeignKey('persona.id')),
                          Column('venta_id', Integer, ForeignKey('venta.id'))
                          )

class TarjetaPersona(db.Model):
    __tablename__ = 'tarjetapersona'
    tarjeta_id = Column(Integer, ForeignKey('tarjeta.id'), primary_key=True)
    persona_id = Column(Integer, ForeignKey('persona.id'), primary_key=True)

class VentasTarjeta(db.Model):
    __tablename__ = 'ventastarjeta'
    tarjeta_id = Column(Integer, ForeignKey('tarjeta.id'), primary_key=True)
    ventas_id = Column(Integer, ForeignKey('ventas.id'), primary_key=True)

class VentasPersona(db.Model):
    __tablename__ = 'ventaspersona'
    ventas_id = Column(Integer, ForeignKey('ventas.id'), primary_key=True)
    persona_id = Column(Integer, ForeignKey('persona.id'), primary_key=True)

#########################
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
    mes = db.Column(db.String(10),
                         index=False,
                         unique=False,
                         nullable=False)
    año = db.Column(db.String(10),
                         index=False,
                         unique=False,
                         nullable=False)
    montomax = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    
    personas = relationship("Persona", secondary='tarjetapersona')
    ventas2 = relationship("Venta", secondary='ventastarjeta')

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
        return '<Tarjeta {}, {}, {}, {}, {}, {}>'.format(self.tipo, self.numero, self.cods, self.mes, self.año, self.montomax)

class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer,
                   primary_key=True)
    nombre = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    apellido = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    tarjetas = relationship("Tarjeta", secondary='tarjetapersona')
    ventas = relationship("Venta", secondary='ventaspersona')

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
        personas = Persona.query.all()
        return personas

    def __repr__(self):
        return '<Persona {}, {}, {}>'.format(self.apellido, self.nombre)


class Venta(db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer,
                   primary_key=True)
    monto = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)

    personas2 = relationship("Persona", secondary='ventaspersona')
    tarjetas2 = relationship("Tarjeta", secondary='ventastarjeta')

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
        venta = Venta.query.all()
        return venta

    def __repr__(self):
        return '<Venta : {}>'.format(self.monto)
