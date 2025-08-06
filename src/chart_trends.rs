use pyo3::prelude::*;
use rust_ti::chart_trends as ct;

/// The `chart_trends` module provides utilities for detecting, analyzing, and breaking down trends in price charts.
///
/// These functions help identify overall direction, peaks, valleys, and trend segments in a time series.
///
/// ## When to Use
/// Use chart trend indicators to:
/// - Decompose a price series into upward/downward trends
/// - Find peaks and valleys for support/resistance analysis
/// - Quantify the overall or local trend direction of an asset
#[pymodule]
pub fn chart_trends(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(peaks, m)?)?;
    m.add_function(wrap_pyfunction!(valleys, m)?)?;
    m.add_function(wrap_pyfunction!(peak_trend, m)?)?;
    m.add_function(wrap_pyfunction!(valley_trend, m)?)?;
    m.add_function(wrap_pyfunction!(overall_trend, m)?)?;
    m.add_function(wrap_pyfunction!(break_down_trends, m)?)?;
    Ok(())
}

/// Calculates all peaks over a given period
///
/// Args:
///     prices: List of prices
///     period: Period over which to find the peak
///     closest_neighbor: Minimum distance between peaks
///
/// Returns:
///     List of tuples containing (peak value, peak index)
#[pyfunction]
fn peaks(prices: Vec<f64>, period: usize, closest_neighbor: usize) -> PyResult<Vec<(f64, usize)>> {
    Ok(ct::peaks(&prices, period, closest_neighbor))
}

/// Calculates all valleys for a given period
///
/// Args:
///     prices: List of prices
///     period: Period over which to find the valley
///     closest_neighbor: Minimum distance between valleys
///
/// Returns:
///     List of tuples containing (valley value, valley index)
#[pyfunction]
fn valleys(
    prices: Vec<f64>,
    period: usize,
    closest_neighbor: usize,
) -> PyResult<Vec<(f64, usize)>> {
    Ok(ct::valleys(&prices, period, closest_neighbor))
}

/// Returns the slope and intercept of the trend line fitted to peaks
///
/// Args:
///     prices: List of prices
///     period: Period over which to calculate the peaks
///
/// Returns:
///     Tuple containing (slope, intercept) of the peak trend line
#[pyfunction]
fn peak_trend(prices: Vec<f64>, period: usize) -> PyResult<(f64, f64)> {
    Ok(ct::peak_trend(&prices, period))
}

/// Calculates the slope and intercept of the trend line fitted to valleys
///
/// Args:
///     prices: List of prices
///     period: Period over which to calculate the valleys
///
/// Returns:
///     Tuple containing (slope, intercept) of the valley trend line
#[pyfunction]
fn valley_trend(prices: Vec<f64>, period: usize) -> PyResult<(f64, f64)> {
    Ok(ct::valley_trend(&prices, period))
}

/// Calculates the slope and intercept of the trend line fitted to all prices
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     Tuple containing (slope, intercept) of the overall trend line
#[pyfunction]
fn overall_trend(prices: Vec<f64>) -> PyResult<(f64, f64)> {
    Ok(ct::overall_trend(&prices))
}

/// Calculates price trends and their slopes and intercepts
///
/// Args:
///     prices: List of prices
///     max_outliers: Allowed consecutive trend-breaks before splitting
///     soft_r_squared_minimum: Soft minimum value for r squared
///     soft_r_squared_maximum: Soft maximum value for r squared
///     hard_r_squared_minimum: Hard minimum value for r squared
///     hard_r_squared_maximum: Hard maximum value for r squared
///     soft_standard_error_multiplier: Soft standard error multiplier
///     hard_standard_error_multiplier: Hard standard error multiplier
///     soft_reduced_chi_squared_multiplier: Soft chi squared multiplier
///     hard_reduced_chi_squared_multiplier: Hard chi squared multiplier
///
/// Returns:
///     List of tuples containing (start_index, end_index, slope, intercept) for each trend segment
#[pyfunction]
fn break_down_trends(
    prices: Vec<f64>,
    max_outliers: usize,
    soft_r_squared_minimum: f64,
    soft_r_squared_maximum: f64,
    hard_r_squared_minimum: f64,
    hard_r_squared_maximum: f64,
    soft_standard_error_multiplier: f64,
    hard_standard_error_multiplier: f64,
    soft_reduced_chi_squared_multiplier: f64,
    hard_reduced_chi_squared_multiplier: f64,
) -> PyResult<Vec<(usize, usize, f64, f64)>> {
    Ok(ct::break_down_trends(
        &prices,
        max_outliers,
        soft_r_squared_minimum,
        soft_r_squared_maximum,
        hard_r_squared_minimum,
        hard_r_squared_maximum,
        soft_standard_error_multiplier,
        hard_standard_error_multiplier,
        soft_reduced_chi_squared_multiplier,
        hard_reduced_chi_squared_multiplier,
    ))
}
