use pyo3::prelude::*;
use rust_ti::standard_indicators as si;

/// The `standard_indicators` module provides implementations of widely-recognized technical indicators,
/// following their established formulas and default parameters as commonly found in financial literature and platforms.
///
/// ## When to Use
/// Use these functions when you need classic, industry-standard indicators for:
/// - Quick benchmarking
/// - Reproducing signals used by major charting tools or trading strategies
/// - Comparing with custom or alternative indicator settings
///
/// ## Structure
/// - **single**: Functions that return a single value for a slice of prices.
/// - **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
#[pymodule]
pub fn standard_indicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

/// **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(bulk_simple_moving_average, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_smoothed_moving_average,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_exponential_moving_average,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_bollinger_bands, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_macd, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_rsi, &bulk_module)?)?;
    parent_module.add_submodule(&bulk_module)?;
    Ok(())
}

/// **single**: Functions that return a single value for a slice of prices.
fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(
        single_simple_moving_average,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(
        single_smoothed_moving_average,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(
        single_exponential_moving_average,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(single_bollinger_bands, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_macd, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_rsi, &single_module)?)?;
    parent_module.add_submodule(&single_module)?;
    Ok(())
}

// Simple Moving Average

/// Calculates the simple moving average
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     Simple moving average
#[pyfunction(name = "simple_moving_average")]
fn single_simple_moving_average(prices: Vec<f64>) -> PyResult<f64> {
    Ok(si::single::simple_moving_average(&prices))
}

/// Calculates the simple moving average
///
/// Args:
///     prices: List of prices
///     period: Period over which to calculate the moving average
///
/// Returns:
///     List of simple moving averages
#[pyfunction(name = "simple_moving_average")]
fn bulk_simple_moving_average(prices: Vec<f64>, period: usize) -> PyResult<Vec<f64>> {
    Ok(si::bulk::simple_moving_average(&prices, period))
}

// Smoothed Moving Average

/// Calculates the smoothed moving averages
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     Smoothed moving average
#[pyfunction(name = "smoothed_moving_average")]
fn single_smoothed_moving_average(prices: Vec<f64>) -> PyResult<f64> {
    Ok(si::single::smoothed_moving_average(&prices))
}

/// Calculates the smoothed moving averages
///
/// Args:
///     prices: List of prices
///     period: Period over which to calculate the moving average
///
/// Returns:
///     List of smoothed moving averages
#[pyfunction(name = "smoothed_moving_average")]
fn bulk_smoothed_moving_average(prices: Vec<f64>, period: usize) -> PyResult<Vec<f64>> {
    Ok(si::bulk::smoothed_moving_average(&prices, period))
}

// Exponential Moving Average

/// Calculates the exponential moving average
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     Exponential moving average
#[pyfunction(name = "exponential_moving_average")]
fn single_exponential_moving_average(prices: Vec<f64>) -> PyResult<f64> {
    Ok(si::single::exponential_moving_average(&prices))
}

/// Calculates the exponential moving average
///
/// Args:
///     prices: List of prices
///     period: Period over which to calculate the moving average
///
/// Returns:
///     List of exponential moving averages
#[pyfunction(name = "exponential_moving_average")]
fn bulk_exponential_moving_average(prices: Vec<f64>, period: usize) -> PyResult<Vec<f64>> {
    Ok(si::bulk::exponential_moving_average(&prices, period))
}

// Bollinger Bands

/// Calculates Bollinger bands
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     Bollinger band tuple (lower band, MA, upper band)
#[pyfunction(name = "bollinger_bands")]
fn single_bollinger_bands(prices: Vec<f64>) -> PyResult<(f64, f64, f64)> {
    Ok(si::single::bollinger_bands(&prices))
}

/// Calculates Bollinger bands
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     List of Bollinger band tuples (lower band, MA, upper band)
#[pyfunction(name = "bollinger_bands")]
fn bulk_bollinger_bands(prices: Vec<f64>) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(si::bulk::bollinger_bands(&prices))
}

// MACD

/// Calculates the MACD, signal line, and MACD histogram
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     MACD tuple (MACD, Signal Line, Histogram)
#[pyfunction(name = "macd")]
fn single_macd(prices: Vec<f64>) -> PyResult<(f64, f64, f64)> {
    Ok(si::single::macd(&prices))
}

/// Calculates the MACD, signal line, and MACD histogram
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     List of MACD tuple (MACD, Signal Line, Histogram)

#[pyfunction(name = "macd")]
fn bulk_macd(prices: Vec<f64>) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(si::bulk::macd(&prices))
}

// RSI

/// Calculates the Relative Strength Index (RSI)
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     Relative Strength Index
#[pyfunction(name = "rsi")]
fn single_rsi(prices: Vec<f64>) -> PyResult<f64> {
    Ok(si::single::rsi(&prices))
}

/// Calculates the Relative Strength Index (RSI)
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     List of Relative Strength Index
#[pyfunction(name = "rsi")]
fn bulk_rsi(prices: Vec<f64>) -> PyResult<Vec<f64>> {
    Ok(si::bulk::rsi(&prices))
}
