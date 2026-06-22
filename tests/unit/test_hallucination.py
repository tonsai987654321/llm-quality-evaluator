from evaluators.hallucination import score_hallucination


def test_all_facts_present_scores_1():
    response = "The capital of France is Paris, a beautiful city."
    assert score_hallucination(response, ["Paris"]) == 1.0


def test_no_facts_present_scores_0():
    response = "The capital of France is Lyon."
    assert score_hallucination(response, ["Paris"]) == 0.0


def test_partial_facts_returns_fraction():
    response = "Shakespeare wrote many plays including Romeo and Juliet."
    facts = ["Shakespeare", "Marlowe"]
    assert score_hallucination(response, facts) == 0.5


def test_empty_facts_scores_1():
    assert score_hallucination("any response", []) == 1.0


def test_case_insensitive_match():
    response = "The answer is h2o which is water."
    assert score_hallucination(response, ["H2O"]) == 1.0
