	
-- SELECT * FROM tblMeasurementUnits;	


-- SELECT tblMeasurementUnits.name_rus, tblMeasurementUnits.name_eng, tblPhysicalProperty.name_rus
-- 	FROM tblMeasurementUnits, tblPhysicalProperty
-- 	WHERE tblMeasurementUnits.FK_tblPhysicalProperty_tblMeasurementUnits=tblPhysicalProperty.ID_tblPhysicalProperty;
-- 
-- 	
-- SELECT tblMeasurementUnits.name_rus, tblPhysicalProperty.name_rus 
-- 	FROM tblMeasurementUnits JOIN tblPhysicalProperty ON FK_tblPhysicalProperty_tblMeasurementUnits=ID_tblPhysicalProperty;
-- 	

	
-- SELECT tblMeasurementUnits.name_rus, tblPhysicalProperty.name_rus 
-- 	FROM tblMeasurementUnits JOIN tblPhysicalProperty ON FK_tblPhysicalProperty_tblMeasurementUnits=ID_tblPhysicalProperty
-- 	WHERE tblPhysicalProperty.name_rus = 'длинна';

SELECT U.name_rus, P.name_rus 
	FROM tblMeasurementUnits AS U JOIN tblPhysicalProperty AS P ON FK_tblPhysicalProperty_tblMeasurementUnits=ID_tblPhysicalProperty
	WHERE P.name_rus = 'длинна';
