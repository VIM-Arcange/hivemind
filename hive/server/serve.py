# -*- coding: utf-8 -*-
"""Hive JSON-RPC API server."""
<<<<<<< HEAD
=======
from logging import Logger
from hive.server.database_api.methods import find_votes, list_votes
>>>>>>> Fix for issue #65
import os
import sys
import logging
import time

from datetime import datetime
from sqlalchemy.exc import OperationalError
from aiohttp import web
from jsonrpcserver.methods import Methods
from jsonrpcserver import async_dispatch as dispatch

import simplejson

from hive.server.condenser_api import methods as condenser_api
from hive.server.condenser_api.tags import get_trending_tags as condenser_api_get_trending_tags
from hive.server.condenser_api.get_state import get_state as condenser_api_get_state
from hive.server.condenser_api.call import call as condenser_api_call
from hive.server.common.mutes import Mutes

from hive.server.bridge_api import methods as bridge_api
from hive.server.bridge_api.thread import get_discussion as bridge_api_get_discussion
from hive.server.bridge_api.support import normalize_post as bridge_api_normalize_post
from hive.server.bridge_api.support import get_post_header as bridge_api_get_post_header
from hive.server.hive_api import community as hive_api_community
from hive.server.hive_api import notify as hive_api_notify
from hive.server.hive_api import stats as hive_api_stats
from hive.server.hive_api.public import get_info as hive_api_get_info

from hive.server.follow_api import methods as follow_api
from hive.server.tags_api import methods as tags_api

from hive.server.database_api import methods as database_api

from hive.server.db import Db

# pylint: disable=too-many-lines

def decimal_serialize(obj):
    return simplejson.dumps(obj=obj, use_decimal=True)

def decimal_deserialize(s):
    return simplejson.loads(s=s, use_decimal=True)

async def db_head_state(context):
    """Status/health check."""
    db = context['db']
    sql = ("SELECT num, created_at, extract(epoch from created_at) ts "
           "FROM hive_blocks ORDER BY num DESC LIMIT 1")
    row = await db.query_row(sql)
    return dict(db_head_block=row['num'],
                db_head_time=str(row['created_at']),
                db_head_age=int(time.time() - row['ts']))

def build_methods():
    """Register all supported hive_api/condenser_api.calls."""
    # pylint: disable=expression-not-assigned, line-too-long
    methods = Methods()

    methods.add(**{'hive.' + method.__name__: method for method in (
        db_head_state,
    )})

    methods.add(**{'hive.get_info' : hive_api_get_info})

    methods.add(**{'condenser_api.' + method.__name__: method for method in (
        condenser_api.get_followers,
        condenser_api.get_following,
        condenser_api.get_follow_count,
        condenser_api.get_content,
        condenser_api.get_content_replies,
        condenser_api_get_state,
        condenser_api_get_trending_tags,
        condenser_api.get_discussions_by_trending,
        condenser_api.get_discussions_by_hot,
        condenser_api.get_discussions_by_promoted,
        condenser_api.get_discussions_by_created,
        condenser_api.get_discussions_by_blog,
        condenser_api.get_discussions_by_feed,
        condenser_api.get_discussions_by_comments,
        condenser_api.get_replies_by_last_update,

        condenser_api.get_discussions_by_author_before_date,
        condenser_api.get_post_discussions_by_payout,
        condenser_api.get_comment_discussions_by_payout,
        condenser_api.get_blog,
        condenser_api.get_blog_entries,
        condenser_api.get_account_reputations,
        condenser_api.get_reblogged_by,
        condenser_api.get_active_votes
    )})

    # dummy methods -- serve informational error
    methods.add(**{
        'condenser_api.get_account_votes': condenser_api.get_account_votes,
        'tags_api.get_account_votes': condenser_api.get_account_votes,
    })

    # follow_api aliases
    methods.add(**{
        'follow_api.get_followers': condenser_api.get_followers,
        'follow_api.get_following': condenser_api.get_following,
        'follow_api.get_follow_count': condenser_api.get_follow_count,
        'follow_api.get_account_reputations': follow_api.get_account_reputations,
        'follow_api.get_blog': condenser_api.get_blog,
        'follow_api.get_blog_entries': condenser_api.get_blog_entries,
        'follow_api.get_reblogged_by': condenser_api.get_reblogged_by,
        'follow_api.get_feed_entries': follow_api.get_feed_entries,
        'follow_api.get_feed': follow_api.get_feed,
        'follow_api.get_blog_authors': follow_api.get_blog_authors
    })

    # tags_api aliases
    methods.add(**{
        'tags_api.get_discussion': tags_api.get_discussion,
        'tags_api.get_content_replies': tags_api.get_content_replies,
        'tags_api.get_discussions_by_trending': condenser_api.get_discussions_by_trending,
        'tags_api.get_discussions_by_hot': condenser_api.get_discussions_by_hot,
        'tags_api.get_discussions_by_promoted': condenser_api.get_discussions_by_promoted,
        'tags_api.get_discussions_by_created': condenser_api.get_discussions_by_created,
        'tags_api.get_discussions_by_blog': condenser_api.get_discussions_by_blog,
        'tags_api.get_discussions_by_comments': condenser_api.get_discussions_by_comments,
        'tags_api.get_discussions_by_author_before_date': condenser_api.get_discussions_by_author_before_date,
        'tags_api.get_post_discussions_by_payout': condenser_api.get_post_discussions_by_payout,
        'tags_api.get_comment_discussions_by_payout': condenser_api.get_comment_discussions_by_payout,
        'tags_api.get_active_votes' : tags_api.get_active_votes,
        'tags_api.get_tags_used_by_author' : tags_api.get_tags_used_by_author,
        'tags_api.get_discussions_by_active' : tags_api.get_discussions_by_active,
        'tags_api.get_discussions_by_cashout' : tags_api.get_discussions_by_cashout,
        'tags_api.get_discussions_by_votes' : tags_api.get_discussions_by_votes,
        'tags_api.get_discussions_by_children' : tags_api.get_discussions_by_children
    })

    # legacy `call` style adapter
    methods.add(**{
        'call': condenser_api_call
    })

    # bridge_api methods
    methods.add(**{'bridge.' + method.__name__: method for method in (
        bridge_api_normalize_post,
        bridge_api_get_post_header,
        bridge_api_get_discussion,
        bridge_api.get_post,
        bridge_api.get_account_posts,
        bridge_api.get_ranked_posts,
        bridge_api.get_profile,
        bridge_api.get_trending_topics,
        bridge_api.get_relationship_between_accounts,
        bridge_api.get_follow_list,
        bridge_api.does_user_follow_any_lists,
        hive_api_notify.post_notifications,
        hive_api_notify.account_notifications,
        hive_api_notify.unread_notifications,
        hive_api_stats.get_payout_stats,
        hive_api_community.get_community,
        hive_api_community.get_community_context,
        hive_api_community.list_communities,
        hive_api_community.list_pop_communities,
        hive_api_community.list_community_roles,
        hive_api_community.list_subscribers,
        hive_api_community.list_all_subscriptions,
    )})

    # database_api methods
    methods.add(**{
        'database_api.list_comments' : database_api.list_comments,
        'database_api.find_comments' : database_api.find_comments,
        'database_api.list_votes' : database_api.list_votes,
        'database_api.find_votes' : database_api.find_votes
    })

    return methods

