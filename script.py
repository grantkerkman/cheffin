from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, Text, TIMESTAMP
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import declarative_base, sessionmaker

import sqlalchemy_classes as alchemy

# Set up the engine and session factory once (not inside the function)
DATABASE_URL = alchemy.DATABASE_URL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def add_meal():
    # Enter in the recipe data and convert to records
    recipe_name = input(f'Enter Recipe Name: ')
    recipe_description = input(f'Enter Description: ')
    primary_protein = input(f'What is the primary protein: ')
    category = input(f'What is the food category: ')
    vegetarian = input(f'Vegitarian [y/n]: ')

    meal = alchemy.Meal(
        recipe_name=recipe_name,
        recipe_description=recipe_description,
        primary_protein=primary_protein,
        category=category,
        vegetarian=vegetarian
    )

    # Add Meal to Database and close
    session = Session()

    try:
        session.add(meal)
        session.commit()
        print('Meal added successfully!')

    except Exception as e:
        session.rollback()
        print(f"Error adding meal: {e}")

    finally:
        session.close()

    return
