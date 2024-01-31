#!/usr/bin/env python

import argparse
import yaml

def initialize_parser(parser):
    parser.add_argument("-c", "--create", nargs='+',
                        help="Utility to create folder structure")
    str_utils = ''' 
        Select from the available utilities: ..., create_connectivity, 
        create_bcs, etc...
    ''' 
    parser.add_argument("-u", "--utils", nargs='+', help=str_utils)
    str_grid = ''' 
        Select from the available grid utilities: create_cartesian_grid, etc...
    ''' 
    parser.add_argument("-g", "--grid" , help=str_grid)

def create_case(name, path):
    from src.utils.case import Case
    case = Case()
    case.create_folder_structure(name, path)
    case.create_base_inputfile()

def utils_map(function):
    utils_available = {
        'create_cartesian_grid': 'uniform',
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    initialize_parser(parser)
    args   = parser.parse_args()
    if args.create:
        if len(args.create) < 2:
            raise Exception(
                'Please provide the case name and path for the folder '\
                'structure, respectively.'
            )
        name = args.create[0]
        path = args.create[1]
        create_case(name, path)
    elif args.utils:
        with open('./paths.yml', 'r') as f1:
            paths = yaml.safe_load(f1)
    elif args.grid:
        with open('./paths.yml', 'r') as f1:
            paths = yaml.safe_load(f1)
        if args.grid == 'create_cartesian_grid':
            with open(f"{paths['input']}/inputfile.yml", 'r') as f2:
                inputs = yaml.safe_load(f2)
            from src.grid.grid import Grid
            grid = Grid(paths, inputs)
            grid.create_cartesian_grid()
