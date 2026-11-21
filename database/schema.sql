CREATE DATABASE IF NOT EXISTS smart_crop_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE smart_crop_db;

CREATE TABLE IF NOT EXISTS farmers (
    farmer_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    farmer_name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    land_area DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (farmer_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS soil_weather (
    soil_weather_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    farmer_id INT UNSIGNED NOT NULL,
    nitrogen DOUBLE NOT NULL,
    phosphorus DOUBLE NOT NULL,
    potassium DOUBLE NOT NULL,
    temperature DOUBLE NOT NULL,
    humidity DOUBLE NOT NULL,
    ph DOUBLE NOT NULL,
    rainfall DOUBLE NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (soil_weather_id),
    CONSTRAINT fk_soil_weather_farmer
        FOREIGN KEY (farmer_id) REFERENCES farmers (farmer_id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS recommendations (
    recommendation_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    farmer_id INT UNSIGNED NOT NULL,
    recommended_crop VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (recommendation_id),
    CONSTRAINT fk_recommendations_farmer
        FOREIGN KEY (farmer_id) REFERENCES farmers (farmer_id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
