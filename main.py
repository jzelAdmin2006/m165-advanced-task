from db import Db

db = Db()

def proceed():
    print('These are all softwares with their serial numbers:')
    for software in db.get_all_softwares():
        print(software['serial'] + ': ' + software['name'])


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
