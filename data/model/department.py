from sqlalchemy import Column, Integer, String
from data import Base


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=256))

    def __repr__(self):
        return 'Id: {0}, title: {1}'.format(
            str(self.id),
            self.title
        )


