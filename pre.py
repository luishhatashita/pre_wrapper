#!/usr/bin/env python

import argparse

def initialize_parser(parser):
    parser.add_argument("-c", "--create", nargs='+',
                        help="Utility to create folder structure")
    str_utils = ''' 
        Select from the available utils: create_domain, create_connectivity, 
        create_bcs, etc...
    ''' 
    parser.add_argument("-u", "--utils", nargs='+',
                        help=str_utils)
    #parser.add_argument("-g", "--grid" , 
    #                    help="Select between the following grid methods")

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
        from src.utils.case import Case
        case = Case()
        name = args.create[0]
        path = args.create[1]
        case.create_folder_structure(name, path)
        case.create_base_inputfile()
    elif args.utils:
        print('utils')
    elif args.grid:
        print('grid')
