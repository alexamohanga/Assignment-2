from cmd import Cmd
from FileHandler.FileReader import FileReader
from FileHandler.FileWriter import FileWriter
from DataExtractor import DataExtractor
from UmlClass import UmlClass
from Database.Sql import Sql
from object_store.Storage import Storage
from Help import Help
from shutil import copy
import re
import os


class Interpreter(Cmd, Help):
    def __init__(self, new_name, new_output_path=None, db_name='Uml_Class'):
        Cmd.__init__(self)
        self.prompt = '>>> '
        self.intro = 'Hi ' + new_name + ' Welcome to \
the Interpreter. Type help or ? to list commands.\n'
        self.extracted_data = []
        self.output_path = new_output_path
        self.db_name = db_name

    def do_extract(self, line):
        options = self.extract_line(line)
        opt = ["f", "d"]
        print(options)
        if len(options) != 2:
            return print('Valid options not provided. Use "help extract" command')
        if opt.index(options[0].lower()) == -1:
            return print('Please provide valid indicator')
        if os.path.isfile(options[1]):
            print('The path provided is not a file!')
        data = []
        if opt.index(options[0].lower()) == "f":
            file_data = FileReader.read_from_file(os.path.abspath(options[1]))
            if file_data != '':
                data.append(file_data)
        elif opt.index(options[0].lower()) == "d":
            data = FileReader.read_from_folder(options[1])
        self.extracted_data = self.extract_class_data(data)

    def do_view(self, arg=""):
        if arg.lower() == 'data':
            return print('Valid options not provided. use "help view" command')
        if len(self.extracted_data) == 0:
            return print('No data available to display. Use "extract" command')
        for a_class_data in self.extracted_data:
            print('Data for ', a_class_data.class_name, ' class.',
                  "Instance attributes names ", a_class_data.instance_attributes,
                  'Instance method names ', a_class_data.instance_methods,
                  'Association Relationship ', a_class_data.association,
                  'Inheritance Relationship ', a_class_data.inheritance)

    def do_generate(self, arg):
        if arg.lower() != 'c':
            return print('Valid options not provided. Use "help generate" command')
        if len(self.extracted_data) == 0:
            return print('No data available to generate\
            diagram. Use "extract" command to extract data first')
        if self.output_path is None:
            self.output_path = os.path.abspath('./output/success')
            print("Output directory path set to: ./output/success")

        if not self.output_path.endswith('.png'):
            self.output_path = os.path.abspath(self.output_path + '/class.png')
            print("Output file set to: class.png")

    def do_get_image(self, line):
        options = self.extract_line(line)

        if len(options) != 2:
            return print('Valid option not provide. Use "help get_image" command')
        if not os.path.isdir(options[1]):
            return print('Please provide a valid Path!!')
        Sql.connect(self.db_name)
        if not Sql.has_file(options[0]):
            print('File Not Found in Database')
        else:
            self.copy_file(Sql.get_path(options[0]), options[1])
        Sql.disconnect()

    def do_store_image(self, line):
        options = self.extract_line(line)
        if len(options) == 2:
            if os.path.isfile(options[1]):
                file_name = os.path.basename(options[1])
                if os.path.isfile('./Database/store/' + file_name) is False:
                    Sql.connect(self.db_name)
                    if Sql.has_file(options[0]) is False:
                        self.copy_file(options[1], './Database/store')
                        Sql.insert_path(options[0],
                                        './Database/store/' + file_name)
                    else:
                        print('Please provide a unique id'
                              'for your file to be stored in databases')
                    Sql.disconnect()
                else:
                    print('Another file with ' +
                          file_name + ' exists in Database')
            else:
                print('Please provide a valid path to the file')
        else:
            print('Valid option not provide. Use "help store_image" command')

    def do_store_data(self, key=None):
        if key is not None:
            if len(self.extracted_data) > 0:
                Storage.open_storage()
                Storage.store(key.lower(), self.extracted_data)
                Storage.close()
            else:
                print('No data available to store. Use "extract" command')
        else:
            print('Key not provided. Use "help store_data" command')

    def do_get_data(self, key=None):
        if key is not None:
            Storage.open_storage()
            self.extracted_data = Storage.get_data(key.lower())
        else:
            print('Key not provided. Use "help get_data" command')

    def do_exit(self, line):
        print('Thank You for using the Interpreter')
        print("Exiting ......")
        return True

    def extract_line(self, line):
        options = []
        for a_command in line.split(' -'):
            striped_command = re.sub('[-]', '', a_command).strip()
            if striped_command != '':
                options.append(striped_command)
        return options

    def extract_class_data(self, raw_data):
        extracted_data = []
        for a_class in raw_data:
            a_class_data = DataExtractor(a_class)
            if a_class_data.class_name is not None:
                extracted_data.append(a_class_data)
        return extracted_data

    #
    def copy_file(self, source, destination):
        copy(source, destination)

