#!/usr/bin/env python3
"""
navinetworkx
"""
import argparse

def main():
    """
    entry point
    """
    parser = argparse.ArgumentParser(description='do something')
    parser.add_argument('--compact-json', action='store_true', help='Generate Compact JSON')
    args = parser.parse_args()
    print("ha ha")

if __name__ == "__main__":
    main()
