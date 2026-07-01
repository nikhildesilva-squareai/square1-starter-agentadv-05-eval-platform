"""LLM-as-judge scoring for agent responses."""

from dataclasses import dataclass


@dataclass
class JudgeScore:
    """Structured score from the LLM judge."""
    relevance: float
    accuracy: float
    completeness: float
    overall: float
    reasoning: str


class LLMJudge:
    """Uses an LLM to score agent responses against criteria."""

    def __init__(self, api_key: str | None = None):
        """Initialise the LLM judge.

        Args:
            api_key: Anthropic API key.
        """
        self.api_key = api_key

    def score_response(
        self,
        question: str,
        response: str,
        *,
        reference: str | None = None,
    ) -> JudgeScore:
        """Score an agent's response using LLM-as-judge.

        Evaluates the response on relevance, accuracy, and completeness,
        optionally comparing against a reference answer.

        Args:
            question: The original question posed to the agent.
            response: The agent's response to evaluate.
            reference: Optional reference (gold) answer for comparison.

        Returns:
            A JudgeScore with per-dimension and overall scores.
        """
        raise NotImplementedError("TODO: implement LLM-as-judge scoring")
