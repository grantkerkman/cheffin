from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, Text, TIMESTAMP
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import declarative_base

# Create the Base
Base = declarative_base()

# Meals Table
class Meal(Base):
    __tablename__ = "meals"

    recipe_name = Column(String, primary_key=True)
    recipe_description = Column(Text)
    date_added = Column(TIMESTAMP)
    primary_protein = Column(String)
    category = Column(String)
    vegetarian = Column(Boolean)

# Recipes Table
class Recipe(Base):
    __tablename__ = "recipes"

    recipe_name = Column(String, primary_key=True)
    ingredients = Column(JSON)
    instructions = Column(Text)
    portions = Column(Integer)

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