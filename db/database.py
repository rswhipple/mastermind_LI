import sqlite3
from sqlite3 import Error
# import threading
# import queue

class MastermindDB:
    def __init__(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file, check_same_thread=False)
            self.conn.execute("PRAGMA foreign_keys = ON;")
            self.conn.commit()
            # print(f"Connected to SQLite database at {db_file}")
        except sqlite3.Error as e: 
            print(e)

    def close_db(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            # print("Database connection closed.\n")

    def create_table(self, create_table_sql):
        self._execute_task(create_table_sql)

    def add_player(self, name):
        sql = 'INSERT INTO players(name) VALUES(?)'
        return self._execute_task(sql, (name,))
    
    def add_game(self, player_id, dur, score):
        sql = 'INSERT INTO games(player_id, duration, score) VALUES(?,?,?)'
        return self._execute_task(sql, (player_id, dur, score))
    
    def add_win(self, player_id, game_id, round):
        sql = 'INSERT INTO wins(player_id, game_id, round) VALUES(?,?,?)'
        return self._execute_task(sql, (player_id, game_id, round))

    def add_loss(self, player_id, game_id):
        sql = 'INSERT INTO wins(player_id, game_id) VALUES(?,?)'
        return self._execute_task(sql, (player_id, game_id))
    
    # def add_guess(self, game_id, round, guess, feedback):
    #     sql = '''INSERT INTO guesses(game_id, round, guess, feedback) VALUES(?,?,?,?)'''
    #     self.execute_task(sql, (game_id, round, guess, feedback))

    def find_player(self, name):
        sql = '''SELECT * FROM players WHERE name = (?)'''
        return self._get_data(sql, (name,))

    def _execute_task(self, sql, data=()):
        try:
            c = self.conn.cursor()
            c.execute(sql, data)
            self.conn.commit()
            return c.lastrowid
        except Error as e:
            # print(e)
            return None
    
    def _get_data(self, sql, data=()):
        try:
            c = self.conn.cursor()
            c.execute(sql, data)
            return c.fetchall()
        except Error as e:
            # print(e)
            return None


def setup_db():
    print("Checking for database.")

    db = MastermindDB('mm_db.sqlite3')
    db.create_table(""" CREATE TABLE IF NOT EXISTS players (
                            id integer PRIMARY KEY,
                            name text UNIQUE
                        ); """)
    db.create_table(""" CREATE TABLE IF NOT EXISTS games (
                            id integer PRIMARY KEY,
                            player_id integer,
                            duration text,
                            score integer,
                            FOREIGN KEY (player_id) REFERENCES players (id)
                        ); """)
    db.create_table(""" CREATE TABLE IF NOT EXISTS wins (
                            id integer PRIMARY KEY,
                            player_id integer,
                            game_id integer,
                            round integer,
                            FOREIGN KEY (player_id) REFERENCES players (id),
                            FOREIGN KEY (game_id) REFERENCES games (id)
                        ); """)
    db.create_table(""" CREATE TABLE IF NOT EXISTS losses (
                            id integer PRIMARY KEY,
                            player_id integer,
                            game_id integer,
                            FOREIGN KEY (player_id) REFERENCES players (id),
                            FOREIGN KEY (game_id) REFERENCES games (id)
                        ); """)
    # db.create_table(""" CREATE TABLE IF NOT EXISTS guesses (
    #                         guess_id integer PRIMARY KEY,
    #                         game_id integer,
    #                         round integer,
    #                         guess integer,
    #                         feedback text,
    #                         FOREIGN KEY (game_id) REFERENCES games (game_id)
    #                     ); """)

    db.close_db()

def connect_db() -> MastermindDB:
    db_file = 'mm_db.sqlite3'
    return MastermindDB(db_file)


if __name__ == "__main__":
    setup_db()



# add to connect_db for multithread
    # if multi:
    #     return MultiThreadDB(db_file)
    # else:
    #     return MastermindDB(db_file)

# class MultiThreadDB(MastermindDB):
#     def __init__(self, db_file):
#         super.__init__(db_file)
#         self.db_queue = queue.Queue() # add Queue for task_handler
#         self.db_thread = threading.Thread(target=self._db_task_handler) # create Thread for task_handler
#         self.db_thread.start()
#         print(f"Multithread connection to SQLite database ./{db_file}.\n")

#     def close_db(self):
#         self.db_queue.put(None)
#         self.db_thread.join()
#         if self.conn:
#             self.conn.close()
#             self.conn = None
#             print("Database connection closed.")
    
#     def _db_task_handler(self):
#         while True:
#             item = self.db_queue.get()
#             if item is None:
#                 self.conn.close()
#                 break
#             sql, data = item
#             try:
#                 cursor = self.conn.cursor()
#                 cursor.execute(sql, data)
#                 self.conn.commit()
#             except sqlite3.DatabaseError as e:
#                 print(f"Database error: {e}")
#                 # Reconnect attempt here
#             finally:
#                 self.db_queue.task_done()

#     def _execute_task(self, sql, data=()):
#         self.db_queue.put((sql, data))