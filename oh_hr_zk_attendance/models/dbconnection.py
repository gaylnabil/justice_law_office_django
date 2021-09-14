import psycopg2


class DbConnection:

    def __init__(self, username, password, host, port, database):

        self.connection = psycopg2.connect(user=username,
                                           password=password,
                                           host=host,
                                           port=port,
                                           database=database)

    def execute_query(self, query, record=None):
        cursor = self.connection.cursor()
        cursor.execute(query, record)
        self.commit()
        if query.strip().upper().startswith('INSERT'):
            last_fetch = cursor.fetchone()
            if last_fetch:
                return last_fetch[0]

        if query.strip().upper().startswith('UPDATE'):
            return None

        return cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
