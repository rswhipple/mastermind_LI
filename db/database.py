import sqlite3
from sqlite3 import Error
import threading
import queue

class MastermindDB:
    def __init__(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file, check_same_thread=False)  # enable multi-threading
            self.db_queue = queue.Queue()
            self.db_thread = threading.Thread(target=self.db_task_handler)
            self.db_thread.start()
            print(f"Multithread connection to SQLite database at {db_file}")
        except Error as e:
            print(e)

    def db_task_handler(self):
        while True:
            item = self.db_queue.get()
            if item is None:  # None is used to signal the shutdown
                break
            sql, data = item
            cursor = self.conn.cursor()
            cursor.execute(sql, data)
            self.conn.commit()
            self.db_queue.task_done()
        self.conn.close()

    def execute_task(self, sql, data=(), callback=None):
        self.db_queue.put((sql, data, callback))

    def close_task(self):
        self.db_queue.put(None)
        self.db_thread.join()

    def create_table(self, create_table_sql):
        self.execute_task(create_table_sql)

    def add_player(self, name):
        sql = '''INSERT INTO players(name, wins, losses) VALUES(?,?,?)'''
        self.execute_task(sql, name)
    
    def add_game(self, player_id, start_time, end_time, score):
        sql = '''INSERT INTO games(start_time, end_time, result) VALUES(?,?,?)'''
        self.execute_task(sql, (player_id, start_time, end_time, score))
    
    def add_win(self, player_id, game_id):
        sql = '''INSERT INTO wins(player_id, game_id) VALUES(?,?)'''
        self.execute_task(sql, (player_id, game_id))

    def add_loss(self, player_id, game_id):
        sql = '''INSERT INTO wins(player_id, game_id) VALUES(?,?)'''
        self.execute_task(sql, (player_id, game_id))

    # def add_guess(self, game_id, guess, feedback):
    #     sql = '''INSERT INTO guesses(game_id, guess, feedback) VALUES(?,?,?)'''
    #     self.execute_task(sql, (game_id, guess, feedback))

    def close_db(self):
        if self.conn:
            self.conn.close()

def setup_db() -> MastermindDB:
    print("Setting up the database.")

    db = MastermindDB('mastermind.db')
    db.create_table(""" CREATE TABLE IF NOT EXISTS players (
                            player_id integer PRIMARY KEY,
                            name text,
                        ); """)
    db.create_table(""" CREATE TABLE IF NOT EXISTS games (
                            game_id integer PRIMARY KEY,
                            player_id integer,
                            start_time text,
                            end_time text,
                            score integer,
                            FOREIGN KEY (player_id) REFERENCES players (player_id)
                        ); """)
    db.create_table(""" CREATE TABLE IF NOT EXISTS wins (
                            win_id integer PRIMARY KEY,
                            player_id integer,
                            game_id integer,
                            FOREIGN KEY (player_id) REFERENCES players (player_id),
                            FOREIGN KEY (game_id) REFERENCES games (game_id)
                        ); """)
    db.create_table(""" CREATE TABLE IF NOT EXISTS losses (
                            loss_id integer PRIMARY KEY,
                            player_id integer,
                            game_id integer,
                            FOREIGN KEY (player_id) REFERENCES players (player_id),
                            FOREIGN KEY (game_id) REFERENCES games (game_id)
                        ); """)
    # db.create_table(""" CREATE TABLE IF NOT EXISTS guesses (
    #                         guess_id integer PRIMARY KEY,
    #                         game_id integer NOT NULL,
    #                         guess integer NOT NULL,
    #                         feedback text,
    #                         FOREIGN KEY (game_id) REFERENCES games (game_id)
    #                     ); """)

    return db
    

if __name__ == "__main__":
    setup_db()
