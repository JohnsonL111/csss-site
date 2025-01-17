#!/bin/bash

set -e -o xtrace

git checkout master


if [ -z "${DB_CONTAINER_NAME}" ]; then
	echo "DB_CONTAINER_NAME is not set, exiting."
	exit 1
fi

function setup_website_db {
  docker run --name "${DB_CONTAINER_NAME}" -p "${DB_PORT}":5432 -it -d -e POSTGRES_PASSWORD="${DB_PASSWORD}" postgres:alpine || true
  wait_for_postgres_db
  docker exec "${DB_CONTAINER_NAME}" psql -U postgres -d postgres -c "DROP DATABASE \"${DB_NAME}\";" || true
  docker exec "${DB_CONTAINER_NAME}" psql -U postgres -d postgres -c "CREATE DATABASE \"${DB_NAME}\" OWNER postgres;" || true
}

function wait_for_postgres_db {
  # aquired from https://docs.docker.com/compose/startup-order/
  until PGPASSWORD=$DB_PASSWORD psql -h localhost -p "${DB_PORT}" -U "postgres" -c '\q'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
  done

  >&2 echo "Postgres is up"
}

function applying_master_db_migrations {
  python3 manage.py migrate
  rm *.json* || true
  if [ -z "${CHANGE_ID}" ]; then
    wget -r --no-parent -nd https://dev.sfucsss.org/dev_csss_website_media/fixtures/ -A 'json'
  else
    cp /mnt/dev_csss_website_media/fixtures/* .
  fi
  python3 manage.py loaddata *.json
  rm *.json* || true
}


setup_website_db
applying_master_db_migrations

git checkout -
