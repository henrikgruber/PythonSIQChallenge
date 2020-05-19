#calling operating system calls
import os
#importing modules
import importlib

def auto_install():
    try:
        try:
            #trying to import the given module
            importlib.import_module("pandas")
            print("Pandas already installed, all good")
        except ImportError:
            #in case the module has not been installed, it will now
            #   be installed
            print ("Trying to Install required module: pandas\n")
            os.system('python -m pip install pandas')
            print("successfully installed PANDAS")
    except ImportError:
        print("install error of PANDAS")
    return