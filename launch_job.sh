#!/usr/bin/env bash
spark-submit --master "local[*]" --py-files dist/jobs.zip dist/main.py --job analyzer