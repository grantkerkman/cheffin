from sqlalchemy import Column, String, Integer, Float, Boolean, Text
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import declarative_base

# Create the Base
Base = declarative_base()

# Meals Table
class Meal(Base):
    __tablename__ = "meals"

    recipe_name = Column(String, primary_key=True)
    recipe_description = Column(Text)
    category = Column(String)
    region = Column(String)
    ingredients = Column(JSON)
    instructions = Column(Text)
    portions = Column(Integer)
    vegetarian = Column(Boolean)


# Nutrition Table
class Nutrition(Base):
    __tablename__ = "nutrition"

    item = Column(String, primary_key=True)
    amount = Column(Float)
    units = Column(String)
    unit_type = Column(String)
    calories = Column(Float)
    fat = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fiber = Column(Float)

# Database URL
DATABASE_URL = "sqlite:///cheffin.db"

