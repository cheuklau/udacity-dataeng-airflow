CREATE TABLE IF NOT EXISTS staging_events (
    artist varchar,
    auth varchar,
    firstName varchar,
    gender varchar,
    itemInSession int,
    lastName varchar,
    length float,
    level varchar,
    location varchar,
    method varchar,
    page varchar,
    registration float,
    sessionId int,
    song varchar,
    status int,
    ts varchar,
    userAgent varchar,
    userId int
)

CREATE TABLE IF NOT EXISTS staging_songs (
    num_songs int,
    artist_id varchar,
    artist_latitude varchar,
    artist_longitude varchar,
    artist_location varchar,
    artist_name varchar,
    song_id varchar,
    title varchar,
    duration float,
    year int
)

CREATE TABLE IF NOT EXISTS songplay (
    songplay_id bigint IDENTITY(0,1) PRIMARY KEY,
    start_time varchar,
    user_id varchar,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id varchar,
    location varchar,
    user_agent varchar
)

CREATE TABLE IF NOT EXISTS users (
    user_id varchar PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
)

CREATE TABLE IF NOT EXISTS song (
    song_id varchar PRIMARY KEY,
    title varchar,
    artist_id varchar,
    year varchar,
    duration float
)

CREATE TABLE IF NOT EXISTS artist (
    artist_id varchar PRIMARY KEY,
    name varchar,
    location varchar,
    latitude varchar,
    longitude varchar
)

CREATE TABLE IF NOT EXISTS time (
    start_time timestamp PRIMARY KEY,
    hour varchar,
    day varchar,
    week varchar,
    month varchar,
    year varchar,
    weekday varchar
)