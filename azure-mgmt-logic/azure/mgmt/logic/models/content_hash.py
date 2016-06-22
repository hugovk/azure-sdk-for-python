# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContentHash(Model):
    """ContentHash.

    :param algorithm: Gets or sets the algorithm.
    :type algorithm: str
    :param value: Gets or sets the value.
    :type value: str
    """ 

    _attribute_map = {
        'algorithm': {'key': 'algorithm', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, algorithm=None, value=None):
        self.algorithm = algorithm
        self.value = value
