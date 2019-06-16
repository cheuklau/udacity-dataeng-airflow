class SqlQueries:
    songplay_table_insert = ("""
    INSERT INTO {} (
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent
    ) 
    SELECT e.ts as start_time,
        e.userId as user_id,
        e.level as level,
        s.song_id as song_id,
        s.artist_id as artist_id,
        e.sessionId as session_id,
        e.location as location,
        e.userAgent as user_agent
    FROM staging_events e
    JOIN staging_songs s ON (e.song = s.title AND e.artist = s.artist_name) 
    """)

    user_table_insert = ("""
    INSERT INTO {} (
        user_id,
        first_name,
        last_name,
        gender,
        level
    )
    SELECT DISTINCT e.userId as user_id,
        e.firstName as first_name,
        e.lastName as last_name,
        e.gender as gender,
        e.level as level
    FROM staging_events e
    WHERE user_id IS NOT NULL
    """)

    song_table_insert = ("""
    INSERT INTO {} (
        song_id,
        title,
        artist_id,
        year,
        duration
    )
    SELECT DISTINCT s.song_id as song_id,
        s.title as title,
        s.artist_id as artist_id,
        s.year as year,
        s.duration as duration
    FROM staging_songs s
    """)

    artist_table_insert = ("""
    INSERT INTO {} (
        artist_id,
        name,
        location,
        latitude,
        longitude
    )
    SELECT DISTINCT s.artist_id as artist_id,
        s.artist_name as name,
        s.artist_location as location,
        s.artist_latitude as latitude,
        s.artist_longitude as longitude
    FROM staging_songs s
    """)

    time_table_insert = ("""
    INSERT INTO {} (
        start_time,
        hour,
        day,
        week,
        month,
        year,
        weekday
    )
    SELECT DISTINCT timestamp 'epoch' + CAST(e.ts AS BIGINT)/1000 * interval '1 second' as start_time,
        extract(HOUR FROM timestamp 'epoch' + CAST(e.ts AS BIGINT)/1000 * interval '1 second') as hour,
        extract(DAY FROM timestamp 'epoch' + CAST(e.ts AS BIGINT)/1000 * interval '1 second') as day,
        extract(WEEK FROM timestamp 'epoch' + CAST(e.ts AS BIGINT)/1000 * interval '1 second') as week,
        extract(MONTH FROM timestamp 'epoch' + CAST(e.ts AS BIGINT)/1000 * interval '1 second') as month,
        extract(YEAR FROM timestamp 'epoch' + CAST(e.ts AS BIGINT)/1000 * interval '1 second') as year,
        extract(DAY FROM timestamp 'epoch' + CAST(e.ts AS BIGINT)/1000 * interval '1 second') as weekday
    FROM staging_events e
    """)