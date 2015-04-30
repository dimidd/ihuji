#!/bin/bash
while read l ; do fields=$(echo $line | tr -dc ',' | wc -c); ((fields <= 9)) && echo $l; done < /tmp/courses.csv > cl_courses.csv
