#!/bin/bash
# gets the veth interface name of a specific service to allow sniffing traffic
# example: `get_veth.sh upf`

SERVICE=${1:-upf}
CONTAINER=$(docker container list | grep $SERVICE | cut -f 1 -d " ")

if [ -z $CONTAINER ]; then
    echo "Cannot find container matching $SERVICE"
    exit 1
fi

IFINDEX=$(docker exec $CONTAINER cat /sys/class/net/eth0/iflink)

for if in /sys/class/net/*; do
    idx=$(cat $if/ifindex)

    if [[ $idx -eq $IFINDEX ]] ; then 
        echo $IFINDEX
        echo $if
        exit 
    fi
done
