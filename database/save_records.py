
from database.db_connection import create_connection


def save_farmer_record(
    farmer_name,
    location,
    land_area,
    nitrogen,
    phosphorus,
    potassium,
    temperature,
    humidity,
    ph,
    rainfall,
    recommended_crop
):
    connection = create_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        # Save farmer details
        farmer_query = """
            INSERT INTO farmers (farmer_name, location, land_area)
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            farmer_query,
            (farmer_name, location, land_area)
        )

        farmer_id = cursor.lastrowid

        # Save soil and weather details
        soil_query = """
            INSERT INTO soil_weather (
                farmer_id, nitrogen, phosphorus, potassium,
                temperature, humidity, ph, rainfall
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            soil_query,
            (
                farmer_id, nitrogen, phosphorus, potassium,
                temperature, humidity, ph, rainfall
            )
        )

        # Save crop recommendation
        recommendation_query = """
            INSERT INTO recommendations (
                farmer_id, recommended_crop
            )
            VALUES (%s, %s)
        """

        cursor.execute(
            recommendation_query,
            (farmer_id, recommended_crop)
        )

        connection.commit()

        return True

    except Exception as e:
        connection.rollback()
        print("Error saving farmer record:", e)
        return False

    finally:
        if cursor:
            cursor.close()

        connection.close()
