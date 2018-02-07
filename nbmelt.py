"""nbmelt: shutdown notebook servers that don't get used

nbmelt starts a timer when the notebook server starts.
If no APIRequest is made by that time, the server will exit.

That's it!

Usage: jupyter server extension enable nbmelt
"""

__version__ = '0.1.0'

import os

from notebook.base.handlers import APIHandler
from tornado.ioloop import IOLoop


def load_jupyter_server_extension(app):
    """Load the extension"""
    timeout = int(os.environ.get('NBMELT_TIMEOUT') or '120')
    app.log.info("This notebook will self destruct in %s seconds! (if you don't use it)", timeout)
    state = {'called': False}
    save_initialize = APIHandler.initialize

    # monkeypatch APIHandler.initialize
    # all we want to know is if one APIHandler was called one time
    def initialize(*args, **kwargs):
        app.log.debug("Received API request, halting nbmelt")
        state['called'] = True
        # only do this once:
        APIHandler.initialize = save_initialize
        return save_initialize(*args, **kwargs)
    APIHandler.initialize = initialize

    def shutdown_if_unused():
        if not state['called']:
            app.log.error("No API request received in %ss, exiting.", timeout)
            IOLoop.current().stop()

    IOLoop.current().call_later(timeout, shutdown_if_unused)
