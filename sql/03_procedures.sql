-- BOOK TICKET
CREATE OR REPLACE PROCEDURE book_ticket
(
    p_passenger NUMBER,
    p_flight NUMBER,
    p_seat NUMBER
)
IS
BEGIN
    INSERT INTO bookings (passenger_id, flight_id, seat_number)
    VALUES (p_passenger, p_flight, p_seat);
END;
/

-- CANCEL TICKET
CREATE OR REPLACE PROCEDURE cancel_ticket
(
    p_booking NUMBER
)
IS
    v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM bookings
    WHERE booking_id = p_booking;

    IF v_count = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Booking ID not found');
    END IF;

    UPDATE bookings
    SET status = 'CANCELLED'
    WHERE booking_id = p_booking;
END;
/

-- MAKE PAYMENT
CREATE OR REPLACE PROCEDURE make_payment
(
    p_booking NUMBER,
    p_amount NUMBER,
    p_method VARCHAR2
)
IS
BEGIN
    INSERT INTO payments
    VALUES (payment_seq.NEXTVAL, p_booking, p_amount, p_method, SYSDATE);
END;
/