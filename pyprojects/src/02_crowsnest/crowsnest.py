#!/usr/bin/env python3
"""
Crow's Nest -- choose the correct article
"""

import argparse


def main():
    """Get a word from the command line and announce it with the proper article"""
    
    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('str', metavar='word', help='A word')
    
    args = parser.parse_args()
    
    word = args.str
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


if __name__ == '__main__':
    main()