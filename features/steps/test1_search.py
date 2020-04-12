from behave import *


@given(u'web page "{web_page}" is open')
def step_impl(context, web_page):
    context.home_page.navigate(web_page)
    assert context.home_page.get_page_title() == 'DuckDuckGo — Privacy, simplified.'


@when(u'the user searches for "{phrase}"')
def step_impl(context, phrase):
    context.home_page.search(phrase)


@then(u'The search results should be displayed')
def step_impl(context):
    search_links_count = context.search_results_page.get_links()
    assert len(search_links_count) > 0


@then(u'the results should contains "{phrase}"')
def step_impl(context, phrase):
    assert context.search_results_page.find_search_result(phrase)
