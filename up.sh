#!/bin/bash

gunicorn 'TileStache:WSGITileServer("tilestache.cfg")' -c gunicorn.cfg.py
