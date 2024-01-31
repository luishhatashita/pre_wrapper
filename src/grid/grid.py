import numpy as np

class Grid():
    """
    Grid related class for: grid generation, etc
    """
    def __init__(self, paths, inputs):
        """
        Parameters:
        -----------
        dict paths  ... dictionary with absolute paths to each folder 
        dict inputs ... dictionary with settings from inputfile
        """
        self.paths  = paths
        self.inputs = inputs

    def create_cartesian_grid(self):
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
        # Domain
        x      = np.linspace(xstart, xstart+Lx, nx) 
        y      = np.linspace(ystart, ystart+Ly, ny) 
        z      = np.linspace(zstart, zstart+Lz, nz) 
        grid_x, grid_y, grid_z = np.meshgrid(x, y, z)
        stack  = np.zeros((nx*ny*nz, 3))
        for k in range(nz):
            for j in range(ny):
                for i in range(nx):
                    stack[i+nx*(j+ny*k), 0] = x[i]
                    stack[i+nx*(j+ny*k), 1] = y[j]
                    stack[i+nx*(j+ny*k), 2] = z[k]
        # CSV implementation
        header = 'x_coord, y_coord, z_coord'
        np.savetxt(
            self.paths['input']+'/grid.csv', stack, 
            delimiter = ",", header=header,
        )
        # TODO:
        # - vtk xml version
        # - or try hdf5 and xdmf files 

class Domain():

    def __init__(self):
        print('domain')
