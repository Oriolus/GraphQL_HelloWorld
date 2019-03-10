from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from data import Base
from data.model import Department


class Azs(Base):
    __tablename__ = 'azs'

    id = Column(Integer, primary_key=True)
    address = Column(String(length=1024))
    number = Column(String(length=512))
    lat = Column(Float)
    lon = Column(Float)
    departmentId = Column(Integer, ForeignKey('department.id'))

    department = relationship(
        Department
    )

