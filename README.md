# Agent Evaluation Platform — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · LLM Agent Architect Advanced · Project 5.**

🤖 **Agent project.** This repo provides the project scaffold, function stubs, and contract tests. Read the full brief on Square 1 for guidance.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# P5: Agent Evaluation Platform

Build a platform for systematically benchmarking, scoring, and regression-testing LLM agents using automated evaluation suites and LLM-as-judge scoring.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # Add your ANTHROPIC_API_KEY
```

## Usage

```bash
python -m src.cli --benchmark my_suite.json --output results/
```

## Running Tests

```bash
pytest tests/ -v
```

## Project Structure

```
src/
  benchmark.py    — Benchmark suite runner
  judge.py        — LLM-as-judge response scoring
  regression.py   — Regression detection across runs
  dashboard.py    — Report generation
  cli.py          — Command-line interface
tests/
  test_eval.py    — Contract tests
```
