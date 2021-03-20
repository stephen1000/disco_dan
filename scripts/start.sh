#!/usr/bin/env bash

# Load secrets from /run
export DISCO_DAN_CONNECTION_STRING=$(cat /run/secrets/disco_dan_conn_str)
export TEST_CONNECTION_STRING=$(cat /run/secrets/test_conn_str)


# Creates necessary tables in specified db
echo "SELECT 'CREATE DATABASE disco_dan' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'disco_dan')\gexec" | psql
echo "SELECT 'CREATE DATABASE disco_dan_test' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'disco_dan_test')\gexec" | psql
disco_dan initdb

# Initiates the discord bot
disco_dan run
