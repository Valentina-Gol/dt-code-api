import logging

from flask import Flask
from flask_cors import CORS

from .actions.version import version as api_version

from .actions.modules.info import info as modules_info
from .actions.modules.status import status as modules_status
from .actions.modules.update import update as modules_update

from .actions.module.update import update as module_update

from .actions.container.run import run as container_run
from .actions.container.status import status as container_status
from .actions.container.stop import stop as container_stop
from .actions.container.restart import restart as container_restart


class CodeAPI(Flask):

    def __init__(self, debug=False):
        super(CodeAPI, self).__init__(__name__)
        # register blueprints (/*)
        self.register_blueprint(api_version)
        # register blueprints (/modules/*)
        self.register_blueprint(modules_info)
        self.register_blueprint(modules_status)
        self.register_blueprint(modules_update)
        # register blueprints (/module/*)
        self.register_blueprint(module_update)
        # register blueprints (/container/*)
        self.register_blueprint(container_run)
        self.register_blueprint(container_status)
        self.register_blueprint(container_stop)
        self.register_blueprint(container_restart)
        # apply CORS settings
        CORS(self)
        # configure logging
        logging.getLogger('werkzeug').setLevel(logging.DEBUG if debug else logging.WARNING)
