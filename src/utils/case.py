import os

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
        try:
            os.makedirs(path + f'main_{name}')
            os.makedirs(path + f'input_{name}')
            os.makedirs(path + f'output_{name}')
        except FileExistsError:
            print('Folder structure already exists.')
