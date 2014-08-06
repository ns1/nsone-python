#
# Copyright (c) 2014 NSONE, Inc.
#
# License under The MIT License (MIT). See LICENSE in project root.
#

from nsone.rest.records import Records


class RecordException(Exception):
    pass


class Record(object):

    def __init__(self, parentZone, domain, type):
        self._rest = Records(parentZone.config)
        self.parentZone = parentZone
        if not domain.endswith(parentZone.zone):
            domain = domain + '.' + parentZone.zone
        self.domain = domain
        self.type = type
        self.data = None
        self.answers = None

    def load(self, callback=None):
        if self.data:
            raise RecordException('record already loaded')

        def success(result):
            self.data = result
            self.answers = self.data['answers']
            if callback:
                return callback(self)
            else:
                return self
        return self._rest.retrieve(self.parentZone.zone,
                                   self.domain, self.type, callback=success)

    def delete(self, callback=None):
        if not self.data:
            raise RecordException('record not loaded')

        def success(result):
            if callback:
                return callback(result)
            else:
                return result
        return self._rest.delete(self.parentZone.zone,
                                 self.domain, self.type,
                                 callback=success)

    def update(self, answers, filters=None, ttl=None, callback=None):
        if not self.data:
            raise RecordException('record not loaded')

        def success(result):
            self.data = result
            self.answers = self.data['answers']
            if callback:
                return callback(self)
            else:
                return self
        return self._rest.update(self.parentZone.zone,
                                 self.domain, self.type,
                                 answers, filters=filters,
                                 ttl=ttl, callback=success)

    def create(self, answers, filters=None, ttl=None, callback=None):
        if self.data:
            raise RecordException('record already loaded')

        def success(result):
            self.data = result
            self.answers = self.data['answers']
            if callback:
                return callback(self)
            else:
                return self
        return self._rest.create(self.parentZone.zone,
                                 self.domain, self.type,
                                 answers, filters=filters, ttl=ttl,
                                 callback=success)
