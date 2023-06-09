from db import Db

db = Db()


def proceed():
    while True:
        print('These are all softwares with their serial numbers:')
        for software in db.get_all_softwares():
            print(str(software['_id']) + ': "' + software['name'] + '" by ' + software['producer'])

        command_input = input(
            'Please enter your command [i] insert software / [k] keys of software / [ik] insert software key / [q] '
            'quit: ')
        match command_input:
            case 'q':
                break
            case 'i':
                name = input('Please enter the software name: ')
                producer = input('Please enter the name of the producer of the software "' + name + '": ')
                db.insert_software(name, producer)
            case 'k':
                while True:
                    serial = input('Please enter the serial number of your software: ')
                    try:
                        software = db.get_software(serial)
                    except ValueError:
                        print('The serial number is not valid.')
                        continue
                    if software is not None:
                        print('These are all keys of the software "' + software['name'] + '": ')
                        for key in software['keys']:
                            print(key)
                        break
            case 'ik':
                while True:
                    serial = input('Please enter the serial number of your software: ')
                    software = db.get_software(serial)
                    if software is not None:
                        db.insert_key(software, input('Please enter the new key: '))
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
