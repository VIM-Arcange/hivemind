#!/bin/bash

set -euo pipefail

collect_stats() {

    echo "Collecting statistics from database ${HIVEMIND_DB_NAME}"

    mkdir -p pg-stats
    DIR=$PWD/pg-stats

    PGPASSWORD=${POSTGRES_PASSWORD} psql \
        --username "${POSTGRES_USER}" \
        --host ${POSTGRES_HOST} \
        --port ${POSTGRES_PORT} \
        --dbname ${HIVEMIND_DB_NAME} << EOF
\timing
\copy (select * from pg_settings) to '$DIR/pg_settings.csv' WITH CSV HEADER
\copy (select * from pg_stat_user_tables) to '$DIR/pg_stat_user_tables.csv' WITH CSV HEADER

-- Disabled, because this table is too big.
--\copy (select * from pg_stat_statements) to '$DIR/pg_stat_statements.csv' WITH CSV HEADER

-- See https://github.com/powa-team/pg_qualstats
\echo pg_qualstats index advisor
SELECT v
  FROM json_array_elements(
    pg_qualstats_index_advisor(min_filter => 50)->'indexes') v
  ORDER BY v::text COLLATE "C";

\echo pg_qualstats unoptimised
SELECT v
  FROM json_array_elements(
    pg_qualstats_index_advisor(min_filter => 50)->'unoptimised') v
  ORDER BY v::text COLLATE "C";
EOF

}

collect_stats