#!/bin/bash
# get ip map of the containers

SCRIPT_DIR=$(dirname "$(realpath "$0")")

ip_map() {
    SERVICES=$(docker compose -f "$1" config --services)
    
    for srv in $SERVICES; do
        (
            cnt=$(docker compose -f "$1" ps "$srv" --format '{{.Names}}')
            [ -n "$cnt" ] &&
            docker inspect $cnt | jq -r "[\"$srv\", .[].NetworkSettings.Networks[].IPAddress] | @sh"
        )&
    done
}

ip_map "$SCRIPT_DIR/../core.yaml"
ip_map "$SCRIPT_DIR/../ran.yaml"
wait
