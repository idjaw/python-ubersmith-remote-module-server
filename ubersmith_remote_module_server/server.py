# Copyright 2016 Internap
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask

from ubersmith_remote_module_server import api, router

class Server(object):
    def __init__(self, modules):
        self.router = router.Router(modules)
        self.app = Flask(__name__)
        self.api = api.Api(self.app, self.router)

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)