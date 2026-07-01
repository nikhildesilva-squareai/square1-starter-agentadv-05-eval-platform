"""Contract tests for the Agent Evaluation Platform."""

import pytest

from src.benchmark import BenchmarkSuite, BenchmarkCase, BenchmarkResult
from src.judge import LLMJudge
from src.regression import RegressionDetector


class TestBenchmarkSuite:
    """Benchmark suite must run all cases and collect results."""

    def test_benchmark_suite_runs_all_cases(self):
        cases = [
            BenchmarkCase(case_id="q1", input_text="What is 2+2?", expected_output="4"),
            BenchmarkCase(case_id="q2", input_text="Capital of France?", expected_output="Paris"),
        ]
        suite = BenchmarkSuite(cases=cases)

        def dummy_agent(text: str) -> str:
            return "test"

        results = suite.run_benchmark(dummy_agent)

        assert isinstance(results, list), "Results must be a list"
        assert len(results) == 2, "Must produce one result per case"
        assert all(isinstance(r, BenchmarkResult) for r in results), \
            "Each result must be a BenchmarkResult"


class TestLLMJudge:
    """Judge must produce structured scores."""

    def test_judge_produces_structured_scores(self):
        judge = LLMJudge()
        score = judge.score_response(
            question="What is machine learning?",
            response="ML is a subset of AI that learns from data.",
        )

        assert 0.0 <= score.relevance <= 1.0, "Relevance must be 0-1"
        assert 0.0 <= score.accuracy <= 1.0, "Accuracy must be 0-1"
        assert 0.0 <= score.completeness <= 1.0, "Completeness must be 0-1"
        assert 0.0 <= score.overall <= 1.0, "Overall must be 0-1"
        assert len(score.reasoning) > 0, "Must provide reasoning"


class TestRegressionDetector:
    """Regression detector must flag performance degradation."""

    def test_regression_detector_flags_degradation(self):
        detector = RegressionDetector()

        baseline = [
            BenchmarkResult(case_id="q1", actual_output="4", passed=True, score=0.95, latency_ms=100),
            BenchmarkResult(case_id="q2", actual_output="Paris", passed=True, score=0.90, latency_ms=120),
        ]
        current = [
            BenchmarkResult(case_id="q1", actual_output="4", passed=True, score=0.50, latency_ms=100),
            BenchmarkResult(case_id="q2", actual_output="London", passed=False, score=0.30, latency_ms=200),
        ]

        report = detector.compare_runs(baseline, current)

        assert report.has_regression is True, "Must detect regression"
        assert len(report.alerts) > 0, "Must produce at least one alert"
        assert report.alerts[0].degradation_pct > 0, "Degradation must be positive"
