![PyTechnicalIndicators Banner](https://github.com/chironmind/PyTechnicalIndicators/blob/main/assets/pytechnicalindicators_banner.png)

[![PyPI Version](https://img.shields.io/pypi/v/pytechnicalindicators.svg)](https://pypi.org/project/pytechnicalindicators/)
[![PyPI Downloads](https://pepy.tech/badge/pytechnicalindicators)](https://pypi.org/project/pytechnicalindicators/)
![Python Versions](https://img.shields.io/pypi/pyversions/pytechnicalindicators)
[![CI](https://github.com/chironmind/PyTechnicalIndicators/actions/workflows/python-package.yml/badge.svg)](https://github.com/chironmind/PyTechnicalIndicators/actions)
[![License](https://img.shields.io/github/license/chironmind/PyTechnicalIndicators)](LICENSE-MIT)

[![Docs](https://img.shields.io/badge/docs-available-brightgreen.svg)](https://github.com/chironmind/PyTechnicalIndicators/wiki)
[![Tutorials](https://img.shields.io/badge/Tutorials-Available-brightgreen?style=flat&logo=book)](https://github.com/chironmind/PyTechnicalIndicators_tutorials)
[![Benchmarks](https://img.shields.io/badge/Performance-Microsecond-blue?logo=zap)](https://github.com/chironmind/PyTechnicalIndicators-benchmarks)

# 🐍 Meet PyTechnicalIndicators

Say hello to PyTechnicalIndicators, the Python-powered bridge to the battle-tested performance of RustTI! 🦀🐍📈

Built on top of the RustTI core, PyTechnicalIndicators brings blazing-fast technical indicators to Python, perfect for quants, traders, and anyone who needs robust, high-performance financial analytics in their Python workflows.

Welcome to PyTechnicalIndicators — powered by Rust, ready for Python.

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

**COMING SOON!**

---

## 🛠️ How-To Guides

> Task-oriented guides for common problems and advanced scenarios.

**COMING SOON!**

---

## 📚 Reference

All the information needed to use PyTechnicalIndicators can be found in the [wiki](https://github.com/chironmind/PyTechnicalIndicators/wiki)

The API reference can be found [here](https://github.com/chironmind/PyTechnicalIndicators/wiki/API-Reference)

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

**COMING SOON!**

*(Performance is comparable with native RustTI. Your results may vary depending on platform and Python environment.)*

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
