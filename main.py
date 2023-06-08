from db import Db

db = Db()

def proceed():
    while True:
        print('These are all softwares with their serial numbers:')
        for software in db.get_all_softwares():
            print(software['serial'] + ': ' + software['name'])

        commandInput = input('Please enter your command [i] insert software / [k] keys of software / [ik] insert software key / [q] quit: ')
        match commandInput:
            case 'q':
                break



if db.db_col_is_available():
    proceed()
else:
    while True:
        createDbColInput = input('The database with the collection does not exist. Do you wish to create them? [y] / [n] ')
        match createDbColInput:
            case 'y':
                db.initialize()
                proceed()
                break
            case 'n':
                break

print('Terminating...')
