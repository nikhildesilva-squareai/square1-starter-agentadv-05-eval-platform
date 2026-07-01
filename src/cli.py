"""Command-line interface for the Agent Evaluation Platform."""

import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Agent Evaluation Platform")
    parser.add_argument("--benchmark", help="Path to benchmark suite JSON")
    parser.add_argument("--compare", nargs=2, help="Compare two result files")
    parser.add_argument("--output", default="outputs/", help="Output directory")
    parser.add_argument("--api-key", default=os.getenv("ANTHROPIC_API_KEY"))
    args = parser.parse_args()

    print("Agent Evaluation Platform")
    print("Use --benchmark to run a suite or --compare to check regressions.")


if __name__ == "__main__":
    main()
