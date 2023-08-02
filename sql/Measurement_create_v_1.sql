/*
 * измеряемые свойства объектов
 */
CREATE TABLE IF NOT EXISTS tblPhysicalPropertys(
		ID_tblPhysicalProperty INTEGER PRIMARY KEY,
		name_rus TEXT NOT NULL,
		name_eng TEXT NOT NULL,
		short_name TEXT,
		UNIQUE (name_rus, name_eng)				
);

INSERT INTO tblPhysicalPropertys (name_rus, name_eng, short_name) VALUES 
	('площадь', 'square', 's'),
	('масса', 'mass', 'n'),
	('количество', 'quantity', 'n'),
	('время', 'time', 't'),
	('длинна', 'length', 'l'),
	('объем', 'volume', 'v');

/*
 * единицы измерения, со ссылкой на физическую сущность измерения
 */
CREATE TABLE tblMeasurementUnits(
		ID_tblMeasurementUnit INTEGER PRIMARY KEY,
		name_rus TEXT NOT NULL,
		name_eng TEXT NOT NULL,
		short_name_rus TEXT,
		short_name_eng TEXT,
		basis INTEGER DEFAULT 0, -- AS Boolean
		multiplier REAL,
		FK_tblPhysicalProperty_tblMeasurementUnits INTEGER NOT NULL,  -- указатель на физичесескую сущность измерения 
		FOREIGN KEY (FK_tblPhysicalProperty_tblMeasurementUnits) 
			REFERENCES tblPhysicalPropertys(ID_tblPhysicalProperty),
		UNIQUE (name_rus, name_eng)
);

INSERT INTO tblMeasurementUnits (name_rus, name_eng, short_name_rus, short_name_eng, basis, multiplier, FK_tblPhysicalProperty_tblMeasurementUnits) VALUES
('метр', 'metr', 'м', 'm', 1, 1,  (SELECT ID_tblPhysicalProperty FROM tblPhysicalPropertys WHERE name_rus = 'длинна')),
('миллиметр', 'millimeter', 'мм', 'mm', 0, 0.001, (SELECT ID_tblPhysicalProperty FROM tblPhysicalPropertys WHERE name_rus = 'длинна' )),
('километр', 'kilometer', 'км', 'km', 0, 1000.0, (SELECT ID_tblPhysicalProperty FROM tblPhysicalPropertys WHERE name_rus = 'длинна' )),
('метр квадратный', 'meter square', 'м2', 'm2', 1, 1, (SELECT ID_tblPhysicalProperty FROM tblPhysicalPropertys WHERE name_rus = 'площадь' )),
('метр кубический', 'cubic meter', 'м3', 'm3', 1, 1, (SELECT ID_tblPhysicalProperty FROM tblPhysicalPropertys WHERE name_rus = 'объем' )),
('метр погонный', 'meter linea', 'мп', 'lm', 0, 1, (SELECT ID_tblPhysicalProperty FROM tblPhysicalPropertys WHERE name_rus = 'длинна' )),
('штука', 'unit', 'шт', 'u', 1, 1, (SELECT ID_tblPhysicalProperty FROM tblPhysicalPropertys WHERE name_rus = 'количество' ));







