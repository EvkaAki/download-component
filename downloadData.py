#!/usr/bin/env python3
import argparse
import wget

parser = argparse.ArgumentParser(description='Download data and output it with pod id.')
parser.add_argument('--url', type=int, default=100,
  help='Url to the file inside of cluster.')
args = parser.parse_args()

file_url = str(args.url)
data = wget.download(file_url)

pod_name = open("/etc/hostname").read()
print(str(pod_name))