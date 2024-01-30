import numpy as np

class Grid():
    """
    Grid related class for: grid generation, etc
    """
    def __init__(self, inputs):
        """
        Parameters:
        -----------
        dict inputs ... dictionary with settings from inputfile
        """
        self.inputs = inputs

    def create_carterian_grid(self):
        # Obtain information from dict for easier referencing
        domain = self.inputs['domain']
        # Number of nodes
        nx     = domain['nx']
        ny     = domain['ny']
        nz     = domain['nz']
        # Domain length
        Lx     = domain['Lx']
        Ly     = domain['Ly']
        Lz     = domain['Lz']
        # Leftmost origin
        xstart = domain['xstart']
        ystart = domain['ystart']
        zstart = domain['zstart']
        print('here')
