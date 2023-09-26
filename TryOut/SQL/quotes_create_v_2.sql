
--DROP TABLE tblTables
CREATE TABLE IF	NOT EXISTS tblTables
    (
        ID_tblTables 	INTEGER PRIMARY KEY,
        code 			TEXT NOT NULL,			-- шифр таблицы
        description		TEXT NOT NULL, 			-- описание таблицы
        UNIQUE (code)
    );
CREATE UNIQUE INDEX idx_code_tblTables ON tblQuotes (code);


--DROP TABLE tblQuotes
CREATE TABLE IF NOT EXISTS tblQuotes
    (
        ID_tblQuote		INTEGER PRIMARY KEY,
        code 			TEXT NOT NULL,					-- шифр расценки
        description     TEXT NOT NULL, 				    -- описание расценки
        FK_tblQuotes_tblTables INTEGER NOT NULL,		-- id таблицы в которой находится расценка
        quarter         INTEGER NOT NULL,               -- номер квартала / дата актуальности
        FOREIGN KEY (FK_tblQuotes_tblTables) REFERENCES tblTables(ID_tblTables),
        UNIQUE (code)
    );
CREATE UNIQUE INDEX idx_code_tblQuotes ON tblQuotes (code);

INSERT INTO tblQuotes (description, cod, quarter, FK_tblQuotes_tblTables) VALUES
	('Разработка грунта в отвал экскаваторами с ковшом вместимостью 1,8 м3 группа грунтов 4', '3.1-1-2', 68,
	 	(SELECT ID_tblDefinition FROM tblTables WHERE code = '3.1-1-1-0-1'));








PRAGMA table_info(tblQuotes);


CREATE TABLE _tblQuotes_history (
    _ID_tblQuote INTEGER,           -- 1        id измененной расценки
    ID_tblQuotes_history INTEGER,
    code TEXT,                      -- 2
    description TEXT,               -- 4
    FK_tblQuotes_tblTables INTEGER, -- 8
    _version INTEGER,
    _updated INTEGER,
    _mask INTEGER
);
CREATE INDEX idx__tblQuotes_history_ID_tblQuote ON _tblQuotes_history (_ID_tblQuote);

CREATE TRIGGER quote_insert_history
AFTER INSERT ON tblQuotes
BEGIN
    INSERT INTO _people_history (_ID_tblQuote, ID_tblQuotes_history, code, description, FK_tblQuotes_tblTables, _version, _updated, _mask)
    VALUES (new.ID_tblQuote, new.ID_tblQuotes_history, new.code, new.description, new.FK_tblQuotes_tblTables, 1, cast((julianday('now') - 2440587.5) * 86400 * 1000 as integer), 15);
END;
