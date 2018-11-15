# W2E

#### Website 2 email

---

Scrape pattern from list of websites

---

## How To

Create a file in this directory called `websites.txt`

The format of this file should be:

```
somewebsite.com
someotherwebsite.com
```

+ Capitalization does not matter
+ Should not include http / https / www

## Goal

The goal of this will be to run a script on a file containing a list of websites. The script will go to the website and crawl it searching for a list of patterns.

run the script with:

```
w2e (-p somepattern) (file )
```