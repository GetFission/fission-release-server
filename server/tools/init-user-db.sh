#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER electronfission WITH PASSWORD 'password' CREATEDB;
    CREATE DATABASE electronfissiondev_dev;
    GRANT ALL PRIVILEGES ON DATABASE electronfission_dev TO electronfission;
EOSQL
