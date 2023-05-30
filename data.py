#!/usr/bin/env python
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import (PrimaryKeyConstraint,Column,Index,DateTime,Integer, String, UniqueConstraint)
from sqlalchemy.orm import sessionmaker,declarative_base

Base = declarative_base()

class Automotive(Base):
    __tablename__='automotives'

    # specify any unique or expected data before we save
    __table_args__=(
        PrimaryKeyConstraint(
            'id',
            name = 'id=pk'
        ),
        UniqueConstraint(
            'chasis',
            name= 'unique_chasis'
        )
    )
    # (indexes)enables swift lookup using the specified column
    Index('index_name','name')

    # table colums
    id = Column(Integer())
    name= Column(String())
    chasis = Column(String(6))
    year = Column(DateTime(),default=datetime.now())
    
    # function that determines our output 

    def __repr__(self):
        return f"the car made on {self.year}:"\
                +f"is {self.name},"\
                +f"with chasis number {self.chasis}"


if __name__ == '__main__':
    engine = create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session= Session()

    # read function
    # car = session.query(Car).all()
    # print(car)

    # delete function
    # car = session.query(Car).filter(Car.name.like('%audi%'),Car.chasis=='A7O05').first()
    # session.delete(car)
    # session.commit()

    # create function
    # carB = Car(
    #     name='jeep',
    #     chasis='A7O04'
    # )

    # carC = Car(
    #     name='audi',
    #     chasis='A7O05'
    # )
    # carD = Car(
    #     name='audi',
    #     chasis='A7O06'
    # )
    # session.bulk_save_objects([carB,carC,carD])
    # session.commit()


    # update function
    # session.query(Car).update({Car.name:'jeep'})
    # session.commit()