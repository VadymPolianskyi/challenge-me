CREATE TABLE "user" (
  username varchar NOT NULL,
  "name" varchar,
  age integer,
  token varchar,
  email varchar,
  PRIMARY KEY(username)
);

CREATE TYPE frequency AS ENUM ('HOUR', 'DAY', 'WEEK', 'MONTH');

CREATE TABLE challenge(
  id varchar NOT NULL,
  "name" varchar,
  description varchar,
  "from" timestamp,
  "until" timestamp,
  created timestamp,
  frequency frequency,
  price integer,
  PRIMARY KEY(id)
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