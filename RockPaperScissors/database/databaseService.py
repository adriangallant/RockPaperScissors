import sqlite3

conn = sqlite3.connect('rock_paper_scissors.db')
cursor = conn.cursor()


def open_connection():
    global cursor, conn
    conn = sqlite3.connect('rock_paper_scissors.db')
    cursor = conn.cursor()


def close_connection():
    global cursor, conn
    conn.commit()
    cursor.close()
    conn.close()


def create_table():
    open_connection()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS results (
                        id INTEGER NOT NULL PRIMARY KEY,
                        winner TEXT DEFAULT 'NONE' NOT NULL,
                        loser TEXT DEFAULT 'NONE' NOT NULL,
                        winner_choice TEXT DEFAULT 'NONE' NOT NULL,
                        loser_choice TEXT DEFAULT 'NONE' NOT NULL,
                        tie_choice TEXT DEFAULT 'NONE' NOT NULL,
                        second_player TEXT NOT NULL,
                        datetime DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                    """)
    close_connection()


def insert_result(winner, loser, winner_choice, loser_choice, tie_choice, second_player):
    open_connection()
    cursor.execute("""
                    INSERT INTO results(winner, loser, winner_choice, loser_choice, tie_choice, second_player) 
                    VALUES(?, ?, ?, ?, ?,?)
                    """, (winner, loser, winner_choice, loser_choice, tie_choice, second_player)
                   )
    close_connection()
