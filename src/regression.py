"""Regression detection across benchmark runs."""

from dataclasses import dataclass

from .benchmark import BenchmarkResult


@dataclass
class RegressionAlert:
    """An alert for a detected regression."""
    case_id: str
    metric: str
    baseline_value: float
    current_value: float
    degradation_pct: float


@dataclass
class RegressionReport:
    """Summary of regression analysis between two runs."""
    alerts: list[RegressionAlert]
    has_regression: bool
    summary: str


class RegressionDetector:
    """Compares benchmark runs to detect performance regressions."""

    def compare_runs(
        self,
        baseline: list[BenchmarkResult],
        current: list[BenchmarkResult],
        *,
        threshold: float = 0.1,
    ) -> RegressionReport:
        """Compare two benchmark runs and flag regressions.

        Identifies cases where performance has degraded beyond the
        specified threshold between the baseline and current runs.

        Args:
            baseline: Results from the baseline (previous) run.
            current: Results from the current run.
            threshold: Minimum degradation fraction to trigger an alert.

        Returns:
            A RegressionReport with any detected regressions.
        """
        raise NotImplementedError("TODO: implement regression detection logic")
