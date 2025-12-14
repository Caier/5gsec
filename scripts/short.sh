#!/bin/bash
# a group of alias commands for faster interfacing with docker
# `source short.sh`

_assign_short_names__() {
    local SCRIPT_DIR;
    SCRIPT_DIR=$(dirname "$(realpath "$1")")

    alias dcc="docker compose -f \"$SCRIPT_DIR/../core.yaml\""
    alias dcr="docker compose -f \"$SCRIPT_DIR/../ran.yaml\""
    alias df5="docker compose -f \"$SCRIPT_DIR/../free5gc.yaml\""
}

_assign_short_names__ "$0"
unset -f _assign_short_names__