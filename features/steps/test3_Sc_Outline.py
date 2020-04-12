from behave import *


@given(u'using "{site}" to search')
def step_impl(context, site):
    context.home_page.navigate(site)
    assert context.home_page.get_page_title() == 'Google' or 'DuckDuckGo — Privacy, simplified.'


@when(u'user searches for "{things}"')
def step_impl(context, things):
    context.home_page.search(things)

