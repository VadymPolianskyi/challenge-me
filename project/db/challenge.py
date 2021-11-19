from project.db.connect import open_connection_cursor, open_connection
from project.model import Challenge, Participation


class ChallengeDaoInterface:
    def get(self, id: str) -> Challenge:
        """Select challenge by id"""
        pass

    def save(self, challenge: Challenge) -> Challenge:
        """Insert new challenge into DB"""
        pass

    def save_participation(self, participation: Participation) -> Participation:
        """Insert new participation in challenge into DB"""
        pass

    def get_all_active_challenges(self, username: str) -> list[Challenge]:
        """Select active challenges by username"""
        pass


class ChallengeDao(ChallengeDaoInterface):

    def get(self, id: str) -> Challenge:
        with open_connection_cursor() as cursor:
            cursor.execute(
                'SELECT id, name, description, active_from, active_until, created, frequency, price, creator FROM challenge WHERE id = %(id)s',
                {'id': id})
            data = cursor.fetchone()
            if not data:
                print(f"Challenge with id='{id}' not found")  # todo: exception
            else:
                return Challenge(id=data[0], name=data[1], description=data[2], active_from=data[3],
                                 active_until=data[4], created=data[5], frequency=data[6], price=data[7],
                                 creator=data[8])

    def save(self, challenge: Challenge) -> Challenge:
        with open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO challenge (id, name, description, active_from, active_until, created, frequency, price, creator) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (challenge.id, challenge.name, challenge.description, challenge.active_from,
                     challenge.active_until, challenge.created, challenge.frequency, challenge.price,
                     challenge.creator))
                conn.commit()
                print(f"Successfully created challenge('{challenge.id}') by user '{challenge.creator}'.")
        return challenge

    def save_participation(self, participation: Participation) -> Participation:
        with open_connection() as conn:
            with conn.cursor() as cursor:
                print(participation)
                cursor.execute(
                    'INSERT INTO participation (challenge_id, "user", active) VALUES(%(challenge_id)s, %(username)s, %(active)s) ON CONFLICT (challenge_id, "user") DO UPDATE SET active=%(active)s;',
                    {'challenge_id': participation.challenge_id, 'username': participation.username,
                     'active': participation.active})
                conn.commit()
                print(
                    f"Successfully upserted participation of user('{participation.username}') in challenge('{participation.challenge_id}') with active={participation.active}.")
        return participation

    def get_all_active_challenges(self, username: str) -> list[Challenge]:
        with open_connection_cursor() as cursor:
            cursor.execute(
                'SELECT id, name, description, active_from, active_until, created, frequency, price, creator FROM challenge JOIN participation p on challenge.id = p.challenge_id WHERE p."user"=%(username)s and p.active is TRUE',
                {'username': username})

            res = []
            data = cursor.fetchone()

            while data:
                challenge = Challenge(id=data[0], name=data[1], description=data[2], active_from=data[3],
                                      active_until=data[4], created=data[5], frequency=data[6], price=data[7],
                                      creator=data[8])
                res.append(challenge)
                data = cursor.fetchone()

            return res
