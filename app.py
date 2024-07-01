from urllib.parse import urlparse, parse_qs
import tldextract
import argparse
import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)

unique_paths_subd = set()
unique_params = set()


#### Take User Input ####
parser = argparse.ArgumentParser(description="Prepare wordlist from provided urls and save to file")
parser.add_argument('-d', '--directory', type=str, help='output file for directory wordlist. If not provided; will be saved in the current directory with the name directory-wordlist.txt')
parser.add_argument('-p', '--paramater', type=str, help="output file for paramater wordlist. If not provided; will be saved in the current directory with the name parameter-wordlist.txt")
parser.usage = """app.py [-h] [url1 ...] -p -d
Examples:
    cat urls | python3 app.py -p param.txt -d dir.txt
"""
args = parser.parse_args()

if sys.stdin.isatty():
    logger.error("Warning: No urls provided as input. Exiting.")
    sys.exit(1)
else:
    urls = [line.strip() for line in sys.stdin.readlines()]


# Parse URLs
for url in urls:
    parsed_url = urlparse(url)
    
    # Extract and store path components, also subdomain names
    path_components = parsed_url.path.strip('/').split('/')
    for component in path_components:
        if component:
            unique_paths_subd.add(component)
    
    extracted = tldextract.extract(parsed_url.subdomain)
    subdomain_names = extracted.subdomain.split('.')
    for subdomain_name in subdomain_names:
        unique_paths_subd.add(subdomain_name)

    # Extract and store query parameters
    query_params = parse_qs(parsed_url.query)
    for param in query_params.keys():
        unique_params.add(param)

if args.directory:
    dir_file = args.d
else:
    dir_file = "directory-wordlist.txt"
with open(dir_file, 'w') as dir_file:
    for path in sorted(unique_paths_subd):
        dir_file.write(path + '\n')


if args.paramater:
    param_file = args.p
else:
    param_file = "paramater-wordlist.txt"
with open(param_file, 'w') as param_file:
    for param in sorted(unique_params):
        param_file.write(param + '\n')
