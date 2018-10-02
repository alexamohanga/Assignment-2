class Help:
    # Created by Jignesh
    def help_extract(self):
        print(
            """
            Extracts UML Class Diagram data \
            from the given file or folder.
            Syntax: extract -[indicator]=Required -[path]=Required
            :param indicator: [f]=file or [d]=Directory.
            :param path: Provide a Absolute or Relative \
            path. "Path should not contain any '-' character".
            :return: None
            """
        )

    # Created by Jignesh
    def help_exit(self):
        print(
            """
            Exit the application.
            Syntax: exit
            :param : None.
            :return: True
            """
        )

    # Created by Suman
    def help_view(self):
        print(
            """
            View extracted data.
            Syntax: view [option]=Required
            :param option: [data]=currently extracted data.
            :return: None
            """
        )

    # Created by Bikrant
    def help_generate(self):
        print(
            """
            Generates Diagram in a .png format.
            Syntax: generate [option]=Required
            :param option: [c]=Class Diagram.
            :return: None
            """
        )

    # Created by Jignesh
    def help_get_image(self):
        print(
            """
            Get stored image from database.
            Syntax: get_image -[Id]=Required -[Path]=Required
            :param :[id]=Unique id of the stored image.
            :param :[Path]=Output path for the image.
            :return: None
            """
        )

    # Created by Jignesh
    def help_store_image(self):
        print(
            """
            Stored image in the database.
            Syntax: store_image -[Id]=Required -[Path]=[Required]
            :param : [id]=Unique id to store image.
            :param : [Path]=Valid path for the image to be stored.\
             "Path should not contain any '-' character"
            :return: None
            """
        )

    # Created by Jignesh
    def help_get_data(self):
        print(
            """
            Get stored data from database.
            Syntax: get_data [key]=Required
            :param :[key]=Unique key of the stored data.
            :return: None
            """
        )

    # Created by Jignesh
    def help_store_data(self):
        print(
            """
            Stored extracted data in the database.
            Syntax: store_data [Key]=Required
            :param : [key]= key for the data to be stored.
            :return: None
            """
        )
