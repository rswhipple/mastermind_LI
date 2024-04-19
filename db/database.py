import sqlite3
from sqlite3 import Error

class MastermindDB:
    def __init__(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(f"Connected to SQLite database at {db_file}")
        except Error as e:
            print(e)

    def create_table(self, create_table_sql):
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def add_game(self, start_time, end_time, result):
        sql = '''INSERT INTO games(start_time, end_time, result) VALUES(?,?,?)'''
        cur = self.conn.cursor()
        cur.execute(sql, (start_time, end_time, result))
        self.conn.commit()
        return cur.lastrowid

    def add_guess(self, game_id, guess_number, guess_value, feedback):
        sql = '''INSERT INTO guesses(game_id, guess_number, guess_value, feedback) VALUES(?,?,?,?)'''
        cur = self.conn.cursor()
        cur.execute(sql, (game_id, guess_number, guess_value, feedback))
        self.conn.commit()
        return cur.lastrowid

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

# Usage
if __name__ == '__main__':
    db = MastermindDB('mastermind.db')
    db.create_table(""" CREATE TABLE IF NOT EXISTS games (
                            game_id integer PRIMARY KEY,
                            start_time text NOT NULL,
                            end_time text,
                            result text
                        ); """)
    db.create_table(""" CREATE TABLE IF NOT EXISTS guesses (
                            guess_id integer PRIMARY KEY,
                            game_id integer NOT NULL,
                            guess_number integer NOT NULL,
                            guess_value text NOT NULL,
                            feedback text,
                            FOREIGN KEY (game_id) REFERENCES games (game_id)
                        ); """)
    
    # Example of adding a game and a guess
    game_id = db.add_game('2023-04-01 10:00:00', '2023-04-01 10:30:00', 'win')
    guess_id = db.add_guess(game_id, 1, 'RGBY', 'Two correct, one wrong position')
    
    db.close()
