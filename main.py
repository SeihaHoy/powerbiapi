from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class AccidentSeverity(BaseModel):
    code: int
    label: str


class DayOfWeek(BaseModel):
    code: int
    label: str


class RoadType(BaseModel):
    code: int
    label: str


class LightConditions(BaseModel):
    code: int
    label: str


class WeatherBase(BaseModel):
    code: int
    label: str


class RoadSurface(BaseModel):
    code: int
    label: str


class UrbanRural(BaseModel):
    code: int
    label: str


class VehicleType(BaseModel):
    code: int
    label: str


class LeftHand(BaseModel):
    code: int
    label: str


class JourneyPurpose(BaseModel):
    code: int
    label: str


class SexDriver(BaseModel):
    code: int
    label: str


class AgeBand(BaseModel):
    code: int
    label: str


class CasualtyClass(BaseModel):
    code: int
    label: str


class IMDDecile(BaseModel):
    code: int
    label: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/acc_severity/", status_code=status.HTTP_201_CREATED)
async def create_severity(accident_severity: AccidentSeverity, db: db_dependency):
    db_severity = models.Accident_Serverity(**accident_severity.dict())
    db.add(db_severity)
    db.commit()


@app.post("/day_of_week/", status_code=status.HTTP_201_CREATED)
async def create_day(day: DayOfWeek, db: db_dependency):
    db_day = models.Day_of_Week(**day.dict())
    db.add(db_day)
    db.commit()


@app.post("/road_type/", status_code=status.HTTP_201_CREATED)
async def create_road(road: RoadType, db: db_dependency):
    db_road = models.Road_Type(**road.dict())
    db.add(db_road)
    db.commit()


@app.post("/light_con/", status_code=status.HTTP_201_CREATED)
async def create_light(light: LightConditions, db: db_dependency):
    db_light = models.Light_Conditions(**light.dict())
    db.add(db_light)
    db.commit()


@app.post("/weather/", status_code=status.HTTP_201_CREATED)
async def create_weather(weather: WeatherBase, db: db_dependency):
    db_weather = models.Weather(**weather.dict())
    db.add(db_weather)
    db.commit()


@app.post("/vehicle_type/", status_code=status.HTTP_201_CREATED)
async def create_vehicle(vehicle: VehicleType, db: db_dependency):
    db_vehicle = models.Vehicle_Type(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()


@app.post("/road_surface/", status_code=status.HTTP_201_CREATED)
async def create_road_surface(road_surface: RoadSurface, db: db_dependency):
    db_road_surface = models.Road_Surface(**road_surface.dict())
    db.add(db_road_surface)
    db.commit()


@app.post("/urban_rural/", status_code=status.HTTP_201_CREATED)
async def create_urban_rural(urban_rural: UrbanRural, db: db_dependency):
    db_urban_rural = models.Urban_Rural(**urban_rural.dict())
    db.add(db_urban_rural)
    db.commit()


@app.post("/left_hand/", status_code=status.HTTP_201_CREATED)
async def create_left_hand(left_hand: LeftHand, db: db_dependency):
    db_left_hand = models.Left_Hand(**left_hand.dict())
    db.add(db_left_hand)
    db.commit()


@app.post("/journey_purpose/", status_code=status.HTTP_201_CREATED)
async def create_journey_purpose(journey_purpose: JourneyPurpose, db: db_dependency):
    db_journey_purpose = models.Journey_Purpose(**journey_purpose.dict())
    db.add(db_journey_purpose)
    db.commit()


@app.post("/sex_driver/", status_code=status.HTTP_201_CREATED)
async def create_sex_driver(sex_driver: SexDriver, db: db_dependency):
    db_sex_driver = models.Sex_Driver(**sex_driver.dict())
    db.add(db_sex_driver)
    db.commit()


@app.post("/age_band/", status_code=status.HTTP_201_CREATED)
async def create_age_band(age_band: AgeBand, db: db_dependency):
    db_age_band = models.Age_Band_Driver(**age_band.dict())
    db.add(db_age_band)
    db.commit()


@app.post("/casualty_class/", status_code=status.HTTP_201_CREATED)
async def create_casualty_class(casualty_class: CasualtyClass, db: db_dependency):
    db_casualty_class = models.Casualty_Class(**casualty_class.dict())
    db.add(db_casualty_class)
    db.commit()


@app.post("/imd_decile/", status_code=status.HTTP_201_CREATED)
async def create_imd_decile(imd_decile: IMDDecile, db: db_dependency):
    db_imd_decile = models.IMD_Decile(**imd_decile.dict())
    db.add(db_imd_decile)
    db.commit()


@app.get("/casualty/{casualty_id}", status_code=status.HTTP_200_OK)
async def get_casualty(casualty_id: str, db: db_dependency):
    db_casualty = (
        db.query(models.Casualties)
        .filter(models.Casualties.Accident_Index == casualty_id)
        .first()
    )
    if db_casualty is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Casualty not found"
        )
    return db_casualty


@app.get("/accident/{accident_id}", status_code=status.HTTP_200_OK)
async def get_accident(accident_id: str, db: db_dependency):
    db_accident = (
        db.query(models.Accidents)
        .filter(models.Accidents.Accident_Index == accident_id)
        .first()
    )
    if db_accident is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="accident not found"
        )
    return db_accident


@app.get("/vehicle/{vehicle_id}", status_code=status.HTTP_200_OK)
async def get_vehicle(vehicle_id: str, db: db_dependency):
    db_vehicle = (
        db.query(models.Vehicles)
        .filter(models.Vehicles.Accident_Index == vehicle_id)
        .first()
    )
    if db_vehicle is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle not found"
        )
    return db_vehicle


