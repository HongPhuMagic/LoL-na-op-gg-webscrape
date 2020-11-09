CREATE TABLE lol_player_stats (
    username_id VARCHAR(15) NOT NULL,
    champion VARCHAR(15) NOT NULL,
    game_length VARCHAR(15) NOT NULL,
    game_type VARCHAR(15) NOT NULL,
    champ_lvl SMALLINT NOT NULL,
    kills SMALLINT NOT NULL,
    deaths SMALLINT NOT NULL,
    assists SMALLINT NOT NULL
);