def truncate_response_log(logger):
    """Overwrite jsonrpcserver resp logger to truncate output.

    https://github.com/bcb/jsonrpcserver/issues/65 was one native
    attempt but helps little for more complex response structs.

    See also https://github.com/bcb/jsonrpcserver/issues/73.
    """
    formatter = logging.Formatter('%(levelname)s:%(name)s:%(message).1024s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger.propagate = False
    logger.addHandler(handler)

def run_server(conf):
    """Configure and launch the API server."""
    #pylint: disable=too-many-statements

    # configure jsonrpcserver logging
    log_level = conf.log_level()
    logging.getLogger('aiohttp.access').setLevel(logging.WARNING)
    logging.getLogger('jsonrpcserver.dispatcher.response').setLevel(log_level)
    truncate_response_log(logging.getLogger('jsonrpcserver.dispatcher.request'))
    truncate_response_log(logging.getLogger('jsonrpcserver.dispatcher.response'))

    # init
    log = logging.getLogger(__name__)
    methods = build_methods()

    mutes = Mutes(conf.get('muted_accounts_url'), conf.get('blacklist_api_url'))
    Mutes.set_shared_instance(mutes)

    app = web.Application()
    app['config'] = dict()
    app['config']['args'] = conf.args()
    app['config']['hive.MAX_DB_ROW_RESULTS'] = 100000
    #app['config']['hive.logger'] = logger

    async def init_db(app):
        """Initialize db adapter."""
        args = app['config']['args']
        app['db'] = await Db.create(args['database_url'])

    async def close_db(app):
        """Teardown db adapter."""
        app['db'].close()
        await app['db'].wait_closed()

    async def show_info(app):
        sql = "SELECT num FROM hive_blocks ORDER BY num DESC LIMIT 1"
        database_head_block = await app['db'].query_one(sql)

        from hive.version import VERSION, GIT_REVISION
        log.info("hivemind_version : %s", VERSION)
        log.info("hivemind_git_rev : %s", GIT_REVISION)

        from hive.db.schema import DB_VERSION as SCHEMA_DB_VERSION
        log.info("database_schema_version : %s", SCHEMA_DB_VERSION)
        
        log.info("database_head_block : %s", database_head_block)

    app.on_startup.append(init_db)
    app.on_startup.append(show_info)
    app.on_cleanup.append(close_db)

    async def head_age(request):
        """Get hive head block age in seconds. 500 status if age > 15s."""
        #pylint: disable=unused-argument
        healthy_age = 15 # hive is synced if head block within 15s
        try:
            state = await db_head_state(app)
            curr_age = state['db_head_age']
        except Exception as e:
            log.info("could not get head state (%s)", e)
            curr_age = 31e6
        status = 500 if curr_age > healthy_age else 200
        return web.Response(status=status, text=str(curr_age))

    async def health(request):
        """Get hive health state. 500 if db unavailable or too far behind."""
        #pylint: disable=unused-argument
        is_syncer = conf.get('sync_to_s3')

        # while 1 hr is a bit stale, such a condition is a symptom of a
        # writer issue, *not* a reader node issue. Discussion in #174.
        max_head_age = 3600 # 1hr

        try:
            state = await db_head_state(app)
        except OperationalError as e:
            state = None
            log.warning("could not get head state (%s)", e)

        if not state:
            status = 500
            result = 'db not available'
        elif not is_syncer and state['db_head_age'] > max_head_age:
            status = 500
            result = 'head block age (%s) > max (%s); head block num: %s' % (
                state['db_head_age'], max_head_age, state['db_head_block'])
        else:
            status = 200
            result = 'head block age is %d, head block num is %d' % (
                state['db_head_age'], state['db_head_block'])

        return web.json_response(status=status, data=dict(
            state=state,
            result=result,
            status='OK' if status == 200 else 'WARN',
            sync_service=is_syncer,
            source_commit=os.environ.get('SOURCE_COMMIT'),
            schema_hash=os.environ.get('SCHEMA_HASH'),
            docker_tag=os.environ.get('DOCKER_TAG'),
            timestamp=datetime.utcnow().isoformat()))

    async def jsonrpc_handler(request):
        """Handles all hive jsonrpc API requests."""
        request = await request.text()
        # debug=True refs https://github.com/bcb/jsonrpcserver/issues/71
        response = None
        try:
            response = await dispatch(request, methods=methods, debug=True, context=app, serialize=decimal_serialize, deserialize=decimal_deserialize)
        except simplejson.errors.JSONDecodeError as ex:
            # in case of malformed json in request try to salvage some data from it
            # and return error response instead 503 internal server error
            # first log exception
            # TODO: consider removing this log - potential log spam
            log.exception(ex)
            # now we need method and id data from malformed json
            # we cannot do a loads because it will fail so we need to parse
            # request manually
            request_str = str(request)
            # strip outer brackets
            request_str = request_str.rstrip("}")
            request_str = request_str.lstrip("{")

            # extract method and request id
            method = ""
            response_id = -1
            for item in request_str.split(","):
                line = item.split(":")
                if len(line) == 2:
                    if line[0].strip('"') == "method":
                        method = line[1].strip('"')
                    if line[0].strip('"') == "id":
                        try:
                            response_id = int(line[1])
                        except:
                            response_id = line[1]
            # create and send error response
            error_response = {
                "jsonrpc":"2.0",
                "method" : method,
                "error" : {
                    "code": -32602,
                    "data": str(ex),
                    "message": "Invalid JSON in request"
                },
                "id" : response_id
            }
            headers = {'Access-Control-Allow-Origin': '*'}
            return web.json_response(error_response, status=200, headers=headers, dumps=decimal_serialize)
        if response is not None and response.wanted:
            headers = {'Access-Control-Allow-Origin': '*'}
            return web.json_response(response.deserialized(), status=200, headers=headers, dumps=decimal_serialize)
        return web.Response()

    if conf.get('sync_to_s3'):
        app.router.add_get('/head_age', head_age)
    app.router.add_get('/.well-known/healthcheck.json', health)
    app.router.add_get('/health', health)
    app.router.add_post('/', jsonrpc_handler)
    if 'auto_http_server_port' in app['config']['args'] and app['config']['args']['auto_http_server_port'] is not None:
        log.debug("auto-http-server-port detected in program arguments, http_server_port will be overriden with port from given range")
        port_range = app['config']['args']['auto_http_server_port']
        port_range_len = len(port_range)
        port_from = port_range[0]
        port_to = port_range[1] if port_range_len == 2 else 65535
        if port_to > 65535:
            port_to = 65535
        if port_from < 1024:
            port_from = 1024

        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while port_from <= port_to:
            try:
                log.debug("Trying port: {}".format(port_from))
                sock.bind(('', port_from))
            except OSError as ex:
                log.debug("Exception: {}".format(ex))
                port_from += 1
            except Exception as ex:
                # log and rethrow exception
                log.exception("Exception: {}".format(ex))
                raise ex
            else:
                with open('hivemind.port', 'w') as port_file:
                    port_file.write("{}\n".format(port_from))
                web.run_app(app, sock=sock)
                break
        if port_from == port_to:
            raise IOError('No free ports in given range')
    else:
        web.run_app(app, port=app['config']['args']['http_server_port'])