# @app.get("/casualties", status_code=status.HTTP_200_OK)
# async def get_all_casualties(db: db_dependency):
#     db_casulties = db.query(models.Casualties).all()
#     return db_casulties


@app.get("/casualties", status_code=status.HTTP_200_OK)
async def get_all_casualties(db: db_dependency, skip: int = 0, limit: int = 100):
    db_casulties = db.query(models.Casualties).offset(skip).limit(limit).all()
    if db_casulties is None:
        raise HTTPException(status_code=404, detail="Casualties not found")
    return db_casulties


@app.get("/accidents", status_code=status.HTTP_200_OK)
async def get_all_accidents(db: db_dependency, skip: int = 0, limit: int = 100):
    db_accidents = db.query(models.Accidents).offset(skip).limit(limit).all()
    if db_accidents is None:
        raise HTTPException(status_code=404, detail="Accidents not found")
    return db_accidents


@app.get("/vehicles", status_code=status.HTTP_200_OK)
async def get_all_vehicles(db: db_dependency, skip: int = 0, limit: int = 100):
    db_vehicles = db.query(models.Vehicles).offset(skip).limit(limit).all()
    if db_vehicles is None:
        raise HTTPException(status_code=404, detail="Vehicles not found")
    return db_vehicles


@app.get("/acc_severity", status_code=status.HTTP_200_OK)
async def get_all_severity(db: db_dependency):
    db_severity = db.query(models.Accident_Serverity).all()
    if db_severity is None:
        raise HTTPException(status_code=404, detail="Severity not found")
    return db_severity


@app.get("/days", status_code=status.HTTP_200_OK)
async def get_all_days(db: db_dependency):
    db_days = db.query(models.Day_of_Week).all()
    if db_days is None:
        raise HTTPException(status_code=404, detail="days not found")
    return db_days


@app.get("/roads", status_code=status.HTTP_200_OK)
async def get_all_roads(db: db_dependency):
    db_roads = db.query(models.Road_Type).all()
    if db_roads is None:
        raise HTTPException(status_code=404, detail="Roads not found")
    return db_roads


@app.get("/lights", status_code=status.HTTP_200_OK)
async def get_all_lights(db: db_dependency):
    db_lights = db.query(models.Light_Conditions).all()
    if db_lights is None:
        raise HTTPException(status_code=404, detail="Lights not found")
    return db_lights


@app.get("/weathers", status_code=status.HTTP_200_OK)
async def get_all_weathers(db: db_dependency):
    db_weathers = db.query(models.Weather).all()
    if db_weathers is None:
        raise HTTPException(status_code=404, detail="Weathers not found")
    return db_weathers


@app.get("/road_surfaces", status_code=status.HTTP_200_OK)
async def get_all_road_surfaces(db: db_dependency):
    db_road_surfaces = db.query(models.Road_Surface).all()
    if db_road_surfaces is None:
        raise HTTPException(status_code=404, detail="Road Surfaces not found")
    return db_road_surfaces


@app.get("/urban_rurals", status_code=status.HTTP_200_OK)
async def get_all_urban_rurals(db: db_dependency):
    db_urban_rurals = db.query(models.Urban_Rural).all()
    if db_urban_rurals is None:
        raise HTTPException(status_code=404, detail="Urban Rurals not found")
    return db_urban_rurals


@app.get("/vehicle_types", status_code=status.HTTP_200_OK)
async def get_all_vehicle_types(db: db_dependency):
    db_vehicle_types = db.query(models.Vehicle_Type).all()
    if db_vehicle_types is None:
        raise HTTPException(status_code=404, detail="Vehicle Types not found")
    return db_vehicle_types


@app.get("/left_hands", status_code=status.HTTP_200_OK)
async def get_all_left_hands(db: db_dependency):
    db_left_hands = db.query(models.Left_Hand).all()
    if db_left_hands is None:
        raise HTTPException(status_code=404, detail="Left Hands not found")
    return db_left_hands


@app.get("/journey_purposes", status_code=status.HTTP_200_OK)
async def get_all_journey_purposes(db: db_dependency):
    db_journey_purposes = db.query(models.Journey_Purpose).all()
    if db_journey_purposes is None:
        raise HTTPException(status_code=404, detail="Journey Purposes not found")
    return db_journey_purposes


@app.get("/sex_drivers", status_code=status.HTTP_200_OK)
async def get_all_sex_drivers(db: db_dependency):
    db_sex_drivers = db.query(models.Sex_Driver).all()
    if db_sex_drivers is None:
        raise HTTPException(status_code=404, detail="SEx of Driver not found")
    return db_sex_drivers


@app.get("/age_bands", status_code=status.HTTP_200_OK)
async def get_all_age_bands(db: db_dependency):
    db_age_bands = db.query(models.Age_Band_Driver).all()
    if db_age_bands is None:
        raise HTTPException(status_code=404, detail="Age Bands not found")
    return db_age_bands


@app.get("/casualty_classes", status_code=status.HTTP_200_OK)
async def get_all_casualty_classes(db: db_dependency):
    db_casualty_classes = db.query(models.Casualty_Class).all()
    if db_casualty_classes is None:
        raise HTTPException(status_code=404, detail="Casualty Classes not found")
    return db_casualty_classes


@app.get("/imd_deciles", status_code=status.HTTP_200_OK)
async def get_all_imd_deciles(db: db_dependency):
    db_imd_deciles = db.query(models.IMD_Decile).all()
    if db_imd_deciles is None:
        raise HTTPException(status_code=404, detail="IMD Deciles not found")
    return db_imd_deciles
