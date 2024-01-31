import os
import sys
import shutil
import yaml

class Case():
    """
    Class for generic case setup: folder structure creation, write input files, 
    etc.
    """
    def __init__(self, nblocks=1):
        self.nblocks = nblocks

    def create_folder_structure(self, name, path):
        """
        Within the parent folder create:
            - main_name;
            - input_name;
            - output_name;
        """
        if path == '.':
            path = './'
        self.name = name
        self.path = path
        try:
            # Create folders
            os.makedirs(path + f'main_{name}')
            os.makedirs(path + f'input_{name}')
            os.makedirs(path + f'output_{name}')
            # Create absolute paths for each folder
            with open(path + f'main_{name}/paths.yml', 'w') as f:
                abs_path_main = os.path.abspath(path + f'main_{name}') 
                paths = {
                    'main'  : abs_path_main,
                    'input' : f'{abs_path_main}/../input_{name}',
                    'output': f'{abs_path_main}/../output_{name}',
                }
                yaml.dump(paths, f)
            # Create softlink of pre_wrapper driver file
            pre_path = os.environ['PRE_PATH'] 
            os.symlink(pre_path + '/pre.py', abs_path_main + '/pre.py')
        except FileExistsError:
            print('Folder structure already exists.')

    def create_base_inputfile(self):
        pre_path = os.environ['PRE_PATH'] 
        shutil.copy(f'{pre_path}/src/files/inputfile.yml', 
                    f'{self.path}/input_{self.name}')

