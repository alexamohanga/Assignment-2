# Created By suman

"""
>>> from Validation.Validator import Validator
>>> Validator.validate('./data/UnformatedCode.py')
'f'
>>> Validator.validate('./data/InvalidCode.py')
'c'
>>> from FileHandler.FileReader import FileReader
>>> import ast
>>> data = FileReader.read('./data/MultipleClass')
./data/MultipleClass  was not found
>>> Validator.contains_multiple_class(ast.parse(data))
True
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)