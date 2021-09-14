-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE users
(
    card_no integer NOT NULL,
    pin integer NOT NULL,
    last_event_id integer,
    status character varying(10),
    CONSTRAINT users_pkey PRIMARY KEY (pin)
)


CREATE TABLE attendance
(
    id BIGSERIAL PRIMARY KEY,
    card_no integer,
    pin integer,
    verified integer NULL,
    door_id integer NULL,
    event_type integer NULL,
    status character varying(10) NULL,
    date_event timestamp with time zone NULL,
    flag boolean DEFAULT false
)
