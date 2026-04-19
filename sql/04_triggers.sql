CREATE OR REPLACE TRIGGER check_seats
BEFORE INSERT ON bookings
FOR EACH ROW
DECLARE
    seat_count NUMBER;
    max_seats NUMBER;
BEGIN
    SELECT COUNT(*) INTO seat_count
    FROM bookings
    WHERE flight_id = :NEW.flight_id;

    SELECT total_seats INTO max_seats
    FROM flights
    WHERE flight_id = :NEW.flight_id;

    IF seat_count >= max_seats THEN
        RAISE_APPLICATION_ERROR(-20001, 'No seats available');
    END IF;
END;
/