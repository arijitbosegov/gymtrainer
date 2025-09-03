import pytest
from gymtrainer import create_gymtrainer  # or your app factory function

@pytest.fixture
def gymtrainer():
    gymtrainer = create_gymtrainer()
    gymtrainer.config.update({
        "TESTING": True,
    })

    yield gymtrainer  # tests run here

@pytest.fixture
def client(gymtrainer):
    return gymtrainer.test_client()

