from behave import *


@given(u'A new web page "{web_page}" is open')
def step_impl(context, web_page):
    context.home_page.navigate(web_page)
    assert context.home_page.get_page_title() == 'Google'

