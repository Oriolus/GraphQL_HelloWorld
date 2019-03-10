from sqlalchemy import Column, String, Integer
from data import Base


class Kkt(Base):
    __tablename__ = 'kkt'
    id = Column(Integer, primary_key=True)
    inn = Column(String(length=128))
    kktRegId = Column(String(length=128))
    driveFistNumber = Column(String(length=128))
    loadingCode = Column(Integer)

