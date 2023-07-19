
db_queries = {

    "DELETE_TABLE_QUOTE": """DROP TABLE IF EXISTS quote;;""",


    "CREATE_TABLE_QUOTES": """
                CREATE TABLE IF NOT EXISTS tblQuotes
                ( 
                    ID_tblQuotes INTEGER PRIMARY KEY,                   
                    cod TEXT UNIQUE NOT NULL, 
                    name TEXT UNIQUE NOT NULL,
                    item TEXT,
                    metric TEXT,
                    parental_quote  TEXT DEFAULT NULL, --заменить на ссылку related_cod INTEGER REFERENCES Quotes
                    --FK_tblValueDimensions_tblQuotes INTEGER DEFAULT 0,
                    --FOREIGN KEY (FK_tblValueDimensions_tblQuotes) REFERENCES tblValueDimensions (ID_tblValueDimensions)    
                    UNIQUE (cod),
                    UNIQUE (name)
                );""",
    "INSERT_QUOTES": """INSERT INTO tblQuotes (cod, name, item, metric) VALUES (?, ?, ?, ?) RETURNING id;""",

    "CREATE_TABLE_VALUE_DIMENSIONS": """
                CREATE TABLE IF NOT EXISTS tblValueDimensions
                (
                    ID_tblValueDimensions INTEGER PRIMARY KEY,
                    min_value INTEGER DEFAULT 0,
                    max_value INTEGER DEFAULT 0,
                    unit_dimension TEXT,
                    step_dimension TEXT, 
                    parameter_type INTEGER DEFAULT 0,
                    FK_tblDimensions_tblValueDimensions INTEGER DEFAULT 0,
                    FOREIGN KEY (FK_tblDimensions_tblValueDimensions) REFERENCES tblDimensions (ID_tblDimensions)
                    
                    UNIQUE (FK_tblDimensions_tblValueDimensions, min_value, max_value, unit_dimension, step_dimension, parameter_type)
                );""",

    "INSERT_VALUE_DIMENSIONS": """INSERT INTO tblValueDimensions (min_value, max_value, unit_dimension, step_dimension parameter_type) VALUES (?, ?, ?, ?, ?) RETURNING id;""",

    "CREATE_TABLE_DIMENSIONS": """
                CREATE TABLE IF NOT EXISTS tblDimensions
                (
                    ID_tblDimensions INTEGER PRIMARY KEY,
                    name TEXT,
                    UNIQUE (name)
                );""",

    "CREATE_TABLE_DIMENSIONS_SET": """
                CREATE TABLE IF NOT EXISTS tblDimensionSets
                (
                    ID_tblDimensionSets INTEGER PRIMARY KEY,
        
                    FK_tblQuotes_tblDimensionSets INTEGER DEFAULT 0,
                    FK_tblValueDimensions_tblDimensionSets INTEGER DEFAULT 0,
                    
                    FOREIGN KEY (FK_tblQuotes_tblDimensionSets) REFERENCES tblQuotes (ID_tblQuotes),
                    FOREIGN KEY (FK_tblValueDimensions_tblDimensionSets) REFERENCES tblValueDimensions (ID_tblValueDimensions),

                    UNIQUE (FK_tblQuotes_tblDimensionSets, FK_tblValueDimensions_tblDimensionSets)
                );""",


}
