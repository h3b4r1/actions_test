import sys
import os
import argparse

def main():
    '''some code to show the use of argparse by dispalying the linux system information'''
    arg_parser = argparse.ArgumentParser(description='Display the system information')
    arg_parser.add_argument('-o', '--os', action='store_true', help='Display the OS information')
    arg_parser.add_argument('-m', '--memory', action='store_true', help='Display the memory information')
    arg_parser.add_argument('-c', '--cpu', action='store_true', help='Display the CPU information')
    arg_parser.add_argument('-n', '--network', action='store_true', help='Display the network information')
    arg_parser.add_argument('-a', '--all', action='store_true', help='Display all the information')
    args = arg_parser.parse_args()
    if len(sys.argv) != 2:
        arg_parser.print_help()
        sys.exit(1)
    if args.os:
        os.system('uname -a')
    if args.memory:
        os.system('free -m')
    if args.cpu:    
        os.system('lscpu')
    if args.network:
        os.system('ifconfig')
    if args.all:
        os.system('uname -a')
        os.system('free -m')
        os.system('lscpu')
        os.system('ifconfig')

if __name__ == "__main__":
    main()