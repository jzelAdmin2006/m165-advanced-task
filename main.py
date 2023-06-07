from db import Db

db = Db()

def proceed():
    print('Hello, World!')


if db.db_col_is_available():
    proceed()
else:
    while True:
        createDbColInput = input('The database with the collection does not exist. Do you wish to create them? [y] / [n]')
        if createDbColInput == 'y':
            db.initialize()
            proceed()
            break
        elif createDbColInput == 'n':
            break

print('Terminating...')
