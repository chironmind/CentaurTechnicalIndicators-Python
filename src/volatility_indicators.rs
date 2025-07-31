use pyo3::prelude::*;
use rust_ti::volatility_indicators as vi;

/// The `volatility_indicators` module provides functions for measuring the volatility of an asset—how much and how quickly prices move over time.
///
/// ## Structure
/// - **single**: Functions that return a single value for a slice of prices.
/// - **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
#[pymodule]
pub fn volatility_indicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

/// **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(bulk_ulcer_index, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_volatility_system, &bulk_module)?)?;
    parent_module.add_submodule(&bulk_module)?;
    Ok(())
}

/// **single**: Functions that return a single value for a slice of prices.
fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(single_ulcer_index, &single_module)?)?;
    parent_module.add_submodule(&single_module)?;
    Ok(())
}

/// Calculates the Ulcer Index
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     Ulcer Index value
#[pyfunction(name = "ulcer_index")]
fn single_ulcer_index(prices: Vec<f64>) -> PyResult<f64> {
    Ok(vi::single::ulcer_index(&prices))
}

/// Calculates the Ulcer Index for a rolling window.
///
/// Args:
///     prices: List of prices
///     period: Period over which to calculate the Ulcer Index
///
/// Returns:
///     List of Ulcer Index values (one per window)
#[pyfunction(name = "ulcer_index")]
fn bulk_ulcer_index(prices: Vec<f64>, period: usize) -> PyResult<Vec<f64>> {
    Ok(vi::bulk::ulcer_index(&prices, period))
}

/// Calculates Welles Wilder's volatility system
///
/// Args:
///     high: List of highs
///     low: List of lows
///     close: List of closing prices
///     period: Period over which to calculate the volatility system
///     constant_multiplier: Multiplier for ATR
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     List of volatility system SaR points
#[pyfunction(name = "volatility_system")]
fn bulk_volatility_system(
    high: Vec<f64>,
    low: Vec<f64>,
    close: Vec<f64>,
    period: usize,
    constant_multiplier: f64,
    constant_model_type: &str,
) -> PyResult<Vec<f64>> {
    Ok(vi::bulk::volatility_system(
        &high,
        &low,
        &close,
        period,
        constant_multiplier,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}
