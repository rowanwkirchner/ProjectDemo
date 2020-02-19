# -*- coding: utf-8 -*-
"""
Copyright 2019 KineticSkunk ITS, Cape Town, South Africa.

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

from toolium.pageobjects.page_object import PageObject


class CustomLogger(PageObject):

    def auto_log_debug(self, message):
        """Automatically log the current function details."""
        import inspect
        # Get the previous frame in the stack, otherwise it would
        # be this function!!!
        func = inspect.currentframe().f_back.f_code
        # Dump the message + the name of this function to the log.
        self.logger.debug("%s: %s in %s:%i" % (
            message,
            func.co_name,
            func.co_filename,
            func.co_firstlineno
        ))

    def auto_log_error(self, message):
        """Automatically log the current function details."""
        import inspect
        # Get the previous frame in the stack, otherwise it would
        # be this function!!!
        func = inspect.currentframe().f_back.f_code
        # Dump the message + the name of this function to the log.
        self.logger.error("%s: %s in %s:%i" % (
            message,
            func.co_name,
            func.co_filename,
            func.co_firstlineno
        ))

    def auto_log_info(self, message):
        """Automatically log the current function details."""
        import inspect
        # Get the previous frame in the stack, otherwise it would
        # be this function!!!
        func = inspect.currentframe().f_back.f_code
        # Dump the message + the name of this function to the log.
        self.logger.info("%s: %s in %s:%i" % (
            message,
            func.co_name,
            func.co_filename,
            func.co_firstlineno
        ))
