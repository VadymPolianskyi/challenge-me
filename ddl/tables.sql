create table "user" (
  username varchar not null,
  "name" varchar,
  age integer,
  token varchar,
  email varchar,
  primary key(username)
);


create type frequency as enum ('HOUR', 'DAY', 'WEEK', 'MONTH');

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


create table participation
(
    challenge_id varchar not null
        constraint participation_challenge_id_fk
            references challenge,
    "user"       varchar not null
        constraint participation_user_username_fk
            references "user",
    active       boolean,
    constraint participation_pk
        primary key (challenge_id, "user")
);


create table "check"
(
    challenge_id varchar not null
        constraint check_challenge_id_fk
            references challenge,
    "user"       varchar not null
        constraint chek_user_username_fk
            references "user",
    timestamp timestamp,
    constraint check_pk
        primary key (challenge_id, "user")
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