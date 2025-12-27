#!/usr/bin/bash

if [ -z "${VIRTUAL_ENV_PROMPT}" ]; then
    if [ -f ".venv/bin/activate" ]; then
        source .venv/bin/activate
    else
        echo "venv not found: .venv" >&2
    fi
fi

python3 app.py $@
