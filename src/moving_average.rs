use pyo3::prelude::*;
use rust_ti::moving_average as ma;

/// The `moving_average` module provides functions for calculating moving averages, a core component of many technical indicators and trading strategies.
///
/// ## Structure
/// - **single**: Functions that return a single value for a slice of prices.
/// - **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
#[pymodule]
pub fn moving_average(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

/// **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(bulk_moving_average, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_mcginley_dynamic, &bulk_module)?)?;
    parent_module.add_submodule(&bulk_module)?;
    Ok(())
}

/// **single**: Functions that return a single value for a slice of prices.
fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(single_moving_average, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_mcginley_dynamic, &single_module)?)?;
    parent_module.add_submodule(&single_module)?;
    Ok(())
}

/// Calculates the Moving Average
///
/// Args:
///     prices: List of prices
///     moving_average_type: Choice of "simple", "smoothed", "exponential"
///
/// Returns:
///     Moving average
#[pyfunction(name = "moving_average")]
fn single_moving_average(prices: Vec<f64>, moving_average_type: &str) -> PyResult<f64> {
    Ok(ma::single::moving_average(
        &prices,
        crate::PyMovingAverageType::from_string(moving_average_type)?.into(),
    ))
}

/// Calculates the Moving Average over a rolling period
///
/// Args:
///     prices: List of prices
///     moving_average_type: Choice of "simple", "smoothed", "exponential"
///     period: Period over which to calculate the moving average
///
/// Returns:
///     List of moving averages
#[pyfunction(name = "moving_average")]
fn bulk_moving_average(
    prices: Vec<f64>,
    moving_average_type: &str,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(ma::bulk::moving_average(
        &prices,
        crate::PyMovingAverageType::from_string(moving_average_type)?.into(),
        period,
    ))
}

/// Calculates the McGinley dynamic
///
/// Args:
///     latest_price: Most recent price
///     previous_mcginley_dynamic: Previous McGinley dynamic (if none 0.0)
///     period: Length of the observed period
///
/// Returns:
///     McGinley dynamic
#[pyfunction(name = "mcginley_dynamic")]
fn single_mcginley_dynamic(
    latest_price: f64,
    previous_mcginley_dynamic: f64,
    period: usize,
) -> PyResult<f64> {
    Ok(ma::single::mcginley_dynamic(
        latest_price,
        previous_mcginley_dynamic,
        period,
    ))
}

/// Calculates the McGinley dynamic
///
/// Args:
///     prices: List of prices
///     previous_mcginley_dynamic: Previous McGinley dynamic (if none 0.0)
///     period: Period over which to calculate the McGinley dynamic
///
/// Returns:
///     List of McGinley dynamics
#[pyfunction(name = "mcginley_dynamic")]
fn bulk_mcginley_dynamic(
    prices: Vec<f64>,
    previous_mcginley_dynamic: f64,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(ma::bulk::mcginley_dynamic(
        &prices,
        previous_mcginley_dynamic,
        period,
    ))
}
