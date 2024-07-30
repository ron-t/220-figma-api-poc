import os

import pytest
import requests

from base import figma, secrets


@pytest.fixture(scope="session")
def header():
    yield {"X-FIGMA-TOKEN": secrets.FIGMA_API_TOKEN}


@pytest.fixture(scope="session")
def api_me_payload(header):
    url = figma.BASE_URL + figma.ME_ENDPOINT
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        raise
    return response.json()


def test_get_request(api_me_payload):
    assert api_me_payload["email"] == "rtio003@aucklanduni.ac.nz"
