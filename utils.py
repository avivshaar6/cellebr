import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Mors translator app')
    parser.add_argument("-p", "--port", help="app port")
    args = parser.parse_args()
    return args