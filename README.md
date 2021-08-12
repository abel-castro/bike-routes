# Bike routes


## Setup
1. Create a .env file with help of the env_template_dev file. In order to use the maps you will need a Maptiler API key. You can get one here https://cloud.maptiler.com/maps/.
2. Build the development image with `docker-compose build`
3. Import some routes
```
docker-compose run --rm django python manage.py import_routes data/routes_to_import.json 
```
4. Run `docker-compose up` and go to http://0.0.0.0:8000


## Other commands
**Run the tests**
```
docker-compose run --rm django pytest
```

## Sources
Sample images from [wikimedia commons](https://commons.wikimedia.org/wiki/Land_Salzburg)

--- 

Created with [Django Docker Starter Template](https://github.com/abel-castro/ddst).
