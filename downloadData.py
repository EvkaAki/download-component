import argparse
import wget

parser = argparse.ArgumentParser(description='Download data and output it with pod id.')
parser.add_argument('--url', type=str, default=100,
  help='Url to the file inside of cluster.')
parser.add_argument("--pod-path", type=str, help="Path to store URI output")

args = parser.parse_args()
podPath = args.pod_path

file_url = str(args.url)
data = wget.download(file_url,'/data.csv')
pod = open("/etc/hostname").read()
print(str(pod))

print(podPath)
f = open(podPath, 'w+')
f.write(str(pod))
f.close()