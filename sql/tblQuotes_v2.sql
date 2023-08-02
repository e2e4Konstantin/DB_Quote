CREATE TABLE IF NOT EXISTS tblQuotes(
	cod TEXT PRIMARY KEY, 
	name TEXT NOT NULL,
	catalog TEXT NOT NULL,
	FK_tblMeasurementUnits_tblQuotes INTEGER DEFAULT 0, -- m2
	FK_tblMeasuringObject_tblQuotes INTEGER DEFAULT 0,	-- покрытия полосы и обочин
	lot INTEGER,
	stat_count INTEGER DEFAULT NULL,
	class TEXT DEFAULT NULL,
	parent TEXT DEFAULT NULL
);


CREATE TABLE IF NOT EXISTS  tblMeasuringObject(
		Id_tblMeasuringObject INTEGER PRIMARY KEY,
		name TEXT NOT NULL,
		description TEXT,
		UNIQUE (name)				
);
INSERT INTO tblMeasuringObject (name) VALUES ('яма'), ('основание'), ('комплект');


CREATE TABLE IF NOT EXISTS tblPhysicalProperty(
		Id_tblPhysicalProperty INTEGER PRIMARY KEY,
		name_rus TEXT NOT NULL,
		name_eng TEXT NOT NULL,
		short_name TEXT,
		UNIQUE (name_rus, name_eng)				
);

INSERT INTO tblPhysicalProperty (name_rus, name_eng, short_name) VALUES 
	('площадь', 'square', 's'),
	('масса', 'mass', 'n'),
	('количество', 'quantity', 'n'),
	('время', 'time', 't'),
	('длинна', 'length', 'l'),
	('объем', 'volume', 'v');
	
SELECT * FROM tblPhysicalProperty;
SELECT Id_tblPhysicalProperty AS 'Id' FROM tblPhysicalProperty 	WHERE name_rus = 'масса';
SELECT DISTINCT name_eng FROM tblPhysicalProperty; -- уникальные значения столбца



CREATE TABLE IF NOT EXISTS tblMeasurementUnits(
		Id_tblMeasurementUnits INTEGER PRIMARY KEY,
		name_rus TEXT NOT NULL,
		name_eng TEXT NOT NULL,
		short_name_rus TEXT,
		short_name_eng TEXT,
		basis INTEGER DEFAULT 0, -- AS Boolean
		multiplier REAL,
		FK_tblPhysicalProperty_tblMeasurementUnits INTEGER NOT NULL, -- 'square
		UNIQUE (name_rus, name_eng, FK_tblPhysicalProperty_tblMeasurementUnits)				
);

INSERT INTO tblMeasurementUnits (name_rus, name_eng, short_name_rus, short_name_eng, basis, multiplier, FK_tblPhysicalProperty_tblMeasurementUnits) VALUES
('метр', 'metr', 'м', 'm', 1, 1,  5),
('миллиметр', 'millimeter', 'мм', 'mm', 0, 0.001, 5),
('метр квадратный', 'meter square', 'м2', 'm2', 1, 1, 1),
('метр кубический', 'cubic meter', 'м3', 'm3', 1, 1, 6),
('метр погонный', 'meter linea', 'мп', 'lm', 0, 1, 5);

INSERT INTO tblMeasurementUnits (name_rus, name_eng, short_name_rus, short_name_eng, basis, multiplier, FK_tblPhysicalProperty_tblMeasurementUnits) 
	SELECT 'тонна', 'ton', 'т', 't', 0, 1000, Id_tblPhysicalProperty  
	FROM tblPhysicalProperty WHERE name_rus = 'масса';
	
INSERT INTO tblMeasurementUnits (name_rus, name_eng, short_name_rus, short_name_eng, basis, multiplier, FK_tblPhysicalProperty_tblMeasurementUnits) 
	SELECT 'килограмм', 'kilogram', 'кг', 'kg', 1, 1, Id_tblPhysicalProperty  
	FROM tblPhysicalProperty WHERE name_rus = 'масса';	

INSERT INTO tblMeasurementUnits (name_rus, name_eng, short_name_rus, short_name_eng, basis, multiplier, FK_tblPhysicalProperty_tblMeasurementUnits) VALUES
('километр', 'kilometer', 'км', 'km', 0, 1000, (SELECT Id_tblPhysicalProperty FROM tblPhysicalProperty WHERE name_rus = 'длинна' ));
	
	






