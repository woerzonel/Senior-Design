CREATE TABLE if not exists notes(
    id INTEGER PRIMARY KEY,
    note TEXT
);

CREATE TABLE if not exists breweries(
    id INTEGER PRIMARY KEY,
    breweryName TEXT
);

CREATE TABLE if not exists beerTypes(
    id INTEGER PRIMARY KEY,
    typeName TEXT
);

CREATE TABLE if not exists beer(
    id INTEGER PRIMARY KEY,
    beerName TEXT,
    breweryId INTEGER,
    typeId INTEGER,
    abv REAL,
    FOREIGN KEY (breweryId) REFERENCES breweries(id),
    FOREIGN KEY (typeId) REFERENCES beerTypes(id)
);

CREATE TABLE if not exists notesToBeer(
    beerId INTEGER,
    noteId INTEGER,
    PRIMARY KEY (beerId, noteId),
    FOREIGN KEY (beerId) REFERENCES beer(id),
    FOREIGN KEY (noteId) REFERENCES notes(id)
);

CREATE TABLE if not exists onTap(
    id INTEGER PRIMARY KEY,
    sensorId INTEGER,
    beerId INTEGER,
    volumeRecord REAL,
    initialVolume REAL,
    FOREIGN KEY (beerId) REFERENCES beer(id)
);
