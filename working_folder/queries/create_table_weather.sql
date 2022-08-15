create sequence if not exists weather_row_sequence
    increment by 1;
CREATE TABLE IF NOT EXISTS weather(
   row_id BIGINT default  nextval('weather_row_sequence'::regclass) PRIMARY KEY
  ,title                  VARCHAR NOT NULL
  ,woeid                  INTEGER  NOT NULL
  ,id                     VARCHAR NOT NULL
  ,weather_state_name     VARCHAR NOT NULL
  ,weather_state_abbr     VARCHAR NOT NULL
  ,wind_direction_compass VARCHAR NOT NULL
  ,created                TIMESTAMP WITHOUT TIME ZONE NOT NULL
  ,applicable_date        DATE  NOT NULL
  ,min_temp               NUMERIC NOT NULL
  ,max_temp               NUMERIC NOT NULL
  ,the_temp               NUMERIC NOT NULL
  ,wind_speed             VARCHAR NOT NULL
  ,wind_direction         VARCHAR NOT NULL
  ,air_pressure           NUMERIC NOT NULL
  ,humidity               INTEGER  NOT NULL
  ,visibility             VARCHAR NOT NULL
  ,predictability         INTEGER  NOT NULL
);
