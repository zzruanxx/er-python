from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship("Cliente", back_populates="pedidos")

Cliente.pedidos = relationship("Pedido", order_by=Pedido.id, back_populates="cliente")

# Criando a base de dados
engine = create_engine('sqlite:///meubanco.db')
Base.metadata.create_all(engine)
