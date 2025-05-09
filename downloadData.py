import argparse
import urllib.request
import os

parser = argparse.ArgumentParser(description='Download data and output it with pod id.')
parser.add_argument('--url', type=str, default=100,
  help='Url to the file inside of cluster.')
parser.add_argument("--pod-path", type=str, help="Path to store URI output")
parser.add_argument("--data-path", type=str, help="Path to store DATA output")

args = parser.parse_args()
pod_path = args.pod_path

pod = open("/etc/hostname").read()
print(str(pod))


print("Pod path " + pod_path)
if not os.path.exists(os.path.dirname(pod_path)):
    os.makedirs(os.path.dirname(pod_path))
f = open(pod_path, 'w+')
f.write(str(pod))
f.close()


data_path = args.data_path
file_url = str(args.url)
if not os.path.exists(os.path.dirname(data_path)):
    os.makedirs(os.path.dirname(data_path))

urllib.request.urlretrieve(file_url, data_path)
