/*
 * Атрибуты: название, подробное описание
 */
CREATE TABLE IF NOT EXISTS tblAttributes
                (
                    ID_tblAttribute INTEGER NOT NULL PRIMARY KEY,
                    name TEXT NOT NULL,													-- название атрибута
                    description TEXT DEFAULT NULL,										-- подробности
                    UNIQUE (name)
                );
CREATE UNIQUE INDEX idx_name_tblAttributes ON tblAttributes (name);

/*
 *  Значения Атрибутов. 
 */               
CREATE TABLE IF NOT EXISTS tblAttributeValues
    (
        ID_tblAttributeValue INTEGER PRIMARY KEY, 
        FK_tblQuotes_tblAttributeValues INTEGER NOT NULL,								-- Id расценки
        FK_tblAttributes_tblAttributeValues INTEGER NOT NULL,							-- Id атрибута                    
        attribute_value TEXT NOT NULL,													-- значение атрибута
        FOREIGN KEY (FK_tblQuotes_tblAttributeValues) REFERENCES tblQuotes(ID_tblQuote),
        FOREIGN KEY (FK_tblAttributes_tblAttributeValues) REFERENCES tblAttributes(ID_tblAttribute),
        
        UNIQUE (FK_tblQuotes_tblAttributeValues, FK_tblAttributes_tblAttributeValues, attribute_value) 
    );               
CREATE INDEX idx_ID_tblQuote_tblAttributeValues ON tblAttributeValues (FK_tblQuotes_tblAttributeValues);

-- /-------------------------------------------------------------------------------------------------------

INSERT INTO tblAttributeValues (name) VALUES 
	('группа'), ('способ производства работ'), ('элемент'),	('материал'), ('расположение'),	('тип');

INSERT INTO tblAttributeValues (FK_tblQuotes_tblAttributeValues, FK_tblAttributes_tblAttributeValues, attribute_value) VALUES 
	(
		(SELECT ID_tblQuote FROM tblQuotes WHERE cod = '3.1-1-2'),
		(SELECT ID_tblAttribute FROM tblAttributes WHERE name = 'способ производства работ'),'Разработка грунта в отвал экскаваторами'
	),
	(
		(SELECT ID_tblQuote FROM tblQuotes WHERE cod = '3.1-1-2'),
		(SELECT ID_tblAttribute FROM tblAttributes WHERE name = 'группа'),'4'
	),
	(
		(SELECT ID_tblQuote FROM tblQuotes WHERE cod = '3.22-52-10'),
		(SELECT ID_tblAttribute FROM tblAttributes WHERE name = 'элемент'),	'Упор'
	),
	(
		(SELECT ID_tblQuote FROM tblQuotes WHERE cod = '3.22-52-10'),
		(SELECT ID_tblAttribute FROM tblAttributes WHERE name = 'материал'), 'Бетонный'
	),
	(
		(SELECT ID_tblQuote FROM tblQuotes WHERE cod = '3.22-52-10'),
		(SELECT ID_tblAttribute FROM tblAttributes WHERE name = 'тип'), 'Постоянный'
	),
	(
		(SELECT ID_tblQuote FROM tblQuotes WHERE cod = '3.22-52-10'),
		(SELECT ID_tblAttribute FROM tblAttributes WHERE name = 'расположение'), 'На трубопроводе'
	);
	
-- /-------------------------------------------------------------------------------------------------------

CREATE VIEW attribute_values_view AS 	
	SELECT 
		tblQuotes.cod AS 'код', 
		tblAttributes.name AS 'атрибут',
		tblAttributeValues.attribute_value  AS 'значение'
	FROM tblAttributeValues
	LEFT JOIN tblQuotes ON tblQuotes.ID_tblQuote = tblAttributeValues.FK_tblQuotes_tblAttributeValues  
	LEFT JOIN tblAttributes ON tblAttributes.ID_tblAttribute = tblAttributeValues.FK_tblAttributes_tblAttributeValues

DROP VIEW attribute_values_view 
	
SELECT * FROM attribute_values_view
