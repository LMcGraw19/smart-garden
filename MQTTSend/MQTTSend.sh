#!/usr/bin/env bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
mosquitto_pub -d -h <IP ADDRESS> -u <USERNAME> -p 8883 -P <PASSWORD> -t <PATH/TO/PLACE> --cafile </PATH/TO/CERT/FILE> --insecure -f </PATH/TO/FILE>