import time
import os
import subprocess

init = {}
new = {}


def get_current_path():
    command = 'pwd'
    run_command = subprocess.Popen(command, shell=True, universal_newlines=True, stdout=subprocess.PIPE)
    output = run_command.communicate()[0]
    return str(output[:-1])

def ls_in_path(path):
    files = os.listdir(path)
    return files

def read_all_file_contents(all_files):
    for single_file in all_files:
        opening_file = open(f'./{single_file}', 'r')
        contents_of_file = opening_file.readlines()
        init.update({single_file : contents_of_file})
        
def new_file_contents(all_files):
    for single_file in all_files:
        opening_file = open(f'./{single_file}', 'r')
        contents_of_file = opening_file.readlines()
        new.update({single_file : contents_of_file})

path = get_current_path()
ls_path = ls_in_path(path)
read_all_file_contents(ls_path)


while True:
    new_file_contents(ls_path)
    if init == new:
        time.sleep(1)
    else:
        print('something changed')
        time.sleep(1)

