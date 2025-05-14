import pytest

def function_print(functName, *args):
    funcNameArgs = functName.replace('_', ' ').title() + ' ' + str(list(args)).replace("'", "")
    print(funcNameArgs)
    return funcNameArgs

def test_readable_function():
    open_browser(browser_name="Chrome")
    #go_to_companyname_homepage(page_url="https://companyname.com")
    #find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = function_print(open_browser.__name__, browser_name)
    print(actual_result)
    assert actual_result == "Open Browser [Chrome]"
