# scrapy-handson


## Requirements
```bash
docker 1.13.X
```

## Install && Debug
```bash
% docker build . --tag scrapy-handson

# or 
% docker pull asia.gcr.io/cyberagent-105/scrapy-handson

# Run container
% docker run --interactive --tty --volume "${PWD}:/work" scrapy-handson bash
```

## Usage
```bash
% scrapy crawl example

% scrapy crawl example -o output.json

% scrapy crawl example -o output.csv
```


## Deploy
```bash
# Login to scrapinghub.com
% shub login

# Generate eggs including libraries
% shub migrate-eggs

# Deploy to scrapinghub.com
% shub deploy
```