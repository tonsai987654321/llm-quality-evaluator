from evaluators.consistency import score_consistency


def test_identical_responses_score_1():
    responses = ["The sky is blue.", "The sky is blue.", "The sky is blue."]
    assert score_consistency(responses) == 1.0


def test_completely_different_responses_score_low():
    responses = ["apple banana cherry", "dog elephant fox", "guitar hammer iron"]
    assert score_consistency(responses) < 0.2


def test_single_response_scores_1():
    assert score_consistency(["only one response"]) == 1.0


def test_partial_overlap_between_0_and_1():
    responses = ["the cat sat on the mat", "the cat sat on a bench", "a cat sat on the floor"]
    score = score_consistency(responses)
    assert 0.0 < score < 1.0
