CREATE TABLE "user" (
  username varchar NOT NULL,
  "name" varchar,
  age integer,
  token varchar,
  email varchar,
  PRIMARY KEY(username)
);

CREATE TYPE frequency AS ENUM ('HOUR', 'DAY', 'WEEK', 'MONTH');

create table challenge
(
    id           varchar not null
        constraint challenge_pkey
            primary key,
    name         varchar,
    description  varchar,
    active_from  timestamp,
    active_until timestamp,
    created      timestamp,
    frequency    frequency,
    price        double precision,
    creator      varchar
        constraint challenge_user_username_fk
            references "user"
);

CREATE TABLE payment(
  id varchar NOT NULL,
  "user" varchar NOT NULL,
  payment_system varchar,
  card_number varchar,
  expiration_date date,
  placeholder varchar,
  PRIMARY KEY(id),
  CONSTRAINT "Forein key" UNIQUE("user")
);

CREATE TABLE participation(
  challenge_id varchar NOT NULL,
  "user" varchar NOT NULL,
  "time" varchar NOT NULL,
  status varchar,
  PRIMARY KEY(challenge_id, "time", "user")
);