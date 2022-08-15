INSERT INTO
    weather(
            title,
            woeid,
            id,
            weather_state_name,
            weather_state_abbr,
            wind_direction_compass,
            created,
            applicable_date,
            min_temp,
            max_temp,
            the_temp,
            wind_speed,
            wind_direction,
            air_pressure,
            humidity,
            visibility,
            predictability
            )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
