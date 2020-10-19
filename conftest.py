import pytest


def pytest_addoption(parser):
    parser.addoption("--apiKey", action="store")


@pytest.fixture(scope="session")
def apiKey(request):
    apiKeyValue = request.config.option.apiKey

    if not apiKeyValue:
        pytest.skip()

    return apiKeyValue
