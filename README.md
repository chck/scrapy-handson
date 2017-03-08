# scrapy-handson


## Requirements
```bash
docker 17.03.X
```

## Install && Run
```bash
# Pull image
% docker pull asia.gcr.io/cyberagent-105/chck/scrapy-handson

# Set tag alias
% docker tag asia.gcr.io/cyberagent-105/chck/scrapy-handson scrapy-handson

# Check it out!!
% docker images

# Run container
% docker run --interactive --tty --volume "${PWD}:/work" scrapy-handson

# Check it out!!
% docker ps

# Enter the container
% docker exec --interactive --tty $CONTAINER_ID bash
```

## Let's start
```bash
% scrapy startproject my_crawler

% cd my_crawler && scrapy genspider example example.com

% vim my_crawler/spiders/example.py

% scrapy runspider example.py

% vim my_crawler/items.py

% scrapy crawl example

% scrapy crawl example -o output.json

% scrapy crawl example -o output.csv
```


## Deploy
```bash
# Login to scrapinghub.com
% shub login

# Create project on your browser (and copy PROJECT_ID)
% open https://app.scrapinghub.com/

# Deploy to scrapinghub.com to generate `scrapinghub.yaml`
% shub deploy

# Generate eggs to generate `setup.py` and `requirements.txt`
% shub migrate-eggs

# Add dependencies
% cat ../requirements.txt >> requirements.txt

# Re-Deploy to scrapinghub.com including dependencies
% shub deploy
```

## Cleanup
```bash
% docker ps

% docker stop $CONTAINER_ID

% docker rm $CONTAINER_ID

% docker ps -a | grep $CONTAINER_ID

% docker rmi scrapy-handson

% docker images | grep scrapy-handson

# Many thanks!!
```
