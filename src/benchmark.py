"""Benchmark suite runner for agent evaluation."""

from dataclasses import dataclass, field


@dataclass
class BenchmarkCase:
    """A single benchmark test case."""
    case_id: str
    input_text: str
    expected_output: str | None
    metadata: dict = field(default_factory=dict)


@dataclass
class BenchmarkResult:
    """Result of running a single benchmark case."""
    case_id: str
    actual_output: str
    passed: bool
    score: float
    latency_ms: float


class BenchmarkSuite:
    """Runs a suite of benchmark cases against an agent."""

    def __init__(self, cases: list[BenchmarkCase] | None = None):
        """Initialise the benchmark suite.

        Args:
            cases: List of benchmark cases to run.
        """
        self.cases = cases or []

    def run_benchmark(self, agent_fn: callable) -> list[BenchmarkResult]:
        """Run all benchmark cases against the provided agent function.

        Executes each case, measures latency, and collects results.

        Args:
            agent_fn: A callable that takes a string input and returns a string.

        Returns:
            A list of BenchmarkResult objects, one per case.
        """
        raise NotImplementedError("TODO: implement benchmark suite execution")
