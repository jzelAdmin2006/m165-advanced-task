import bson.errors

from db import Db
from software import Software

db = Db()


def proceed():
    while True:
        print('These are all softwares with their serial numbers:')
        for software in db.get_all_softwares():
            print(software.get_id() + ': "' + software.name + '" by ' + software.producer)

        command_input = input(
            'Please enter your command [i] insert software / [k] keys of software / [ik] insert software key / [q] '
            'quit: ')
        match command_input:
            case 'q':
                break
            case 'i':
                name = input('Please enter the software name: ')
                producer = input('Please enter the name of the producer of the software "' + name + '": ')
                db.insert_software(Software(name, producer, []))
            case 'k':
                software = get_software_by_serial(software)
                print('These are all keys of the software "' + software.name + '": ')
                for key in software.keys:
                    print(key)
            case 'ik':
                db.insert_key(get_software_by_serial(software), input('Please enter the new key: '))


def get_software_by_serial(software):
    while True:
        serial = input('Please enter the serial number of your software: ')
        try:
            software = db.get_software(serial)
        except bson.errors.InvalidId:
            print('The serial number is not valid.')
            continue
        except TypeError:
            print('The serial number does not exist.')
            continue
        break
    return software


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
