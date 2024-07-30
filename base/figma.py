import os

import requests

from base import secrets

BASE_URL = "https://api.figma.com"

ME_ENDPOINT = "/v1/me"

TEAM_ID = "1400022202890114290"
TEAM_PROJECTS_ENDPOINT_TEMPLATE = "/v1/teams/{team_id}/projects"
PROJECT_FILES_ENDPOINT_TEMPLATE = "/v1/projects/{project_id}/files"

FILE_ENDPOINT_TEMPLATE = "/v1/files/{file_key}"

if __name__ == "__main__":
    headers = {"X-FIGMA-TOKEN": secrets.FIGMA_API_TOKEN}

    url = BASE_URL + ME_ENDPOINT
    url = BASE_URL + TEAM_PROJECTS_ENDPOINT_TEMPLATE.format(team_id=TEAM_ID)
    url = BASE_URL + PROJECT_FILES_ENDPOINT_TEMPLATE.format(project_id="260394413")
    url = BASE_URL + FILE_ENDPOINT_TEMPLATE.format(file_key="ia4bwrtffnOTBHacQxdJfe")

    resp = requests.get(url, headers=headers)
    print(resp)
