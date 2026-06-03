import pytest

pytest_plugins = [
    "fixtures.page_objects"
]


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,

        "record_video_dir": "reports/videos"
    }