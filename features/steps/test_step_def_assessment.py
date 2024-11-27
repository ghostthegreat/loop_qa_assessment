from behave import given, when, then
import asyncio
from pages.test_landing_page import LandingPage
from pages.test_cross_functional_page import CrossFunctionalPage
from pages.test_work_requests_page import WorkRequestsPage
from pages.login_page import LoginPage

@given(u'I am logged into Asana')
async def step_impl(context):
    login_page = LoginPage(context.page)
    await login_page.login()

async def _login(context):
    login_page = LoginPage(context.page)
    await login_page.login()

@when(u'I navigate to "{page_name}"')
async def step_impl(context, page_name):
    asyncio.run(_navigate(context, page_name))

async def _navigate(context, page_name):
    landing_page = LandingPage(context.page)
    if page_name == "Cross-functional project plan, Project":
        await landing_page.navigate_to_cross_functional_page()
        cross_func_page = CrossFunctionalPage(context.page, context)
        context.cross_func_page = cross_func_page
    elif page_name == "Work Requests":
        await landing_page.navigate_to_work_requests_page()
        work_requests_page = WorkRequestsPage(context.page, context)
        context.work_requests_page = work_requests_page
    else:
        raise ValueError(f"Unknown page name: {page_name}")

@then(u'I should see "{task_name}" in the "{column_name}" column')
async def step_impl(context, task_name, column_name):
    asyncio.run(_verify_task(context, task_name, column_name))

async def _verify_task(context, task_name, column_name):
    if hasattr(context, 'cross_func_page'):
        page = context.cross_func_page
    elif hasattr(context, 'work_requests_page'):
        page = context.work_requests_page
    else:
        raise AttributeError("Page object not found in context")

    context.current_task_name = task_name
    context.current_column_name = column_name

    await page.verify_task_in_column(column_name, task_name)

@then(u'it should have the tags:')
async def step_impl(context):
    asyncio.run(_verify_tags(context))

async def _verify_tags(context):
    if not (hasattr(context, 'current_task_name') and hasattr(context, 'current_column_name')):
        raise AttributeError("No task information found in context")

    expected_tags = [row[0] for row in context.table]
    if hasattr(context, 'cross_func_page'):
        page = context.cross_func_page
    elif hasattr(context, 'work_requests_page'):
        page = context.work_requests_page
    else:
        raise AttributeError("Page object not found in context")

    await page.verify_task_tags(context.current_column_name, context.current_task_name, expected_tags)

