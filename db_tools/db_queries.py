
db_queries = {

    "DELETE_TABLE_QUOTE": """DROP TABLE IF EXISTS quote;;""",


    "CREATE_TABLE_QUOTES": """
                CREATE TABLE IF NOT EXISTS tblQuotes
                ( 
                    ID_tblQuotes INTEGER PRIMARY KEY,
                    catalog TEXT NOT NULL,                   
                    cod TEXT NOT NULL, 
                    name TEXT NOT NULL,
                    item INTEGER,
                    metric TEXT,
                    stat_sum INTEGER DEFAULT NULL,
                    class TEXT DEFAULT NULL,
                    parent TEXT DEFAULT NULL,
                    UNIQUE (cod)
                );""",
    "INSERT_QUOTES": """INSERT INTO tblQuotes (catalog, cod, name, item, metric, stat_sum, class, parent) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?) RETURNING ID_tblQuotes;""",

    "CREATE_TABLE_VALUE-DIMENSIONS": """
                CREATE TABLE IF NOT EXISTS tblValueDimensions
                (
                    ID_tblValueDimensions INTEGER PRIMARY KEY,
                    min_value INTEGER DEFAULT 0,
                    max_value INTEGER DEFAULT 0,
                    unit_dimension TEXT,
                    step_dimension TEXT, 
                    parameter_type INTEGER DEFAULT 0,
                    FK_tblDimensions_tblValueDimensions INTEGER DEFAULT 0,
                    FOREIGN KEY (FK_tblDimensions_tblValueDimensions) REFERENCES tblDimensions (ID_tblDimensions),
                    
                    UNIQUE (FK_tblDimensions_tblValueDimensions, min_value, max_value, unit_dimension, step_dimension, parameter_type)
                );""",

    "INSERT_VALUE-DIMENSIONS": """INSERT INTO tblValueDimensions (min_value, max_value, unit_dimension, step_dimension parameter_type) VALUES (?, ?, ?, ?, ?) RETURNING id;""",

    "CREATE_TABLE_DIMENSIONS": """
                CREATE TABLE IF NOT EXISTS tblDimensions
                (
                    ID_tblDimensions INTEGER PRIMARY KEY,
                    name TEXT,
                    UNIQUE (name)
                );""",

    "CREATE_TABLE_DIMENSIONS-SET": """
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
