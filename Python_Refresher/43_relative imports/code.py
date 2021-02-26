import mymodule # absolute import

print("code.py: ", __name__)


# print statements

# operator.py:  libs.operations.operator # relative import can be done because there is a folder
# mylib.py:  libs.mylibs # relative import can be done because there is a folder
# mymodule.py:  mymodule # relative import Can't be done because there is NO folder
# code.py:  __main__ # relative import Can't be done because there is NO folder

# Relative import with FROM sintax always
