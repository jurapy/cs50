-- Keep a log of any SQL queries you execute as you solve the mystery.

--CRIME SCENE REPORTS
SELECT description FROM crime_scene_reports
WHERE street = "Humphrey Street"
AND year = 2021
AND month = 7
AND day = 28;


--TRANSCRIPTS FROM INTERVIEWS
SELECT transcript FROM interviews
WHERE transcript LIKE "%bakery%";


-- THIEF LICENCE PLATE NUMBER
SELECT license_plate FROM bakery_security_logs
WHERE activity = "exit"
AND year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute BETWEEN 15 AND 25;


-- THIEF BANK ACCOUNT NUMBER
SELECT account_number FROM atm_transactions
WHERE transaction_type = "withdraw"
AND atm_location = "Leggett Street"
AND year = 2021
AND month = 7
AND day = 28;


-- CALLER AND RECEIVER PHONE NUMBER
SELECT caller, receiver FROM phone_calls
WHERE duration < 60
AND year = 2021
AND month = 7
AND day = 28;


-- THIEF PHONE NUMBER
SELECT caller FROM phone_calls
WHERE duration < 60
AND year = 2021
AND month = 7
AND day = 28;


-- RECIEVER PHONE NUMBER
SELECT receiver FROM phone_calls
WHERE duration < 60
AND year = 2021
AND month = 7
AND day = 28;


--EARLIEST FLIGHT DESTINATION
SELECT flights.id, origin_airport_id, destination_airport_id, hour, minute, a1.city AS origin_city, a2.city AS destination_city
FROM flights
LEFT JOIN airports a1 ON flights.origin_airport_id = a1.id
LEFT JOIN airports a2 ON flights.destination_airport_id = a2.id
WHERE year = 2021
AND month = 7
AND day = 29
ORDER BY hour;


-- THIEF AND ACCOMPLICE PASSPORT NUMBER
SELECT flight_id, passport_number, seat
FROM passengers
WHERE flight_id = 36
ORDER BY seat;


--QUERY FOR THIEF
SELECT *
FROM people
JOIN phone_calls
ON phone_calls.caller = people.phone_number
JOIN passengers
ON passengers.passport_number = people.passport_number
JOIN bakery_security_logs
ON bakery_security_logs.license_plate = people.license_plate
WHERE activity = "exit"
AND bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute BETWEEN 15 AND 25
AND passengers.flight_id = 36
AND phone_calls.duration < 60
AND phone_calls.year = 2021
AND phone_calls.month = 7
AND phone_calls.day = 28;


--QUERY FOR ACCOMPLICE
SELECT *
FROM people
JOIN phone_calls
ON phone_calls.receiver = people.phone_number
JOIN passengers
ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = 36
AND phone_calls.duration < 60
AND phone_calls.year = 2021
AND phone_calls.month = 7
AND phone_calls.day = 28;
