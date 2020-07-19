import sys
import subprocess
import pkg_resources

required = {'numpy', "matplotlib", 'basemap'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
eingabe = ""

if missing:
    print("Folgende Module sind nicht insterliert:")
    for miss in missing:
        print("-",miss)
    eingabe = input("Möchten Sie diese Module interlieren [J/N]")
else:
    print("Alle erforderlichen Module sind bereits Insterliert :)")

if(eingabe == "J" or eingabe == "j"):
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing])
else:
    print("Module werden nicht insterliert.")

input("\nPress 'ENTER' to exit...")