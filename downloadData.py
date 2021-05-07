#!/usr/bin/env python3
import argparse
import wget

parser = argparse.ArgumentParser(description='Download data and output it with pod id.')
parser.add_argument('--url', type=str, default=100,
  help='Url to the file inside of cluster.')
args = parser.parse_args()

file_url = str(args.url)
data = wget.download(file_url,'/data.csv')

pod_name = open("/etc/hostname").read()
print(str(pod_name))
f = open("/pod.txt", 'w')
f.write(str(pod_name))
f.close()