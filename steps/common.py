from behave import given, when, then

from pageobjects.common import CommonPageObject
from pageobjects.login import LoginPageObject


@given('the "{page_name}" page is open')
@when('the "{page_name}" page is open')
@then('the "{page_name}" page is open')
def step_impl(context, page_name=""):
    context.current_page = CommonPageObject().init_web_page(page_name)
    context.current_page = context.current_page.init_web_page_elements(context.current_page.mobile_page)
    assert page_name in context.current_page.mobile_page.__class__.__name__, \
        "page_name = {}, class_name = {}" \
            .format(page_name, context.current_page.mobile_page.__class__.__name__)

# @given('close "{page_name}"')
# @when('close "{page_name}"')
# @then('close "{page_name}"')
# def step_impl(context, page_name=""):
#     context.current_page = CommonPageObject().init_web_page(page_name)
#     context.current_page = context.current_page.init_web_page_elements(context.current_page.mobile_page)
#     assert page_name in context.current_page.mobile_page.__class__.__name__, \
#         "page_name = {}, class_name = {}" \
#             .format(page_name, context.current_page.mobile_page.__class__.__name__)


@given('the "{element_name}" element "{attribute_name}" has a value of "{expected_value}"')
@when('the "{element_name}" element "{attribute_name}" has a value of "{expected_value}"')
@then('the "{element_name}" element "{attribute_name}" has a value of "{expected_value}"')
def step_impl(context, element_name, attribute_name, expected_value):
    actual_value = context.current_page.get_mobile_element_attribute_value(element_name, attribute_name)
    assert str(actual_value).lower() == str(expected_value).lower(), \
        "element_name = '{}', attribute_name = '{}', expected value = '{}', actual_value = '{}'" \
            .format(element_name, attribute_name, expected_value, actual_value)


@given('the "{element_name}" element "{attribute_name}" contains "{expected_value}"')
@when('the "{element_name}" element "{attribute_name}" contains "{expected_value}"')
@then('the "{element_name}" element "{attribute_name}" contains "{expected_value}"')
def step_impl(context, element_name, attribute_name, expected_value):
    actual_value = context.current_page.get_mobile_element_attribute_value(element_name, attribute_name)
    assert str(expected_value).lower() in str(actual_value).lower(), \
        "element_name = '{}', attribute_name = '{}', expected value = '{}'" \
            .format(element_name, attribute_name, expected_value, actual_value)


@given('the user clicks the "{element_name}" where "{attribute_name}" has a value of "{attribute_value}"')
@when('the user clicks the "{element_name}" where "{attribute_name}" has a value of "{attribute_value}"')
@then('the user clicks the "{element_name}" where "{attribute_name}" has a value of "{attribute_value}"')
def step_impl(context, element_name="", attribute_name=None, attribute_value=None):
    assert context.current_page.click_element(element_name, attribute_name, attribute_value) is True, \
        "Attempted to click on element '{}'".format(element_name)


@given('the user sets the "{attribute}" value of element "{element_name}" to "{value}"')
@when('the user sets the "{attribute}" value of element "{element_name}" to "{value}"')
@then('the user sets the "{attribute}" value of element "{element_name}" to "{value}"')
def step_impl(context, attribute="", element_name="", value=""):
    assert context.current_page.set_element_attribute_value(element_name, attribute, value) is True, \
        "Attempted to set the value of '{}.{}' to '{}'".format(element_name, attribute, value)


@given('the user selects the value "{value}" from the "{element_name}" list')
@when('the user selects the value "{value}" from the "{element_name}" list')
def step_impl(context, value=None, element_name=None):
    assert context.current_page.select_list_value(element_name, value) is True, \
        "Failed to select the value {} in list '{}'".format(value, element_name)


@given('the user "{checks}" the "{element_name}" in page "{page_name}"')
@when('the user "{checks}" the "{element_name}" in page "{page_name}"')
def step_impl(context, checks="checks", element_name="", page_name=""):
    assert context.current_page.check_element(page_name, element_name, checks) is True, \
        "Attempted to check element '{}' in page {}".format(element_name, page_name)


@given('the user clears "{element_name}"')
@when('the user clears "{element_name}"')
def step_impl(context, element_name):
    assert context.current_page.clear_element(element_name) is True, \
        "Attempted to clear element value '{}'".format(element_name)


@given('the user toggles the wifi')
@when('the user toggles the wifi')
def step_impl(context):
    context.current_page.switch_off_connectivity()


@given('the user scroll "{element_name}" into view')
@when('the user scroll "{element_name}" into view')
@then('the user scroll "{element_name}" into view')
def step_impl(context, element_name):
    context.current_page.scroll_into_view(element_name)
    "Attempted to click on element '{}'".format(element_name)


@given('the user scrolls down')
@when('the user scrolls down')
@then('the user scrolls down')
def step_impl(context):
    context.current_page.web_scroll()


@given('the user hovers over middle dress')
@when('the user hovers over middle dress')
@then('the user hovers over middle dress')
def step_impl(context):
    context.current_page.hover()


@given('the user drags "{first_element}" to "{second_element}"')
@when('the user drags "{first_element}" to "{second_element}"')
def step_impl(context, first_element, second_element):
    context.current_page.drag_element(first_element, second_element)


@given('the user drags "{first_element}" to "{second_element}" in order to zoom')
@when('the user drags "{first_element}" to "{second_element}" in order to zoom')
def step_impl(context, first_element, second_element):
    context.current_page.zoom_element(first_element, second_element)


@given('the user double taps and drags "{element_name}"')
@when('the user double taps and drags "{element_name}"')
@then('the user double taps and drags "{element_name}"')
def step_impl(context, element_name):
    context.current_page.drag_hold(element_name)
    "Attempted to click on element '{}'".format(element_name)
