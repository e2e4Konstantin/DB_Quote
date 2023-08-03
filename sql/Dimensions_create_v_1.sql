/*
 * параметры: название, подробное описание
 */
CREATE TABLE IF NOT EXISTS tblParameters
                (
                    ID_tblParameter INTEGER NOT NULL PRIMARY KEY,
                    name TEXT NOT NULL,													-- название параметра
                    description TEXT DEFAULT NULL,										-- подробности
                    UNIQUE (name)
                );
CREATE UNIQUE INDEX idx_name_tblParameters ON tblParameters (name);
               
               
/*
 *  Значения параметров. Набор значений параметра
 */               
CREATE TABLE IF NOT EXISTS tblParameterValues
    (
        ID_tblParameterValue INTEGER PRIMARY KEY, 
        FK_tblQuotes_tblValueParameters INTEGER NOT NULL,								-- Id расценки
        FK_tblParameters_tblValueParameters INTEGER NOT NULL,							-- Id параметра
        parameter_type INTEGER DEFAULT NULL												-- тип параметра
        	CHECK (parameter_type > 0 AND parameter_type < 5), 			
        min_value REAL DEFAULT 0.0 CHECK (min_value >= 0.0),							-- минимальное значение 
        max_value REAL DEFAULT NULL,													-- максимальное значение
        step_value REAL DEFAULT NULL,													-- шаг 
        FK_tblParameterValues_tblMeasurementUnits INTEGER NOT NULL,						-- Id единицы измерения                    
        validity TEXT DEFAULT NULL,														-- применимость, ограничения
        FOREIGN KEY (FK_tblQuotes_tblValueParameters) REFERENCES tblQuotes(ID_tblQuote),
        FOREIGN KEY (FK_tblParameterValues_tblMeasurementUnits) REFERENCES tblMeasurementUnits(ID_tblMeasurementUnit),
        FOREIGN KEY (FK_tblParameters_tblValueParameters) REFERENCES tblParameters(ID_tblParameter),
        CONSTRAINT MarkParameterValues UNIQUE (FK_tblQuotes_tblValueParameters, FK_tblParameters_tblValueParameters) 
    );               
CREATE UNIQUE INDEX idx_ID_tblQuote_tblParameters ON tblParameterValues (FK_tblQuotes_tblValueParameters);

               
-- /-------------------------------------------------------------------------------------------------------
   
INSERT INTO tblParameters (name) VALUES 
	('напряжение'), ('высота этажа'), ('количество телесигналов (ТС)'),	('количество сигналов телеизмерения (ТИ)'), ('Высота здания'),
	('количество сигналов телеизмерения текущих значений параметров (ТИТ)'), ('количество сигналов телеуправления (ТУ)'), ('высота лесов');
    
INSERT INTO tblParameterValues 
  	(
  		FK_tblQuotes_tblValueParameters, FK_tblParameters_tblValueParameters, 
  		parameter_type, min_value, max_value, step_value, FK_tblParameterValues_tblMeasurementUnits, validity
  	) VALUES 
	(
		(SELECT ID_tblQuote FROM tblQuotes WHERE cod = '3.8-27-2'),
		(SELECT ID_tblParameter FROM tblParameters WHERE name = 'высота лесов'), 3, 16, NULL, 4,  
		(SELECT ID_tblMeasurementUnit FROM tblMeasurementUnits WHERE name_rus = 'метр'),'за каждые 4 м свыше 16 м'
	),
	(
		(SELECT ID_tblQuote FROM tblQuotes WHERE cod = '3.8-28-1'), 
		(SELECT ID_tblParameter FROM tblParameters WHERE name = 'высота лесов'), 3, 0, 6, NULL,  
		(SELECT ID_tblMeasurementUnit FROM tblMeasurementUnits WHERE name_rus = 'метр'), NULL
	),
	(	
		(SELECT ID_tblQuote FROM tblQuotes WHERE cod = '4.8-1-5'),
		(SELECT ID_tblParameter FROM tblParameters WHERE name = 'напряжение'), 1, 35, 35, NULL,  
		(SELECT ID_tblMeasurementUnit FROM tblMeasurementUnits WHERE name_rus = 'киловольт'), NULL
	);
                 













