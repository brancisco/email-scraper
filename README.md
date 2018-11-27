# W2E

#### Website 2 email

---

Scrape pattern from list of websites

---

## How To

### Setting up, and running the script
Create a file in this directory called `websites.txt`

The format of this file should be a single website perline:

```
somewebsite.com
someotherwebsite.com
.
.
.
somelastwebsite.com
```

+ Capitalization does not matter
+ Should not include http / https / www

run the script with:

```
python3 email_scraper.py
```

### output

The output format is

```
0 url []
1 url []
2 url [some@email.com]
.
.
i url ERR
.
.
n url [someother@email.com]
```

+ `[]` means there were no emails found on that website
+ `[some@email.com, ...]` list of emails found
+ `ERR` means there was some error trying to load the website 

### trouble shooting

Make sure that the scraper.py has execute and write permissions.

## Features

Follows links that have the word *"Contact"* in them

## Goal

The goal of this will be to run a script on a file containing a list of websites. The script will go to the website and crawl it searching for a list of patterns.

in the future a format to run the script with might look like:

```
w2e (-p somepattern) (file )
```