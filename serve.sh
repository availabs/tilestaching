#!/bin/bash

rm -rf ./stache

gunicorn -c gunicorn.cfg.py 'TileStache:WSGITileServer("tilestache.cfg")'