nsone.config
============

This object is used to configure the SDK and REST client. It handles multiple
API keys via a simple selection mechanism (keyID).

Sample:

.. code-block:: json

    {
       "default_key": "account2",
       "verbosity": 5,
       "keys": {
            "account1": {
                "key": "qACMD09OJXBxT7XOuRs8",
                "desc": "account number 1",
                "writeLock": true
            },
            "account2": {
                "key": "qACMD09OJXBxT7XOwv9v",
                "desc": "account number 2",
                "writeLock": false
            }
       },
       "cli": {
           "output_format": "text"
       }
    }

.. automodule:: nsone.config
    :members:
    :undoc-members:
    :show-inheritance:



