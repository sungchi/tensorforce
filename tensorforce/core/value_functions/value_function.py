# Copyright 2017 reinforce.io. All Rights Reserved.
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
# ==============================================================================

"""
Generic baseline value function for policy gradient methods.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class ValueFunction(object):

    def __init__(self, session):
        self.session = session

    def create_tf_operations(self):
        raise NotImplementedError

    def predict(self, states):
        raise NotImplementedError

    def update(self, states, returns):
        raise NotImplementedError
