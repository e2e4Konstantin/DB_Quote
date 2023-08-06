db_queries = {

    "DELETE_TABLE_QUOTE": """DROP TABLE IF EXISTS tblQuotes;""",

    "CREATE_TABLE_QUOTES": """
        CREATE TABLE IF NOT EXISTS tblQuotes
            (
                ID_tblQuote		 INTEGER PRIMARY KEY NOT NULL,
                description		 TEXT NOT NULL, 							-- подробное название расценки
                cod 			 TEXT NOT NULL,								-- код расценки
                catalog_cod 	 TEXT NOT NULL,								-- код таблицы классификатора
                measurement_text TEXT DEFAULT NULL,                         -- сырой текст измерения расценки
                zoom 			 INTEGER DEFAULT 1 CHECK (zoom > 0),		-- коэффициент масштабирования
                stat_sum 		 INTEGER DEFAULT 0 CHECK (stat_sum >= 0),	-- статистика использования
                parent 			 TEXT DEFAULT NULL,							-- код родительской расценки
                FK_tblQuotes_tblQuoteDefinitions INTEGER NOT NULL,				-- определение расценки: разработка/устройство/...
                FK_tblQuotes_tblMeasuringObjects INTEGER NOT NULL,			-- что измеряет: грунт/трубопровод/...
                FK_tblQuotes_tblMeasurementUnits INTEGER NOT NULL,			-- в чем измеряется метр/километр/штука...
                FOREIGN KEY (FK_tblQuotes_tblQuoteDefinitions) REFERENCES tblQuoteDefinitions(ID_tblQuoteDefinitions),
                FOREIGN KEY (FK_tblQuotes_tblMeasuringObjects) REFERENCES tblMeasuringObjects(ID_tblMeasuringObject),
                FOREIGN KEY (FK_tblQuotes_tblMeasurementUnits) REFERENCES tblMeasurementUnits(ID_tblMeasurementUnit),
                UNIQUE (cod)
            );""",

    "CREATE_INDEX_QUOTES": """CREATE UNIQUE INDEX idx_cod_tblQuotes ON tblQuotes (cod);""",

    "INSERT_QUOTES": """
        INSERT INTO tblQuotes (
            description, cod, catalog_cod, measurement_text, zoom, stat_sum, parent, 
            FK_tblQuotes_tblQuoteDefinitions, 
            FK_tblQuotes_tblMeasuringObjects, 
            FK_tblQuotes_tblMeasurementUnits) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) RETURNING ID_tblQuote;""",
    # -------------------------------------------------------------------------------------------------------------
    "CREATE_TABLE_QUOTE_DEFINITIONS": """
        CREATE TABLE IF	NOT EXISTS tblQuoteDefinitions 
            (
                ID_tblQuoteDefinition 	INTEGER PRIMARY KEY NOT NULL,
                name				    TEXT NOT NULL, 			-- название определения расценки
                synonym				    TEXT DEFAULT NULL,      -- синоним или 2 название
                UNIQUE (name)
            );""",

    "CREATE_INDEX_QUOTE_DEFINITIONS": """CREATE UNIQUE INDEX idx_name_tblQuoteDefinitions ON tblQuoteDefinitions (name);""",

    "INSERT_QUOTE_DEFINITIONS": """INSERT INTO tblQuoteDefinitions (name, synonym) VALUES (?, ?) RETURNING ID_tblQuoteDefinition;""",
    # -------------------------------------------------------------------------------------------------------------
    "CREATE_TABLE_MEASURING_OBJECTS": """
        CREATE TABLE IF	NOT EXISTS tblMeasuringObjects 
            (
                ID_tblMeasuringObject INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,     -- название измеряемого объекта расценки
                description TEXT,       -- описание назначения объекта
                UNIQUE (name)	
            );""",

    "CREATE_INDEX_MEASURING_OBJECTS": """CREATE UNIQUE INDEX idx_name_tblMeasuringObjects ON tblMeasuringObjects (name);""",

    "INSERT_MEASURING_OBJECTS": """INSERT INTO tblMeasuringObjects (name, description) VALUES (?, ?) RETURNING ID_tblMeasuringObject;""",
    # -------------------------------------------------------------------------------------------------------------
    "CREATE_TABLE_PHYSICAL_PROPERTIES": """
        CREATE TABLE IF	NOT EXISTS tblPhysicalProperties 
            (
                ID_tblPhysicalProperty INTEGER PRIMARY KEY,
                name_rus TEXT NOT NULL,
                name_eng TEXT NOT NULL,
                short_name TEXT,
                UNIQUE (name_rus, name_eng)	
            );""",

    "INSERT_PHYSICAL_PROPERTIES": """INSERT INTO tblPhysicalProperties (name_rus, name_eng, short_name) VALUES (?, ?, ?) RETURNING ID_tblPhysicalProperty;""",
    "DELETE_DATA_FROM_PHYSICAL_PROPERTIES": """DELETE FROM tblPhysicalProperties;""",

    "GET_ID_PHYSICAL_PROPERTY": """SELECT ID_tblPhysicalProperty FROM tblPhysicalProperties WHERE name_rus = ?""",
    
    
    
    
    # -------------------------------------------------------------------------------------------------------------
    "CREATE_TABLE_MEASUREMENT_UNITS": """
        CREATE TABLE IF	NOT EXISTS tblMeasurementUnits 
            (
                ID_tblMeasurementUnit INTEGER PRIMARY KEY,
                name_rus TEXT NOT NULL,
                name_eng TEXT NOT NULL,
                short_name_rus TEXT,
                short_name_eng TEXT,
                basis INTEGER DEFAULT 0, -- AS Boolean
                multiplier REAL,
                FK_tblPhysicalProperties_tblMeasurementUnits INTEGER NOT NULL,  -- указатель на физическую сущность измерения 
                FOREIGN KEY (FK_tblPhysicalProperties_tblMeasurementUnits) REFERENCES tblPhysicalProperties(ID_tblPhysicalProperty),
                UNIQUE (name_rus, name_eng)	
            );""",

    "CREATE_INDEX_MEASUREMENT_UNITS": """CREATE UNIQUE INDEX idx_name_tblMeasurementUnits ON tblMeasurementUnits (name_rus);""",
    "DROP_INDEX_MEASUREMENT_UNITS": """DROP INDEX IF EXISTS idx_name_tblMeasurementUnits;""",

    "INSERT_MEASUREMENT_UNITS": """INSERT INTO tblMeasurementUnits (name_rus, name_eng, short_name_rus, short_name_eng, basis, multiplier, FK_tblPhysicalProperties_tblMeasurementUnits) VALUES (?, ?, ?, ?, ?, ?, ?) RETURNING ID_tblMeasurementUnit;""",
}
