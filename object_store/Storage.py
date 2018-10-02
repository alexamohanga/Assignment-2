import shelve


# Created By Jignesh
class Storage:
    db = None

    @staticmethod
    def open_storage():
        Storage.db = shelve.open('./object_store'
                                 '/storage.shelf', 'c')

    @staticmethod
    def store(key, new_data):
        if isinstance(Storage.db, shelve.DbfilenameShelf):
            Storage.db[key] = new_data

    @staticmethod
    def get_data(key):
        if isinstance(Storage.db, shelve.DbfilenameShelf):
            try:
                return Storage.db[key]
            except KeyError as e:
                print('Key Not Found')

    @staticmethod
    def close():
        Storage.db.close()
