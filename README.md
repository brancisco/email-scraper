# W2E

#### Website 2 email

---

Scrape pattern from list of websites

---

## How To

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
python3 scraper.py
```

### trouble shooting

Make sure that the scraper.py has execute and write permissions.

## Goal

The goal of this will be to run a script on a file containing a list of websites. The script will go to the website and crawl it searching for a list of patterns.

in the future a format to run the script with might look like:

```
w2e (-p somepattern) (file )
```