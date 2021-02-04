# Clickjacking Tester

A python script designed to check if the website is vulnerable of clickjacking and saves the result into .txt file.

### Usage

```
python3 clickjack.py <file_name>
```

### Example

##### Input

```
python3 clickjack.py sites.txt
```

##### sites.txt

```
www.bugcrowd.com
www.srsecure.xyz
```

##### Output

```
[-] www.bugcrowd.com is not vulnerable to ClickJacking
[+] www.srsecure.xyz is vulnerable to ClickJacking
```
