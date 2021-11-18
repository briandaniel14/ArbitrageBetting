import sqlite3 as sq

connection = sq.connect('Betting.db')

cursor = connection.cursor()

# Create bookie table

command1 = """CREATE TABLE IF NOT EXISTS
bookies(Bookie_ID TEXT PRIMARY KEY, Transaction_Fee FLOAT)"""

cursor.execute(command1)

# Creating a bets table

command2 = """CREATE TABLE IF NOT EXISTS
bets(Bookie_ID TEXT,  
Bet_Type text, 
DateOfMatch DATE,
Sport TEXT, 
Team1 TEXT, 
Team2 TEXT, 
O1 FLOAT,
O2 FLOAT,
O3 FLOAT, 
URLs TEXT,
PRIMARY KEY (Bookie_ID, DateofMatch, Team1, Team2),
FOREIGN KEY(Bookie_ID) REFERENCES bookies(Bookie_ID))"""

cursor.execute(command2)

# populating the bookies table

# populating the bets table


def DisplayBets():
    cursor.execute("select * FROM bets")
    print("{:<15} {:<12} {:<12} {:<12} {:<20} {:<20} {:<7} {:<7} {:<7} {:<40} \n".format(
        'Bookie ID',
        'Bet Type',
        'Date',
        'Sport',
        'Team 1',
        'Team 2',
        'O1',
        'O2',
        'O3',
        'URL',
    ))

    for v in cursor.fetchall():
        BookieID, Bet_Type, Date, Sport, Team1, Team2, O1, O2, O3, URLs = v
        print(("{:<15} {:<12} {:<12} {:<12} {:<20} {:<20} {:<7} {:<7} {:<7} {:<40}").format(
            BookieID,
            Bet_Type,
            Date,
            Sport,
            Team1,
            Team2,
            O1,
            O2,
            O3,
            URLs
        ))


def DisplayBookies():
    cursor.execute("SELECT * FROM Bookies")

    print("{:<20} {:<15} \n".format('Bookie', 'Fee'))

    for v in cursor.fetchall():
        BookieID, Fee = v
        print("{:<20} {:<15}".format(BookieID, Fee))

# Code to take data from text file an smack it into the database


# bookies
file = open("BookieData.txt", "r")
content = file.read()
file.close()

lines = content.split('\n')


for record in lines:

    data = record.split('!')

    a = f"""
    INSERT INTO BOOKIES VALUES
    (
    '{data[0]}',
    '{data[1]}'
    )
    """

    cursor.execute(a)

# bets
file = open("BetsData.txt", "r")
content = file.read()
file.close()

lines = content.split('\n')


for record in lines:

    data = record.split('!')

    pk = data[0]

    a = f"""
    INSERT INTO BETS VALUES
    (
    '{data[0]}',
    '{data[1]}',
    '{data[2]}',
    '{data[3]}',
    '{data[4]}',
    '{data[5]}',
    '{data[6]}',
    '{data[7]}',
    '{data[8]}',
    '{data[9]}'
    )
    """

    cursor.execute(a)


if __name__ == '__main__':
    DisplayBookies()
    print()
    DisplayBets()
    print()
