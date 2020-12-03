#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app
from bottle import debug, run

debug(True)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8090))
    run(app, reloader=True, host='localhost', port=port)
