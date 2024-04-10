#!/bin/bash
cd /var/www/reports.openstreetmap.ie
echo "fetching the latest .... "
mkdir -p /var/www/reports.openstreetmap.ie/data
s3cmd get --force s3://osmie-tiles/reports/* /var/www/reports.openstreetmap.ie
s3cmd get --force s3://osmie-tiles/reports/data/* /var/www/reports.openstreetmap.ie/data
