from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, Text
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import declarative_base, sessionmaker

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

# Create DuckDB Database
name_db = input("What is the database name? ")
DATABASE_URL = f"sqlite:///{name_db}.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(engine)
print("Database and tables created successfully!")