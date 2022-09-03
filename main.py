'''
 !/usr/bin/env python3
 Path: innit.py
 Description: This file is used to innitiate the project. It is run when the project is started and it creates the innit.py file and the logs folder. It also deletes old log files.
 Author: @Ze7111
'''

# ====================================================================================== Default imports =======================================================================================================================================================================#
try: # try
    import sys, os, time, logging, shutil, rich
except Exception as e:
    import os
    string = str(e)
    module = string.split("'")[1].split("'")[0]
    os.system(f'pip install {module}')
from rich import console; print = console.Console().print; from backend.core.basic_handler import file_actions; from backend.modules.admin import main as admin; from backend.core.configRead import Read; read_def = Read().get_default #
# ==============================================================================================================================================================================================================================================================================#

# ============================== Get Global Variables ==============================
runadmin = True if read_def('RunAdmin') == '1' else False # set runadmin true if 1 |
backup = file_actions.create_zip_backup # set backup to create_zip_backup function |
clearLogs = file_actions.delete_logs # set clearLogs to delete_logs function       |
log = logging # set log to logging                                                 |
color = Read().get_colors # set color to color from config file                    |
# ==================================================================================

class innit: # innit class
    def __init__(self): # innit function
        log.warning(f'Innit function is starting in file {__file__}') # log that innit function is starting
        backup() # create zip backup
        clearLogs() # delete logs
        log.warning(f'Innit function is done in file {__file__}') # log that innit function is done
        pass # pass
    
    def main(self): # main function
        log.warning(f'Main function is starting in file {__file__}') # log that main function is starting
        print(f'[bold {color("green")}]Innit is done!') # print innit is done
        log.warning(f'Main function is done in file {__file__}') # log that main function is done
        pass # pass
        
if __name__ == '__main__': # check if file is being run directly
    if runadmin is True: # if runadmin is true
        admin() # run admin module ---------------------------------------- use this only if you want to run the admin module ----------------------------------------
    innit().main() # run main function
    sys.exit() # exit
else: # if file is not being run directly
    print('This file is not meant to be imported.', style='bold red') # print error if file is imported