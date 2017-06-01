#
# Copyright (c) 2014 NSONE, Inc.
#
# License under The MIT License (MIT). See LICENSE in project root.
#
from __future__ import absolute_import

from nsone.rest.transport.base import TransportBase
from nsone.rest.errors import ResourceException, RateLimitException, \
    AuthException

try:
    from urllib.request import build_opener, Request, HTTPSHandler
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import build_opener, Request, HTTPSHandler
    from urllib2 import HTTPError
import json
import socket


class BasicTransport(TransportBase):

    def __init__(self, config):
        TransportBase.__init__(self, config, self.__module__)
        self._timeout = self._config.get('timeout', socket._GLOBAL_DEFAULT_TIMEOUT)

    def send(self, method, url, headers=None, data=None, files=None,
             callback=None, errback=None):
        if headers is None:
            headers = {}
        if files is not None:
            # XXX
            raise Exception('file uploads not supported in BasicTransport yet')
        self._logHeaders(headers)
        self._log.debug("%s %s %s" % (method, url, data))
        opener = build_opener(HTTPSHandler)
        request = Request(url, headers=headers, data=data)
        request.get_method = lambda: method

        def handleProblem(code, resp, msg):
            if errback:
                errback((resp, msg))
                return

            if code == 429:
                raise RateLimitException('rate limit exceeded',
                                         resp,
                                         msg)
            elif code == 401:
                raise AuthException('unauthorized',
                                    resp,
                                    msg)
            else:
                raise ResourceException('server error',
                                        resp,
                                        msg)

        # Handle error and responses the same so we can
        # always pass the body to the handleProblem function
        try:
            resp = opener.open(request, timeout=self._timeout)
            body = resp.read()
        except HTTPError as e:
            resp = e
            body = resp.read()
        except Exception as e:
            body = '"Service Unavailable"'
            resp = HTTPError(url, 503, body, headers, None)
        finally:
            if resp.code != 200:
                handleProblem(resp.code, resp, body)

        # TODO make sure json is valid
        try:
            jsonOut = json.loads(body)
        except ValueError:
            if errback:
                errback(resp)
                return
            else:
                raise ResourceException('invalid json in response',
                                        resp,
                                        body)
        if callback:
            return callback(jsonOut)
        else:
            return jsonOut

TransportBase.REGISTRY['basic'] = BasicTransport
