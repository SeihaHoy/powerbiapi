from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Casualties(Base):
    __tablename__ = "casualties0514"
    Accident_Index = Column(String(15), primary_key=True, index=True)
    Vehicle_Reference = Column(Integer)
    Casulty_Reference = Column(Integer)
    Casulty_Class = Column(Integer)
    Sex_of_Casulty = Column(Integer)
    Age_of_Casulty = Column(Integer)
    Age_Band_of_Casulty = Column(Integer)
    Casulty_Severity = Column(Integer)
    Pedestrian_Location = Column(Integer)
    Pedestrian_Movement = Column(Integer)
    Car_Passenger = Column(Integer)
    Bus_or_Coach_Passenger = Column(Integer)
    Pedestrian_Road_Maintenance_Worker = Column(Integer)
    Casulty_Type = Column(Integer)
    Casulty_Home_Area_Type = Column(Integer)




