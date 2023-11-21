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


class Accidents(Base):
    __tablename__ = "Accidents0514"
    Accident_Index = Column(String(15), primary_key=True, index=True)
    Accident_Severity = Column(Integer)
    Number_of_Vehicles = Column(Integer)
    Number_of_Casualties = Column(Integer)
    Date = Column(String(10))
    Day_of_Week = Column(Integer)
    Time = Column(String(5))
    Local_Authority_District = Column(Integer)
    Road_type = Column(Integer)
    Speed_limit = Column(Integer)
    Junction_Detail = Column(Integer)
    Junction_Control = Column(Integer)
    Pedestrian_Crossing_Human_Control = Column(Integer)
    Pedestrian_Crossing_Physical_Facilities = Column(Integer)
    Light_Conditions = Column(Integer)
    Weather_Conditions = Column(Integer)
    Road_Surface_Conditions = Column(Integer)
    Special_Conditions_at_Site = Column(Integer)
    Carriageway_Hazards = Column(Integer)
    Urban_or_Rural_Area = Column(Integer)
    Did_Police_Officer_Attend_Scene_of_Accident = Column(Integer)


class Vehicles(Base):
    __tablename__ = "Vehicles0514"
    Accident_Index = Column(String(15), primary_key=True, index=True)
    Vehicle_Reference = Column(Integer)
    Vehicle_Type = Column(Integer)
    Towing_and_Articulation = Column(Integer)
    Vehicle_Manoeuvre = Column(Integer)
    Vehicle_Location_Restricted_Lane = Column(Integer)
    Junction_Location = Column(Integer)
    Skidding_and_Overturning = Column(Integer)
    Hit_Object_in_Carriageway = Column(Integer)
    Vehicle_Leaving_Carriageway = Column(Integer)
    Hit_Object_off_Carriageway = Column(Integer)
    First_Point_of_Impact = Column(Integer)
    Left_Hand_Drive = Column(Integer)
    Journey_Purpose_of_Driver = Column(Integer)
    Sex_of_Driver = Column(Integer)
    Age_of_Driver = Column(Integer)
    Age_Band_of_Driver = Column(Integer)
    Engine_Capacity_CC = Column(Integer)
    Propulsion_Code = Column(Integer)
    Age_of_Vehicle = Column(Integer)
    Driver_IMD_Decile = Column(Integer)
    Driver_Home_Area_Type = Column(Integer)


class Accident_Serverity(Base):
    __tablename__ = "Accident_Severity"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Day_of_Week(Base):
    __tablename__ = "Day_of_Week"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Road_Type(Base):
    __tablename__ = "Road_Type"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Light_Conditions(Base):
    __tablename__ = "Light_Conditions"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Weather(Base):
    __tablename__ = "Weather"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Road_Surface(Base):
    __tablename__ = "Road_Surface"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Urban_Rural(Base):
    __tablename__ = "Urban_Rural"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Vehicle_Type(Base):
    __tablename__ = "Vehicle_Type"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Left_Hand(Base):
    __tablename__ = "Left_Hand"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Journey_Purpose(Base):
    __tablename__ = "Journey_Purpose"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Sex_Driver(Base):
    __tablename__ = "Sex_Driver"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Age_Band_Driver(Base):
    __tablename__ = "Age_Band_Driver"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class Casualty_Class(Base):
    __tablename__ = "Casualty_Class"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))


class IMD_Decile(Base):
    __tablename__ = "IMD_Decile"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    label = Column(String(50))
