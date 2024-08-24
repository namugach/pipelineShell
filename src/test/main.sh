#!/bin/bash
SCRIPT_PATH=$(dirname "$(realpath "$0")")
SCRIPT_NAME=$(basename "$0")
SCRIPT_NAME_NO_EXT="${SCRIPT_NAME%.*}"
python "$SCRIPT_PATH/$SCRIPT_NAME_NO_EXT.py"