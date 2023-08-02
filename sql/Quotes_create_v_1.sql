
CREATE TABLE IF NOT EXISTS tblQuotes
                (
                    ID_tblQuotes	INTEGER PRIMARY KEY,
                    description		TEXT NOT NULL, 						-- название расценки
                    cod 			TEXT NOT NULL,						-- код расценки
                    catalog_cod 	TEXT NOT NULL,						-- код таблицы классификатора     
                    zoom 			INTEGER,							-- коэффициент масштабирования
                    stat_sum 		INTEGER DEFAULT 0,					-- статистика использования
                    parent 			TEXT DEFAULT NULL,					-- код родительской расценки
                    FK_tblQuotes_tblDefinitions INTEGER NOT NULL,		-- определение расценки: разработка/устройство/...
                    FK_tblQuotes_tblMeasuringObjects INTEGER NOT NULL,	-- что измеряет: грунт/трубопровод/...
                    FK_tblQuotes_tblMeasurementUnits INTEGER NOT NULL,	-- в чем измеряется метр/километр/штука...                    
                    FOREIGN KEY (FK_tblQuotes_tblDefinitions) REFERENCES tblDefinitions(ID_tblDefinition),
                    FOREIGN KEY (FK_tblQuotes_tblMeasuringObjects) REFERENCES tblMeasuringObjects(ID_tblMeasuringObject),
                    FOREIGN KEY (FK_tblQuotes_tblMeasurementUnits) REFERENCES tblMeasurementUnits(ID_tblMeasurementUnit),
                    UNIQUE (cod)
                );
CREATE UNIQUE INDEX idx_cod_tblQuotes ON tblQuotes (cod);               
                
INSERT INTO tblQuotes
(description, cod, catalog_cod, zoom, stat_sum, parent, FK_tblQuotes_tblDefinitions, FK_tblQuotes_tblMeasuringObjects, FK_tblQuotes_tblMeasurementUnits) VALUES 
	('Разработка грунта в отвал экскаваторами с ковшом вместимостью 1,8 м3 группа грунтов 4', '3.1-1-2', '3.1-1-1-0-1', 100, 1, NULL, 
	 	(SELECT ID_tblDefinition FROM tblDefinitions WHERE name = 'разработка'),
	 	(SELECT ID_tblMeasuringObject FROM tblMeasuringObjects WHERE name = 'грунт'),
	 	(SELECT ID_tblMeasurementUnit FROM tblMeasurementUnits WHERE name_rus = 'метр кубический'));
	 
INSERT INTO tblQuotes
(description, cod, catalog_cod, zoom, stat_sum, parent, FK_tblQuotes_tblDefinitions, FK_tblQuotes_tblMeasuringObjects, FK_tblQuotes_tblMeasurementUnits) VALUES 
	('Устройство постоянных бетонных упоров на трубопроводе диаметром 800 мм', '3.22-52-10', '3.22-0-15-0-52',  1, 1, NULL,
		(SELECT ID_tblDefinition FROM tblDefinitions WHERE name = 'устройство бетонных упоров'),
		(SELECT ID_tblMeasuringObject FROM tblMeasuringObjects WHERE name = 'трубопровод'),
		(SELECT ID_tblMeasurementUnit FROM tblMeasurementUnits WHERE name_rus = 'километр'));	 


SELECT tblQuotes.cod, tblQuotes.description, tblDefinitions.name,  tblMeasuringObjects.name,  tblMeasurementUnits.name_rus 
FROM  tblQuotes
INNER JOIN tblDefinitions ON tblDefinitions.ID_tblDefinition  = tblQuotes.FK_tblQuotes_tblDefinitions 
INNER JOIN tblMeasuringObjects ON tblMeasuringObjects.ID_tblMeasuringObject = tblQuotes.FK_tblQuotes_tblMeasuringObjects 
INNER JOIN tblMeasurementUnits ON tblMeasurementUnits.ID_tblMeasurementUnit  = tblQuotes.FK_tblQuotes_tblMeasurementUnits 	
	
CREATE VIEW quotes_view AS 	
	SELECT 
		tblQuotes.catalog_cod  AS 'каталог',
		tblQuotes.cod AS 'код', 
		tblQuotes.description AS 'содержание', 
		tblDefinitions.name AS 'определение',  
		tblMeasuringObjects.name AS 'что измеряет',
		tblQuotes.zoom  AS 'масштаб',
		tblMeasurementUnits.short_name_rus AS 'единица измерения',
		tblQuotes.stat_sum AS 'статистика',
		tblQuotes.parent AS 'родительская расценка'
	FROM  tblQuotes
	LEFT JOIN tblDefinitions ON tblDefinitions.ID_tblDefinition  = tblQuotes.FK_tblQuotes_tblDefinitions 
	LEFT JOIN tblMeasuringObjects ON tblMeasuringObjects.ID_tblMeasuringObject = tblQuotes.FK_tblQuotes_tblMeasuringObjects 
	LEFT JOIN tblMeasurementUnits ON tblMeasurementUnits.ID_tblMeasurementUnit  = tblQuotes.FK_tblQuotes_tblMeasurementUnits

DROP VIEW quotes_view 
	
SELECT * FROM quotes_view  	
	
	
	
	
 
/*
 * определение расценки  
 */
CREATE TABLE IF	NOT EXISTS tblDefinitions 
				(
					ID_tblDefinition 	INTEGER PRIMARY KEY,
                    name				TEXT NOT NULL, 			-- название определения расценки
                    synonym				TEXT DEFAULT NULL,
                    UNIQUE (name)
				);
				
INSERT INTO tblDefinitions (name, synonym) VALUES ('разработка', NULL), ('устройство бетонных упоров', NULL), ('подвешивание', NULL);


/*
 * объекты которые измеряет расценка / измерение расценки 
 */
CREATE TABLE IF NOT EXISTS  tblMeasuringObjects(
		ID_tblMeasuringObject INTEGER PRIMARY KEY,
		name TEXT NOT NULL,
		description TEXT,
		UNIQUE (name)				
);

CREATE UNIQUE INDEX idx_name_tblMeasuringObjects ON tblMeasuringObjects (name);     

INSERT INTO tblMeasuringObjects (name) VALUES ('яма'), ('основание'), ('комплект'), ('грунт'), ('трубопровод') ;


			