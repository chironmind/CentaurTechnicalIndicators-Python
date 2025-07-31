use pyo3::prelude::*;
use rust_ti::other_indicators as oi;

/// The `other_indicators` module provides technical analysis tools that do not fit neatly
/// into the main categories like momentum, trend, or volatility.
///
/// These calculations often serve as foundational measures or are used as components of broader strategies.
///
/// ## When to Use
/// Use these functions when you need to:
/// - Calculate foundational metrics for risk, volatility, or bar strength
/// - Analyze price movement range or return over a period
/// - Incorporate less common but valuable technical measures into your models
///
/// ## Structure
/// - **single**: Functions that return a single value for a slice of prices.
/// - **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
#[pymodule]
pub fn other_indicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

/// **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(bulk_return_on_investment, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_true_range, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_average_true_range, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_internal_bar_strength, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_positivity_indicator, &bulk_module)?)?;
    parent_module.add_submodule(&bulk_module)?;
    Ok(())
}

/// **single**: Functions that return a single value for a slice of prices.
fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(
        single_return_on_investment,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(single_true_range, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_average_true_range, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(
        single_internal_bar_strength,
        &single_module
    )?)?;
    parent_module.add_submodule(&single_module)?;
    Ok(())
}

// Return on Investment

/// Calculates the final value and percentage return of an investment
///
/// Args:
///     start_price: Initial price of the asset
///     end_price: Final price of the asset
///     investment: Amount invested at start
///
/// Returns:
///     Tuple of (final investment value, percentage return)
#[pyfunction(name = "return_on_investment")]
fn single_return_on_investment(
    start_price: f64,
    end_price: f64,
    investment: f64,
) -> PyResult<(f64, f64)> {
    Ok(oi::single::return_on_investment(
        start_price,
        end_price,
        investment,
    ))
}

/// Calculates the return on investment and percent return over a period
///
/// Args:
///     prices: List of prices
///     investment: Initial investment
///
/// Returns:
///     List of tuples containing (final investment value, percentage return)
#[pyfunction(name = "return_on_investment")]
fn bulk_return_on_investment(prices: Vec<f64>, investment: f64) -> PyResult<Vec<(f64, f64)>> {
    Ok(oi::bulk::return_on_investment(&prices, investment))
}

// True Range

/// Calculates the True Range (TR)
///
/// Args:
///     previous_close: Previous period close
///     high: Current period high
///     low: Current period low
///
/// Returns:
///     True Range value
#[pyfunction(name = "true_range")]
fn single_true_range(close: f64, high: f64, low: f64) -> PyResult<f64> {
    Ok(oi::single::true_range(close, high, low))
}

/// Calculates the True Range for a series of prices
///
/// Args:
///     close: List of previous closes
///     high: List of highs
///     low: List of lows
///
/// Returns:
///     List of True Range values
#[pyfunction(name = "true_range")]
fn bulk_true_range(close: Vec<f64>, high: Vec<f64>, low: Vec<f64>) -> PyResult<Vec<f64>> {
    Ok(oi::bulk::true_range(&close, &high, &low))
}

// Average True Range

/// Calculates the Average True Range (ATR)
///
/// Args:
///     close: List of previous closes
///     high: List of highs
///     low: List of lows
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Average True Range value
#[pyfunction(name = "average_true_range")]
fn single_average_true_range(
    close: Vec<f64>,
    high: Vec<f64>,
    low: Vec<f64>,
    constant_model_type: &str,
) -> PyResult<f64> {
    Ok(oi::single::average_true_range(
        &close,
        &high,
        &low,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}

/// Calculates the Average True Range (ATR) over a period
///
/// Args:
///     close: List of previous closes
///     high: List of highs
///     low: List of lows
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     period: Period over which to calculate the ATR
///
/// Returns:
///     List of Average True Range values
#[pyfunction(name = "average_true_range")]
fn bulk_average_true_range(
    close: Vec<f64>,
    high: Vec<f64>,
    low: Vec<f64>,
    constant_model_type: &str,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(oi::bulk::average_true_range(
        &close,
        &high,
        &low,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        period,
    ))
}

// Internal Bar Strength

/// Calculates the internal bar strength
///
/// Args:
///     high: High price
///     low: Low price
///     close: Close price
///
/// Returns:
///     Internal bar strength value
#[pyfunction(name = "internal_bar_strength")]
fn single_internal_bar_strength(high: f64, low: f64, close: f64) -> PyResult<f64> {
    Ok(oi::single::internal_bar_strength(high, low, close))
}

/// Calculates the internal bar strength for a series of prices
///
/// Args:
///     high: List of highs
///     low: List of lows
///     close: List of closing prices
///
/// Returns:
///     List of internal bar strength values
#[pyfunction(name = "internal_bar_strength")]
fn bulk_internal_bar_strength(
    high: Vec<f64>,
    low: Vec<f64>,
    close: Vec<f64>,
) -> PyResult<Vec<f64>> {
    Ok(oi::bulk::internal_bar_strength(&high, &low, &close))
}

// Positivity Indicator

/// Calculates the positivity indicator and its signal line
///
/// Args:
///     open: List of opening prices
///     previous_close: List of closing prices
///     signal_period: Period to calculate the signal
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     List of tuples containing (positivity indicator, signal line)
#[pyfunction(name = "positivity_indicator")]
fn bulk_positivity_indicator(
    open: Vec<f64>,
    previous_close: Vec<f64>,
    signal_period: usize,
    constant_model_type: &str,
) -> PyResult<Vec<(f64, f64)>> {
    Ok(oi::bulk::positivity_indicator(
        &open,
        &previous_close,
        signal_period,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}
