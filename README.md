# words
## Overview
- The URL Parser Tool is designed to parse URLs from standard input (stdin), extract unique directory names and parameters, and generate two separate wordlists: one for directory names (directory-wordlist.txt) and another for parameters (parameter-wordlist.txt).
## Installation
1. Clone the repository:
```
git clone https://github.com/emre-bi/words.git
cd words
```
## Example Usage
```
cat urls.txt | python app.py
```
```
cat urls.txt | python app.py -d dir.txt -p par.txt
```
## Example Output
- Consider the following urls.txt file:
```
https://example.com/dir1/page?param1=value1
https://example.com/dir2/page?param2=value2
https://example.com/dir1/page?param3=value3
```
- Running the tool:
```
cat urls.txt | python app.py
```
- tool Produces two wordlists:
- directory-wordlist.txt:
```
dir1
dir2
page
```
- parameter-wordlist.txt:
```
param1
param2
param3
```
