#!/bin/bash
while read l ; do fields=$(echo $line | tr -dc ',' | wc -c); ((fields <= 9)) && echo $l; done < /tmp/courses.csv > cl_courses.csv
cat /tmp/groups.csv | cut -d',' -f 1-3 > cl_groups.csv
