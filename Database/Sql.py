from sqlite3 import connect
from sqlite3 import DatabaseError
from sqlite3 import Connection
from os.path import isfile


# Created By Jignesh
class Sql:
    connection = None
    cursor = None

    @staticmethod
    def connect(db_name):
        db = './Database/' + db_name + '.db'
        # db = db_name + '.db'
        if isfile(db):
            try:
                Sql.connection = connect(db)
            except DatabaseError as d:
                print(d)
            except Exception as e:
                print(e)
            finally:
                if isinstance(Sql.connection, Connection):
                    try:
                        Sql.cursor = Sql.connection.cursor()
                    except Exception as e:
                        print(e)
        else:
            print('Database ' + db_name + ' not found')

    @staticmethod
    def create_table():
        sql_command = """
        CREATE TABLE class (
        name VARCHAR(20) PRIMARY KEY,
        path VARCHAR(100));"""
        try:
            Sql.cursor.execute(sql_command)
        except Exception as e:
            print(e)

    @staticmethod
    def insert_path(key, file_path):
        sql_command = """
            INSERT INTO class (name, path)
            VALUES ("{new_key}", "{new_path}");
        """
        sql_command = sql_command.format(new_key=key, new_path=file_path)
        try:
            Sql.cursor.execute(sql_command)
            Sql.connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def get_path(name):
        search_name = "'" + name + "'"
        path = None
        sql_command = """
                SELECT path
                from class
                where name = {name};
            """
        sql_command = sql_command.format(name=search_name)
        try:
            path = Sql.cursor.execute(sql_command)
        except Exception as e:
            print(e)
        if path:
            return path.fetchone()[0]

    @staticmethod
    def has_file(key):
        search_key = "'" + key + "'"
        path = None
        sql_command = """
                    SELECT path
                    from class
                    where name = {key};
                """
        sql_command = sql_command.format(key=search_key)
        try:
            path = Sql.cursor.execute(sql_command)

        except Exception as e:
            print(e)
        if path is not None:
            return len(path.fetchall()) > 0

    @staticmethod
    def disconnect():
        try:
            Sql.cursor.close()
            Sql.connection.close()
        except Exception as e:
            print(e)

# Reset Database
# Sql.connect('Uml_Class')
# Sql.cursor.execute("""DROP TABLE IF EXISTS "class";""")
# Sql.create_table()
# Sql.disconnect()
# Sql.insert_path('int','hello')
# print(Sql.has_file('hello'))
# print(Sql.cursor.execute("""select * from class""").fetchall())
