# -*- coding: utf-8 -*-
"""
Copyright 2018 KineticSkunk ITS, Cape Town, South Africa.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pageobjects.common import CommonPageObject


class Actionwords:

    cpo = None

    def __init__(self):
        self.cpo = CommonPageObject

    def the_page_is_open(self, page_name=None):
        self.cpo = CommonPageObject().init_web_page(page_name)
        assert page_name in self.cpo.__class__.__name__, \
            "page_name = {}, class_name = {}" \
            .format(page_name, self.cpo.__class__.__name__)
        pass


