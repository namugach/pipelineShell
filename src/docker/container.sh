#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

if [ $# -lt 1 ]; then
	echo "Usage: $0 <command> [options]"
	exit 1
fi

python "$SCRIPT_DIR/container.py" "$@"
