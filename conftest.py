import json
import os

import pytest
from openai import OpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


@pytest.fixture(scope="session")
def llm_client():
    kwargs = {"api_key": os.environ["OPENAI_API_KEY"]}
    base_url = os.environ.get("OPENAI_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


@pytest.fixture(scope="session")
def prompt_data():
    with open("prompts/prompts.json") as f:
        return json.load(f)
