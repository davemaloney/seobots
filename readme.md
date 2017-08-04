# SEO Bots

This is a packaged web crawler that is meant to automate some routine functions for search engine optimization, based on the [Scrapy](https://scrapy.org/) project. It assumes the use of [Virtual Environment](https://virtualenv.pypa.io/).

Don't crawl sites without permission.

## TODO

- Need to automate all the functions listed in `seo_spider`
- Need a way to track 301 chains
- Need a way to find offsite 404s
- Identify images without alt text
- CSV column order is all over the place; need to standardize output
- Ideally all bots would run with a single command. Possible to run two spiders at once? Single output file or multiple?
- Output should overwrite, not append

## Setup

1. Confirm Python and Pip are ready to go by finding this output or equivalent
    ```
    $ which python
    /usr/local/bin/python

    $ which pip
    /usr/local/bin/pip
    ```

1. Install Virtual Environment with one of these commands
    ```
    $ pip install virtualenv

    $ sudo /usr/bin/easy_install virtualenv

    $ pip2 install virtualenv
    ```

1. Set up the virtual environment, replacing `[sandbox]` with your preferred directory
    ```
    $ virtualenv [sandbox]
    $ cd [sandbox]
    ```
1. Clone this repo
    ```
    $ git clone https://github.com/davemaloney/seobots.git
    ```
1. Activate the virtual environment
    ```
    $ source bin/activate
    ```
    (When ready to deactivate)
    ```
    $ deactivate
    ```
1. Install scrapy and enter project
    ```
    $ pip install scrapy
    $ cd seobots
    ```

## SEO Spider

To run the SEO Spider
```
$ scrapy crawl seo_spider -a startpage=http://yourdomain.com/ -a domain=yourdomain.com
```
Output to JSON or CSV with
`-o file.json` or `-o file.csv`

## Broken Links Spider

To run the Broken Links Spider
```
$ scrapy crawl link_spider -a startpage=http://yourdomain.com/ -a domain=yourdomain.com
```
Output to JSON or CSV the same way.