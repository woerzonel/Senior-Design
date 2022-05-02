INSERT INTO notes (id, note) VALUES
    (-1, 'toasty'),
    (-2, 'malty'),
    (-3, 'fruit'),
    (-4, 'sour'),
    (-5, 'bitter'),
    (-6, 'balanced');

INSERT INTO breweries (id, breweryName) VALUES
    (-1, 'MKE'),
    (-2, 'Lake Front'),
    (-3, 'Great Lakes Brewing Company'),
    (-4, 'Dogfish Head');

INSERT INTO beerTypes (id, typeName) VALUES
    (-1, 'Lager'),
    (-2, 'Ale'),
    (-3, 'Brown Ale'),
    (-4, 'Stout'),
    (-5, 'IPA'),
    (-6, 'Pale Ale'),
    (-7, 'Pilsner'),
    (-8, 'Porter');

INSERT INTO beer (id, breweryId, beerName, typeId, abv) VALUES
    (-1, -1, 'Louies Resurection', -3, .089),
    (-2, -2, 'Stein', -1, .066),
    (-3, -3, 'Christomas Ale', -2, .07),
    (-4, -4, '90 minute IPA', -5, .09),
    (-5, -4, 'Blah Beer', -7, .056);

INSERT INTO notesToBeer (beerId, noteId) VALUES
    (-1, -2),
    (-1, -1),
    (-2, -2),
    (-3, -2),
    (-4, -5);

INSERT INTO onTap (id, sensorId, beerId, volumeRecord, initialVolume) VALUES
    (-1, 1234, -1, 0, 100),
    (-2, 2343, -2, 0, 100)
