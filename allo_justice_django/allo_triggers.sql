DROP SCHEMA public CASCADE;
CREATE SCHEMA public;


CREATE OR REPLACE FUNCTION schedule_insert_row() 
   RETURNS TRIGGER 
   LANGUAGE PLPGSQL
AS $$
BEGIN
   INSERT INTO schedule(day_name, time_from, time_to, attorney_id)
						VALUES (N'Mo', N'08:00', N'16:00', NEW.id),
							   (N'Tu', N'08:00', N'16:00', NEW.id),
							   (N'We', N'08:00', N'16:00', NEW.id),
						       (N'Th', N'08:00', N'16:00', NEW.id),
							   (N'Fr', N'08:00', N'16:00', NEW.id),
						       (N'Sa', N'08:00', N'16:00', NEW.id),
						       (N'Su', N'', N'', NEW.id);
	RETURN NEW;
END;
$$

CREATE TRIGGER attorney_after_insert_create_schedules
    AFTER INSERT ON attorney
    FOR EACH ROW
    EXECUTE PROCEDURE schedule_insert_row();
	
	
