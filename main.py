from db import Db

db = Db()


def proceed():
    while True:
        print('These are all softwares with their serial numbers:')
        for software in db.get_all_softwares():
            print(str(software['_id']) + ': "' + software['name'] + '" by ' + software['producer'])

        commandInput = input(
            'Please enter your command [i] insert software / [k] keys of software / [ik] insert software key / [q] quit: ')
        match commandInput:
            case 'q':
                break
            case 'i':
                name = input('Please enter the software name: ')
                producer = input('Please enter the name of the producer of the software "' + name + '": ')
                db.insert_software(name, producer)
            case 'k':
                while True:
                    serial = input('Please enter the serial number of your software: ')
                    software = db.get_software(serial)
                    if software is not None:
                        print('These are all keys of the software "' + software['name'] + '": ')
                        for key in software['keys']:
                            print(key)
                        break


if db.db_col_is_available():
    proceed()
else:
    while True:
        createDbColInput = input(
            'The database with the collection does not exist. Do you wish to create them? [y] / [n] ')
        match createDbColInput:
            case 'y':
                db.initialize()
                proceed()
                break
            case 'n':
                break

print('Terminating...')
