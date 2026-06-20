[![PyPI Version](https://img.shields.io/pypi/v/centaur_technical_indicators.svg)](https://pypi.org/project/centaur-technical-indicators/)
[![PyPI Downloads](https://pepy.tech/badge/centaur_technical_indicators)](https://pypi.org/project/centaur-technical-indicators/)
![Python Versions](https://img.shields.io/pypi/pyversions/centaur_technical_indicators)
[![CI](https://github.com/chironmind/CentaurTechnicalIndicators-Python/actions/workflows/python-package.yml/badge.svg)](https://github.com/chironmind/CentaurTechnicalIndicators-Python/actions)
[![License](https://img.shields.io/github/license/chironmind/CentaurTechnicalIndicators-Python)](LICENSE-MIT)

[![Docs - ReadTheDocs](https://img.shields.io/badge/docs-latest-brightgreen?logo=readthedocs)](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/)
[![Docs - GitHub Pages](https://img.shields.io/badge/docs-github%20pages-blue?logo=github)](https://chironmind.github.io/CentaurTechnicalIndicators-Python-Docs/)
[![Tutorials](https://img.shields.io/badge/Tutorials-Available-brightgreen?style=flat&logo=book)](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/tutorials)
[![Benchmarks](https://img.shields.io/badge/Performance-Microsecond-blue?logo=zap)](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/benchmarks)

# Centaur Technical Indicators

A production-ready Python library providing 50+ technical indicators for financial analysis, built on a high-performance Rust backend.

Part of the CRT (Centaur Research & Technologies) ecosystem.

Looking for the Rust crate? See: [ChironMind/CentaurTechnicalIndicators-Rust](https://github.com/ChironMind/CentaurTechnicalIndicators-Rust)

Looking for the WASM bindings? See: [ChironMind/CentaurTechnicalIndicators-JS](https://github.com/chironmind/CentaurTechnicalIndicators-JS)

---

## 🚀 Getting Started

**1. Install the package:**

```shell
pip install centaur_technical_indicators
```

**2. Calculate your first indicator:**

```python
import centaur_technical_indicators as cti

prices = [100.2, 100.46, 100.53, 100.38, 100.19]

ma = cti.moving_average.single.moving_average(
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

- [01 - Using with pandas](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/tutorials/pandas/)
- [02 - Using with Plotly](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/tutorials/plotly/)
- [03 - Advanced use cases](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/tutorials/advanced/)
- [04 - Connecting to an API](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/tutorials/api_connection/)
---

## 🛠️ How-To Guides

> Task-oriented guides for common problems and advanced scenarios.

- [How to pick Bulk vs Single](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/howto/bulk_vs_single/)
- [How to choose a Constant Model Type](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/howto/choose_constant_model_type/)
- [How to choose a Deviation Model](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/howto/choose_deviation_model/)
- [How to choose a period](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/howto/choose_period/)
- [How to use the McGinley dynamic function variations](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/howto/mcginley_dynamic/)

---

## 📚 Reference

The API reference can be found [here](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/api/)

### Examples

A reference of how to call each function can be found in the tests:

- [Reference Examples](./tests/)

Clone and run:

```shell
$ source you_venv_location/bin/activate

$ pip3 install -r test_requirements.txt

$ maturin develop

$ pytest .

```

### Library Structure

- Modules based on their analysis areas (**`moving_average`**, **`momentum_indicators`**, **`strength_indicators`**...)
- Most modules have both `bulk` and `single` sub-modules:
  - `bulk`: Compute indicator over rolling periods, returns a list.
  - `single`: Compute indicator for the entire list, returns a single value.
- **Exceptions (asymmetric shape):**
  - `chart_trends` — flat module (no `single`/`bulk` sub-modules; functions are top-level).
  - `volatility_indicators` — `ulcer_index` has `single` only; `volatility_system` is `bulk` only.
  - `other_indicators`, `strength_indicators`, and `trend_indicators` are asymmetric (not every
    indicator has both variants).
- `types` used to personalise the technical indicators (**`moving_average_type`**, **`deviation_model`**, **`constant_model_type`**...)

---

## 🧠 Explanation & Design

### Why Centaur Technical Indicators?

- **Performance:** Rust-powered backend for maximal speed, safety, and low overhead.
- **Configurability:** Most indicators are highly customizable—tweak calculation methods, periods, or even use medians instead of means.
- **Breadth:** Covers a wide range of technical indicators out of the box.
- **Advanced Use:** Designed for users who understand technical analysis and want deep control.

**Note:** Some features may require background in technical analysis. See [Investopedia: Technical Analysis](https://www.investopedia.com/terms/t/technicalanalysis.asp) for a primer.

---

## 📈 Available Indicators

All indicators are grouped and split into modules based on their analysis area.

### Candle Indicators
- Ichimoku Cloud, Moving Constant Bands/Envelopes, Donchian Channels, Keltner, Supertrend,
  McGinley Dynamic Envelopes, McGinley Dynamic Bands

### Chart Trends
- Trend break down, overall trends, peak/valley trends, peak favorable move, valley favorable move

### Correlation Indicators
- Correlate asset prices

### Momentum Indicators
- Chaikin Oscillator, CCI, MACD, Money Flow Index, On Balance Volume, ROC, RSI, Williams %R,
  Stochastic Oscillator, Slow Stochastic, Slowest Stochastic, Percentage Price Oscillator (PPO),
  Chande Momentum Oscillator (CMO), Signal Line (MACD signal),
  McGinley Dynamic Commodity Channel Index, McGinley Dynamic MACD Line

### Moving Averages
- McGinley Dynamic, Moving Average

### Other Indicators
- ROI, True Range, ATR, Internal Bar Strength, Positivity Indicator

### Strength Indicators
- Accumulation/Distribution, PVI, NVI, RVI, Volume Index

### Trend Indicators
- Aroon (Up/Down/Oscillator), Parabolic, DM, Volume-Price Trend, TSI

### Volatility Indicators
- Ulcer Index, Volatility System

**Note on scope:** Statistical primitives available in Python's `statistics` / `math` modules
(the Rust `basic_indicators` surface) are intentionally not re-bound. Use the standard library
directly for those.

---

## 📊 Performance Benchmarks

Want to know how fast the library runs in real-world scenarios?  
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

Browse all benchmark tables
- [CentaurTechnicalIndicators-Python Benchmarks](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/benchmarks/)

*(Your results may vary depending on platform and Python environment.)*

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!
- [Open an issue](https://github.com/chironmind/CentaurTechnicalIndicators-Python/issues)
- [Submit a pull request](https://github.com/chironmind/CentaurTechnicalIndicators-Python/pulls)
- See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines

---

## 💬 Community & Support

- Start a [discussion](https://github.com/chironmind/CentaurTechnicalIndicators-Python/discussions)
- File [issues](https://github.com/chironmind/CentaurTechnicalIndicators-Python/issues)
- Add your project to the [Showcase](https://github.com/chironmind/CentaurTechnicalIndicators-Python/discussions/categories/show-and-tell)

---

## 📰 Release Notes

**Latest:** See [CHANGELOG.md](./CHANGELOG.md) for details.

**Full changelog:** See [Releases](https://github.com/chironmind/CentaurTechnicalIndicators-Python/releases) for details

---

## 📄 License

MIT License. See [LICENSE](LICENSE-MIT).

---

## 📚 More Documentation

This repository is part of a structured documentation suite:

- 📕 **Tutorials:** — [See here](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/tutorials/)
- 📘 **How-To Guides:** — [See here](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/howto/)
- ⏱️ **Benchmarks:** — [See here](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/benchmarks/)
- 📙 **Explanations:** — [tech.centaurresearchtechnologies.com](https://tech.centaurresearchtechnologies.com/)
- 📗 **Reference:** — [See here](https://centaurtechnicalindicators-python.readthedocs.io/en/latest/api/)
 
---
