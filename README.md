# Installation

## System dependencies
``` bash
sudo apt-get update
sudo apt-get install gunicorn tilestache python-pil python-shapely
sudo pip install mapbox mapbox_vector_tile
```

## Starting the server
``` bash
git clone https://github.com/availabs/tilestaching.git
cd tilestaching/

gunicorn 'TileStache:WSGITileServer("tilestache.cfg")' -c gunicorn.cfg.py
```

