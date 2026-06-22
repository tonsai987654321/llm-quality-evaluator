from evaluators.latency import score_latency


def test_fast_response_scores_1():
    assert score_latency(1.0) == 1.0


def test_at_threshold_scores_1():
    assert score_latency(10.0) == 1.0


def test_slow_response_degrades():
    score = score_latency(15.0)
    assert 0.0 < score < 1.0


def test_very_slow_response_scores_0():
    assert score_latency(20.0) == 0.0


def test_custom_threshold():
    assert score_latency(5.0, threshold=5.0) == 1.0
    assert score_latency(10.0, threshold=5.0) == 0.0
