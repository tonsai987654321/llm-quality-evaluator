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
    return OpenAI(api_key=os.environ["OPENAI_API_KEY"])


@pytest.fixture(scope="session")
def prompt_data():
    with open("prompts/prompts.json") as f:
        return json.load(f)
