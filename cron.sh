#!/bin/bash
cd /var/www/reports.openstreetmap.ie
echo "fetching the latest .... "
s3cmd get --force s3://osmie-tiles/reports/* /var/www/reports.openstreetmap.ie
