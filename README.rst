Legacy NS1 Python SDK
=====================

> This SDK is [deprecated](https://github.com/ns1/community/blob/master/project_status/DEPRECATED.md)
in favor of `ns1-python <https://github.com/ns1/ns1-python>` _and should not be used for new projects._

The code in this repository provides just a thin wrapper for the new SDK to allow easier migration.

Migration to the new SDK
------------------------

The new SDK provides equivalent functionality. To migrate a project to the new
SDK:

* Update your project dependencies to use ``ns1-python`` instead of ``nsone``.
* Replace use of ``nsone`` namespace with ``ns1``.
* Replace use of ``nsone.NSONE`` with ``ns1.NS1``.
