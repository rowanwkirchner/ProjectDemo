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
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from selenium import webdriver
from toolium.pageelements import PageElement
from toolium.pageelements import PageElements
from toolium.pageobjects.page_object import PageObject
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from pageobjects.Create_an_account import CreateAccountPageObject
from pageobjects.custom_logger import CustomLogger
from pageobjects.login import LoginPageObject
from pageobjects.home_page import HomePageObject

import time


class CommonPageObject(PageObject):
    cl = CustomLogger()

    mobile_page = None
    page_element = None
    page_elements = {}
    mobile_page_element = None
    mobile_page_elements = None
    actual_value = None
    connectivity = None

    option_locator = 'new UiScrollable(new UiSelector().scrollable(true).instance(0))' \
                     '.scrollIntoView(new UiSelector().text("{}").instance(0));'

    def init_web_page(self, page_name):
        """Initialize mobile pages"""
        self.cl.auto_log_info("Attempting to load page {}".format(page_name))

        switcher = {
            "LoginPageObject": LoginPageObject(),
            "HomePageObject": HomePageObject(),
            "CreateAccountPageObject": CreateAccountPageObject()

        }

        self.mobile_page = switcher.get(page_name, None)

        self.cl.auto_log_info("Mobile page {} = '{}'".format(page_name, self.mobile_page.__class__.__name__))

        if self.mobile_page is not None:
            self.mobile_page = self.mobile_page.wait_until_loaded(self.driver.
                                                                  get('{}'.format(self.config.
                                                                                  get('Test', 'url'))))
            self.cl.auto_log_info("Loaded page {}".format(self.mobile_page.__class__.__name__))
        else:
            self.cl.auto_log_error("Failed to load page {}".format(page_name))
        return self

    def init_web_page_elements(self, mobile_page=None):
        """Method to initialize page elements. """
        self.cl.auto_log_info("The mobile_page object = {}".format(mobile_page.__class__.__name__))

        for attribute, value in list(mobile_page.__dict__.items()) + list(
                mobile_page.__class__.__dict__.items()):
            if attribute != 'parent' and isinstance(value, PageElement) or isinstance(value, PageElements):
                self.cl.auto_log_info("Element name = {}, value = {}".format(attribute, value))
                self.page_elements[attribute] = value
        return self

    def get_element(self, element_name=None):
        """This method get a given page element."""
        try:
            if element_name in self.page_elements:
                self.cl.auto_log_info("Found element {} in '{}'".format(element_name,
                                                                        self.page_elements.__class__.__name__))

                self.cl.auto_log_debug("Element {} = '{}'".format(element_name, self.page_elements[element_name]))
            assert self.page_elements[element_name] is not None
        except AssertionError as error:
            self.cl.auto_log_error("Element {} = {}'".format(element_name, "None"))
            self.cl.auto_log_error("Error message= ".format(error))
            return None
        else:
            return self.page_elements[element_name]

    def get_mobile_element_attribute_value(self, element_name=None, attribute_name=None):
        """This method get a given page element and verifies with attribute values."""
        actual_value = None
        if element_name is not None:
            actual_value = self.get_element(element_name).get_attribute(attribute_name)
            self.cl.auto_log_debug("{}.{} = {}".format(element_name, attribute_name, actual_value))
        else:
            self.cl.auto_log_error("{} = {}".format(element_name, "None"))
        return actual_value

    def click_element(self, element_name=None, attribute=None, value=None):
        """This method clicks page elements and verifies with attribute values."""

        try:
            self.mobile_page_element = self.get_element(element_name)
            assert str(self.get_mobile_element_attribute_value(element_name, attribute)).lower() == \
                   str(value).lower()
        except AssertionError as error:
            self.cl.auto_log_error("{}.{} <> {}'".format(element_name, attribute, value))
            self.cl.auto_log_error("Error message= ".format(error))
            return False
        else:
            self.mobile_page_element.click()
            self.cl.auto_log_debug("Clicked on element '{}'".format(element_name))
            return True
        finally:
            self.mobile_page_element = None
        pass

    def set_element_attribute_value(self, element_name=None, attribute=None, value=None):
        """This method set a attribute value to a page element."""
        try:
            self.cl.auto_log_debug("Attempting to set '{}.{}' to '{}'".format(element_name, attribute, value))
            self.mobile_page_element = self.utils.get_web_element(self.get_element(element_name))
            if str(attribute).lower().__eq__("text"):
                self.mobile_page_element.send_keys(value)
            elif str(attribute).lower().__eq__("value"):
                self.mobile_page_element.send_keys(value)
            else:
                err_msg = ("Attribute '{}' is not supported or cannot be set".format(attribute))
                self.cl.auto_log_error(err_msg)
                raise Exception(err_msg)

            # assert str(self.get_mobile_element_attribute_value(element_name, attribute)).lower() == str(value).lower()
        except AssertionError as error:
            err_msg = ("Failed to set '{}.{}' to '{}'".format(element_name, attribute, value))
            self.cl.auto_log_error(err_msg)
            self.cl.auto_log_error("Error message= ".format(error))
            return False
        else:
            return True
        finally:
            self.mobile_page_element = None
        pass

    def select_list_value(self, element_name=None, value=None):
        """This method select a list value in list view."""
        self.cl.auto_log_info("Attempting to select list value '{}' in list '{}'".format(value, element_name))
        el = self.get_list_element(element_name, value)
        if el is not None:
            self.utils.get_web_element(el).click()
            return True
        elif self.mobile_page_element is False:
            err_msg = ("List value '{}' was not found in '{}'".format(value, element_name))
            self.cl.auto_log_error(err_msg)
            raise Exception(err_msg)
        return False

    def get_list_element(self, element_name=None, value=None):
        """This method get a list element in list view."""
        try:
            self.cl.auto_log_info("Attempting to locate list value '{}' in list '{}'".format(value, element_name))
            self.mobile_page_elements = self.get_element(element_name)

            if self.mobile_page_elements is not None:
                for el in self.mobile_page_elements.web_elements:
                    self.cl.auto_log_info("List value = {}".format(el.get_attribute("text")))
                    if value.lower() == str(el.get_attribute("text")).lower():
                        self.cl.auto_log_info("List value {} found = '{}'".format(el.get_attribute("text"), True))
                        return el
                self.cl.auto_log_error("List value {} found = '{}'".format(value, False))
                return None
            else:
                err_msg = "Element '{}' is undefined".format(element_name)
                self.cl.auto_log_error(err_msg)
                raise Exception(err_msg)
        finally:
            self.mobile_page_elements = None
        pass

    def check_element(self, element_name=None, checks=None):
        """This method select the checkbox."""
        try:
            switcher = {
                "checked": True,
                "unchecked": False
            }

            perf_check = switcher.get(checks, None)
            msg = None

            if perf_check is True:
                msg = "Attempting to check element = {}".format(element_name)
            elif perf_check is False:
                msg = "Attempting to uncheck element = {}".format(element_name)
            elif perf_check is None:
                err_msg = "'{}' is not a supported check box action".format(checks)
                self.cl.auto_log_error(err_msg)
                raise Exception(err_msg)

            self.cl.auto_log_info(msg)

            self.mobile_page_element = self.utils.get_web_element(self.get_element(element_name))

            # TODO add instance check

            if perf_check is True:
                msg = "Checking '{}'".format(element_name)
                self.mobile_page_element.check()
            elif perf_check is False:
                msg = "Un-checking '{}'".format(element_name)
                self.mobile_page_element.uncheck()

            self.cl.auto_log_info(msg)

            if perf_check is True:
                assert self.mobile_page_element.is_selected() is True
            elif perf_check is False:
                assert self.mobile_page_element.is_selected() is False
        except AssertionError as error:
            err_msg = ("Failed to '{}' checkbox '{}'".format(checks, element_name))
            self.cl.auto_log_error(err_msg)
            self.cl.auto_log_error("Error message= ".format(error))
            return False
        finally:
            self.mobile_page_element = None
        pass

    def clear_element(self, element_name):
        """This method clear the element value."""
        self.cl.auto_log_info("Attempting to clear element value '{}'".format(element_name))
        el = self.get_element(element_name)

        if el is not None:
            self.utils.get_web_element(el).clear()
            return True
        return self

    def switch_off_connectivity(self):
        """This method toggles the wifi."""
        self.connectivity = \
            self.driver.toggle_wifi()
        time.sleep(9)

    def scroll_into_view(self, element_name):
        """This method scrolls an element into view."""
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, self.option_locator.format(element_name))
        self.cl.auto_log_info("Clicked on element '{}'".format(element_name))
        return self

    def web_scroll(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)

    def hover(self):
        self.element = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/ul/li[2]')
        self.hover = ActionChains(self.driver).move_to_element(self.element).perform()
        self.add_to_cart = self.driver.find_element(By.XPATH,
                                                    '/html/body/div/div[2]/div/div[3]/div[2]/ul/li[2]/div/div['
                                                    '2]/div[2]/a[2]/span').click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)

    def drag_element(self, first_element=None, second_element=None):
        """This method drags a element to another element."""
        el1 = self.utils.get_web_element(self.get_element(first_element))
        self.cl.auto_log_error("Attempting to find element value '{}'".format(first_element))
        el2 = self.utils.get_web_element(self.get_element(second_element))
        self.cl.auto_log_error("Attempting to find element value '{}'".format(second_element))
        self.driver.scroll(el1, el2)
        return self

    def zoom_element(self, first_element=None, second_element=None):
        """This method uses touch action to zoom an element."""
        el1 = self.utils.get_web_element(self.get_element(first_element))
        self.cl.auto_log_error("Attempting to find element value '{}'".format(first_element))
        el2 = self.utils.get_web_element(self.get_element(second_element))
        self.cl.auto_log_error("Attempting to find element value '{}'".format(second_element))

        action1 = TouchAction()
        action1.long_press(el1, 10, 20).move_to(el2, 10, 200).release()

        action2 = TouchAction()
        action2.long_press(el2, 10, 10).move_to(el1, 10, 100).release()

        ma = MultiAction(self.driver)
        ma.add(action1, action2)
        ma.perform()

    def drag_hold(self, element_name=None):
        """This method uses multi touch action to double tap and drag element."""
        el1 = self.utils.get_web_element(self.get_element(element_name))
        self.cl.auto_log_error("Attempting to find element value '{}'".format(element_name))
        action0 = TouchAction().tap(el1).move_to(el1, 10, 200)
        action1 = TouchAction().tap(el1).move_to(el1, 200, 10)
        ma = MultiAction(self.driver)
        ma.add(action0, action1)
        ma.perform()
