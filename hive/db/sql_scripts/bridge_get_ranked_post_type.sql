DROP TYPE IF EXISTS bridge_api_post CASCADE;
CREATE TYPE bridge_api_post AS (
    id INTEGER,
    author VARCHAR,
    parent_author VARCHAR,
    author_rep BIGINT,
    root_title VARCHAR,
    beneficiaries JSON,
    max_accepted_payout VARCHAR,
    percent_hbd INTEGER,
    url TEXT,
    permlink VARCHAR,
    parent_permlink_or_category VARCHAR,
    title VARCHAR,
    body TEXT,
    category VARCHAR,
    depth SMALLINT,
    promoted DECIMAL(10,3),
    payout DECIMAL(10,3),
    pending_payout DECIMAL(10,3),
    payout_at TIMESTAMP,
    is_paidout BOOLEAN,
    children INTEGER,
    votes INTEGER,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    rshares NUMERIC,
    abs_rshares NUMERIC,
    json TEXT,
    is_hidden BOOLEAN,
    is_grayed BOOLEAN,
    total_votes BIGINT,
    sc_trend FLOAT4,
    role_title VARCHAR,
    community_title VARCHAR,
    role_id SMALLINT,
    is_pinned BOOLEAN,
    curator_payout_value VARCHAR,
    is_muted BOOLEAN
);

DROP TYPE IF EXISTS bridge_api_post_reblogs CASCADE;
CREATE TYPE bridge_api_post_reblogs AS (
    id INTEGER,
    author VARCHAR,
    parent_author VARCHAR,
    author_rep BIGINT,
    root_title VARCHAR,
    beneficiaries JSON,
    max_accepted_payout VARCHAR,
    percent_hbd INTEGER,
    url TEXT,
    permlink VARCHAR,
    parent_permlink_or_category VARCHAR,
    title VARCHAR,
    body TEXT,
    category VARCHAR,
    depth SMALLINT,
    promoted DECIMAL(10,3),
    payout DECIMAL(10,3),
    pending_payout DECIMAL(10,3),
    payout_at TIMESTAMP,
    is_paidout BOOLEAN,
    children INTEGER,
    votes INTEGER,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    rshares NUMERIC,
    abs_rshares NUMERIC,
    json TEXT,
    is_hidden BOOLEAN,
    is_grayed BOOLEAN,
    total_votes BIGINT,
    sc_trend FLOAT4,
    role_title VARCHAR,
    community_title VARCHAR,
    role_id SMALLINT,
    is_pinned BOOLEAN,
    curator_payout_value VARCHAR,
    reblogged_by VARCHAR[]
);
