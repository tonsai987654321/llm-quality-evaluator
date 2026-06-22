import json
import os

import pytest
from openai import OpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def _load_prompts():
    with open("prompts/prompts.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def llm_client():
    kwargs = {"api_key": os.environ["OPENAI_API_KEY"]}
    base_url = os.environ.get("OPENAI_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


@pytest.fixture(scope="session")
def prompt_data():
    return _load_prompts()


def pytest_generate_tests(metafunc):
    prompts = _load_prompts()
    if "prompt_item" in metafunc.fixturenames:
        metafunc.parametrize("prompt_item", prompts, ids=[p["prompt"] for p in prompts])
    if "factual_prompt_item" in metafunc.fixturenames:
        factual = [p for p in prompts if p.get("expected_facts")]
        metafunc.parametrize("factual_prompt_item", factual, ids=[p["prompt"] for p in factual])
    if "open_ended_prompt_item" in metafunc.fixturenames:
        open_ended = [p for p in prompts if not p.get("expected_facts")]
        metafunc.parametrize("open_ended_prompt_item", open_ended, ids=[p["prompt"] for p in open_ended])
