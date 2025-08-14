![PyTechnicalIndicators Banner](https://github.com/chironmind/PyTechnicalIndicators/blob/main/assets/pytechnicalindicators_banner.png)

[![PyPI Version](https://img.shields.io/pypi/v/pytechnicalindicators.svg)](https://pypi.org/project/pytechnicalindicators/)
[![PyPI Downloads](https://pepy.tech/badge/pytechnicalindicators)](https://pypi.org/project/pytechnicalindicators/)
![Python Versions](https://img.shields.io/pypi/pyversions/pytechnicalindicators)
[![CI](https://github.com/chironmind/PyTechnicalIndicators/actions/workflows/python-package.yml/badge.svg)](https://github.com/chironmind/PyTechnicalIndicators/actions)
[![License](https://img.shields.io/github/license/chironmind/PyTechnicalIndicators)](LICENSE-MIT)

[![Docs - ReadTheDocs](https://img.shields.io/badge/docs-latest-brightgreen?logo=readthedocs)](https://pytechnicalindicators-docs.readthedocs.io/en/latest/)
[![Docs - GitHub Pages](https://img.shields.io/badge/docs-github%20pages-blue?logo=github)](https://chironmind.github.io/PyTechnicalIndicators-docs/)
[![Tutorials](https://img.shields.io/badge/Tutorials-Available-brightgreen?style=flat&logo=book)](https://github.com/chironmind/PyTechnicalIndicators_tutorials)
[![Benchmarks](https://img.shields.io/badge/Performance-Microsecond-blue?logo=zap)](https://github.com/chironmind/PyTechnicalIndicators-benchmarks)

# 🐍 Meet PyTechnicalIndicators

Say hello to PyTechnicalIndicators, the Python-powered bridge to the battle-tested performance of RustTI! 🦀🐍📈

Built on top of the RustTI core, PyTechnicalIndicators brings blazing-fast technical indicators to Python, perfect for quants, traders, and anyone who needs robust, high-performance financial analytics in their Python workflows.

Welcome to PyTechnicalIndicators — powered by Rust, ready for Python.

Looking for the Rust crate? See: [ChironMind/RustTI](https://github.com/ChironMind/RustTI)

Looking for the WASM bindings? See: [ChironMind/ti-engine](https://github.com/chironmind/ti-engine)

---

## 🚀 Getting Started

> The fastest way to get up and running with PyTechnicalIndicators.

**1. Install PyTechnicalIndicators:**

```shell
pip install pytechnicalindicators
```

**2. Calculate your first indicator:**

```python
import pytechnicalindicators as pti

prices = [100.2, 100.46, 100.53, 100.38, 100.19]

ma = pti.moving_average(
    prices,
    "simple"
)
print(f"Simple Moving Average: {ma}")
```

Expected output:
```
Simple Moving Average: 100.352
```

**3. Explore more tutorials**

- [01 - Using PyTechnicalIndicators with pandas](https://github.com/chironmind/PyTechnicalIndicators_Tutorials/blob/main/01_pandas_and_pytechnicalindicators.md)
- [02 - Using PyTechnicalIndicators with Plotly](https://github.com/chironmind/PyTechnicalIndicators_Tutorials/blob/main/02_using_plotly_and_pytechnicalindicators.md)
- [03 - More advanced use cases for PyTechnicalIndicators](https://github.com/chironmind/PyTechnicalIndicators_Tutorials/blob/main/03_advanced_pytechnicalindicators.md)
- [04 - Connecting to an API](https://github.com/chironmind/PyTechnicalIndicators_Tutorials/blob/main/04_api_connection.md)
- [05 - Using PyTechnicalIndicators with Jupyter Notebooks](https://github.com/chironmind/PyTechnicalIndicators_Tutorials/blob/main/05_using_jupyter_and_pytechnicalindicators.ipynb)

---

## 🛠️ How-To Guides

> Task-oriented guides for common problems and advanced scenarios.

- [How to pick Bulk vs Single](https://github.com/chironmind/PyTechnicalIndicators-How-To-guides/blob/main/bulk_vs_single.md)
- [How to choose a Constant Model Type](https://github.com/chironmind/PyTechnicalIndicators-How-To-guides/blob/main/choose_constant_model_type.md)
- [How to choose a Deviation Model](https://github.com/chironmind/PyTechnicalIndicators-How-To-guides/blob/main/choose_deviation_model.md)
- [How to choose a period](https://github.com/chironmind/PyTechnicalIndicators-How-To-guides/blob/main/choose_period.md)
- [How to use the McGinley dynamic function variations](https://github.com/chironmind/PyTechnicalIndicators-How-To-guides/blob/main/mcginley_dynamic.md)

---

## 📚 Reference


The API reference can be found [here](https://pytechnicalindicators-docs.readthedocs.io/en/latest/api/)

### Example

A reference of how to call each function can be found in the tests:

- [Reference Example](./tests/)

Clone and run:

```shell
$ source you_venv_location/bin/activate

$ pip3 install -r test_requirements.txt

$ maturin develop

$ pytest .

```

### Library Structure

- Modules based on their analysis areas (**`moving_average`**, **`momentum_indicators`**, **`strength_indicators`**...)
- `bulk` & `single` function variants  
  - `bulk`: Compute indicator over rolling periods, returns a list.
  - `single`: Compute indicator for the entire list, returns a single value.
- Types used to personalise the technical indicators (**`moving_average_type`**, **`deviation_model`**, **`contant_model_type`**...)

---

## 🧠 Explanation & Design

### Why PyTechnicalIndicators?

- **Performance:** Rust-powered backend for maximal speed, safety, and low overhead.
- **Configurability:** Most indicators are highly customizable—tweak calculation methods, periods, or even use medians instead of means.
- **Breadth:** Covers a wide range of technical indicators out of the box.
- **Advanced Use:** Designed for users who understand technical analysis and want deep control.

**Note:** Some features may require background in technical analysis. See [Investopedia: Technical Analysis](https://www.investopedia.com/terms/t/technicalanalysis.asp) for a primer.

---

## 📈 Available Indicators

All indicators are grouped and split into modules based on their analysis area.  
Each module has `bulk` (list output) and `single` (scalar output) functions.

### Standard Indicators
- Simple, Smoothed, Exponential Moving Average, Bollinger Bands, MACD, RSI

### Candle Indicators
- Ichimoku Cloud, Moving Constant Bands/Envelopes, Donchian Channels, Keltner, Supertrend

### Chart Trends
- Trend break down, overall trends, peak/valley trends

### Correlation Indicators
- Correlate asset prices

### Momentum Indicators
- Chaikin Oscillator, CCI, MACD, Money Flow Index, On Balance Volume, ROC, RSI, Williams %R

### Moving Averages
- McGinley Dynamic, Moving Average

### Other Indicators
- ROI, True Range, ATR, Internal Bar Strength

### Strength Indicators
- Accumulation/Distribution, PVI, NVI, RVI

### Trend Indicators
- Aroon (Up/Down/Oscillator), Parabolic, DM, Volume-Price Trend, TSI

### Volatility Indicators
- Ulcer Index, Volatility System

---

## 📊 Performance Benchmarks

Want to know how fast PyTechnicalIndicators runs in real-world scenarios?  
We provide detailed, reproducible benchmarks using realistic OHLCV data and a variety of indicators.

## Benchmarks summary (Raspberry Pi 5)

All results are produced on a Raspberry Pi 5 (RPi5) and reported as microseconds per call (min/mean/median) and derived ops/sec. Each suite is run in two modes:
- single: run the indicator repeatedly for timing small, per-call latency
- bulk: process larger arrays to measure throughput-oriented workloads

Headline observations from the momentum suite (large 10Y dataset)
- Ultra‑lightweight indicators achieve sub‑microsecond latency per call:
  - ROC single: ~0.11 µs (≈8.72e+06 ops/sec); bulk: ~86 µs (≈1.16e+04 ops/sec)
  - OBV single: ~0.13 µs (≈7.85e+06 ops/sec); bulk: ~130 µs (≈7.7e+03 ops/sec)
- RSI single-call latency ranges roughly 45–115 µs depending on averaging method; bulk ranges ~560–3600 µs
  - Averaging method impact (fast → slow): simple/mean/exponential ≈ median < mode
- Stochastic (fast/slow/slowest) single: ~36–98 µs; bulk: ~109–2600 µs (mode again the slowest)
- CCI families:
  - “standard/mean/median/mode” single calls mostly ~39–155 µs; bulk ~230–3600 µs
  - “ulcer” variant is significantly heavier: single ~6.8–6.9 ms; bulk ~1.0–2.1 ms
- MACD line and signal line single: ~32–80 µs; bulk: ~170–4,000+ µs depending on smoothing and dataset
  - McGinley MACD line single is among the fastest (~32–33 µs); bulk ~300 µs
- Chaikin Oscillator single: ~140–300 µs; bulk: ~500–2,900 µs
- PPO single: ~36–151 µs; bulk: ~175–5,700 µs
- CMO single: ~45 µs; bulk: ~505 µs

These patterns (simple/mean/exponential being fastest; median slightly slower; mode slowest; “ulcer” notably heavy) are consistent across indicator variants and hold across single vs bulk modes.

Small dataset: 1Y daily data
Medium dataset: 5Y daily data
Large dataset: 10Y daily data

Coverage and result files
- Candle indicators: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_candle_indicators_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_candle_indicators_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_candle_indicators_large_benchmark_results.md)
- Chart trends: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_chart_trends_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_chart_trends_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_chart_trends_large_benchmark_results.md)
- Correlation indicators: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_correlation_indicators_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_correlation_indicators_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_correlation_indicators_large_benchmark_results.md)
- Momentum indicators: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_momentum_indicators_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_momentum_indicators_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_momentum_indicators_large_benchmark_results.md)
- Moving averages: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_moving_average_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_moving_average_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_moving_average_large_benchmark_results.md)
- Other indicators: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_other_indicators_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_other_indicators_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_other_indicators_large_benchmark_results.md)
- Standard indicators: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_standard_indicators_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_standard_indicators_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_standard_indicators_large_benchmark_results.md)
- Strength indicators: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_strength_indicators_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_strength_indicators_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_strength_indicators_large_benchmark_results.md)
- Trend indicators: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_trend_indicators_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_trend_indicators_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_trend_indicators_large_benchmark_results.md)
- Volatility indicators: [small](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_volatility_indicators_small_benchmark_results.md) • [medium](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_volatility_indicators_medium_benchmark_results.md) • [large](https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/blob/main/results/markdown/rpi5_volatility_indicators_large_benchmark_results.md)

Browse all benchmark tables
- Folder: https://github.com/chironmind/PyTechnicalIndicators-Benchmarks/tree/main/results/markdown

*(Your results may vary depending on platform and Python environment.)*

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!
- [Open an issue](https://github.com/chironmind/PyTechnicalIndicators/issues)
- [Submit a pull request](https://github.com/chironmind/PyTechnicalIndicators/pulls)
- See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines

---

## 💬 Community & Support

- Start a [discussion](https://github.com/chironmind/PyTechnicalIndicators/discussions)
- File [issues](https://github.com/chironmind/PyTechnicalIndicators/issues)
- Add your project to the [Showcase](https://github.com/chironmind/PyTechnicalIndicators/discussions/categories/show-and-tell)

---

## 📰 Release Notes

**Latest:** See [CHANGELOG.md](./CHANGELOG.md) for details.

**Full changelog:** See [Releases](https://github.com/chironmind/PyTechnicalIndicators/releases) for details

---

## 📄 License

MIT License. See [LICENSE](LICENSE-MIT).

---

## 📚 More Documentation

This repository is part of a structured documentation suite:

- 📕 **Tutorials:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators_Tutorials)
- 📘 **How-To Guides:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators-How-To-guides)
- ⏱️ **Benchmarks:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators-Benchmarks)
- 📙 **Explanations:** — Coming soon
- 📗 **Reference:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators/wiki)
 
---
