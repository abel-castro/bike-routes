# Bike routes
Django project that displays bike routes in a map.

**Features:**
- provide an REST-API with CRUD operations with routes
- show routes in a map
- import routes from a JSON file

![Screenshot_1](https://github.com/abel-castro/bike-routes/blob/main/screenshot_1.png)
![Screenshot_2](https://github.com/abel-castro/bike-routes/blob/main/screenshot_2.png)

## Setup
1. Create a .env file with help of the env_template_dev file. In order to use the maps you will need a Maptiler API key. You can get one here https://cloud.maptiler.com/maps/.
2. Build the development image with `docker-compose build`
3. Import some routes
```
docker-compose run --rm django python manage.py import_routes data/routes_to_import.json 
```
4. Run `docker-compose up` and go to http://0.0.0.0:8000


## API 
Provided endpoints:

`api/routes/` 
- GET: fetch all routes
- POST: create a new route
    - name: String, optional
    - data: JSON  

`api/routes/<route-id>` 
- GET: retrieve routes data
- DELETE: delete a route


## Other commands
**Run the tests**
```
docker-compose run --rm django pytest
```
**'Log in' in the django container**
```
docker-compose run --rm django bash
```

## Sources
- Sample images from [wikimedia commons](https://commons.wikimedia.org/wiki/Land_Salzburg)
- [MapLibre Add a GeoJSON Line](https://maplibre.org/maplibre-gl-js-docs/example/geojson-line/)

--- 

Created with [Django Docker Starter Template](https://github.com/abel-castro/ddst).
