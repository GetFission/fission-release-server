#!/bin/bash
set -e

python -m smtpd -n -c DebuggingServer localhost:1025
