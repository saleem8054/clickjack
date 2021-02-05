# Clickjacking Tester

A python script designed to check if the website is vulnerable of clickjacking and saves the result into Vulnerable.txt file.

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
www.developer.pubg.com
```

##### Output

```
[-] www.bugcrowd.com is not Vulnerable
[+] www.srsecure.xyz is Vulnerable
[+] www.developer.pubg.com is Vulnerable
```
