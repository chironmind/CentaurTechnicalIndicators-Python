use pyo3::prelude::*;
use rust_ti::trend_indicators as ti;

/// The `trend_indicators` module provides functions to analyze and quantify price trends in time series data.
///
/// Trend indicators are used to determine the direction, strength, and potential reversals of market trends.
///
/// ## When to Use
/// Use trend indicators to:
/// - Identify the presence and direction of a trend (uptrend, downtrend, or sideways)
/// - Spot trend reversals or trend exhaustion
/// - Confirm other technical signals
///
/// ## Structure
/// - **single**: Functions that return a single value for a slice of prices.
/// - **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
#[pymodule]
pub fn trend_indicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

/// **bulk**: Functions that compute values over a period and return a vector.
fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(bulk_aroon_up, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_aroon_down, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_aroon_oscillator, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_aroon_indicator, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_parabolic_time_price_system,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_directional_movement_system,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_volume_price_trend, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_true_strength_index, &bulk_module)?)?;
    parent_module.add_submodule(&bulk_module)?;
    Ok(())
}

/// **single**: Functions that return a single value for a slice of prices.
fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(single_aroon_up, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_aroon_down, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_aroon_oscillator, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_aroon_indicator, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(
        single_long_parabolic_time_price_system,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(
        single_short_parabolic_time_price_system,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(single_volume_price_trend, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(
        single_true_strength_index,
        &single_module
    )?)?;
    parent_module.add_submodule(&single_module)?;
    Ok(())
}

// Aroon Up

/// Calculates the Aroon Up indicator
///
/// Args:
///     highs: List of highs
///
/// Returns:
///     Aroon Up value
#[pyfunction(name = "aroon_up")]
fn single_aroon_up(highs: Vec<f64>) -> PyResult<f64> {
    Ok(ti::single::aroon_up(&highs))
}

/// Calculates the Aroon Up indicator
///
/// Args:
///     highs: List of highs
///     period: Period over which to calculate the Aroon up
///
/// Returns:
///     List of Aroon Up values
#[pyfunction(name = "aroon_up")]
fn bulk_aroon_up(highs: Vec<f64>, period: usize) -> PyResult<Vec<f64>> {
    Ok(ti::bulk::aroon_up(&highs, period))
}

// Aroon Down

/// Calculates the Aroon Down indicator
///
/// Args:
///     lows: List of lows
///
/// Returns:
///     Aroon Down value
#[pyfunction(name = "aroon_down")]
fn single_aroon_down(lows: Vec<f64>) -> PyResult<f64> {
    Ok(ti::single::aroon_down(&lows))
}

/// Calculates the Aroon Down indicator
///
/// Args:
///     lows: List of lows
///     period: Period over which to calculate the Aroon down
///
/// Returns:
///     List of Aroon Down values
#[pyfunction(name = "aroon_down")]
fn bulk_aroon_down(lows: Vec<f64>, period: usize) -> PyResult<Vec<f64>> {
    Ok(ti::bulk::aroon_down(&lows, period))
}

// Aroon Oscillator

/// Calculates the Aroon Oscillator
///
/// Args:
///     aroon_up: Aroon Up value
///     aroon_down: Aroon Down value
///
/// Returns:
///     Aroon Oscillator value
#[pyfunction(name = "aroon_oscillator")]
fn single_aroon_oscillator(aroon_up: f64, aroon_down: f64) -> PyResult<f64> {
    Ok(ti::single::aroon_oscillator(aroon_up, aroon_down))
}

/// Calculates the Aroon Oscillator
///
/// Args:
///     aroon_up: List of Aroon Up values
///     aroon_down: List of Aroon Down values
///
/// Returns:
///     List of Aroon Oscillator values
#[pyfunction(name = "aroon_oscillator")]
fn bulk_aroon_oscillator(aroon_up: Vec<f64>, aroon_down: Vec<f64>) -> PyResult<Vec<f64>> {
    Ok(ti::bulk::aroon_oscillator(&aroon_up, &aroon_down))
}

// Aroon Indidcator

/// Calculates the Aroon Indicator
///
/// Args:
///     highs: List of highs
///     lows: List of lows
///
/// Returns:
///     Aroon indicator tuple (Aroon Up, Aroon Down, Aroon Oscillator)
#[pyfunction(name = "aroon_indicator")]
fn single_aroon_indicator(highs: Vec<f64>, lows: Vec<f64>) -> PyResult<(f64, f64, f64)> {
    Ok(ti::single::aroon_indicator(&highs, &lows))
}

/// Calculates Aroon Indicator
///
/// Args:
///     highs: List of highs
///     lows: List of lows
///     period: Period over which to calculate the Aroon indicator
///
/// Returns:
///     List of  Aroon indicator tuples (Aroon Up, Aroon Down, Aroon Oscillator)
#[pyfunction(name = "aroon_indicator")]
fn bulk_aroon_indicator(
    highs: Vec<f64>,
    lows: Vec<f64>,
    period: usize,
) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(ti::bulk::aroon_indicator(&highs, &lows, period))
}

// Parabolic Time Price System

/// Calculates the long Parabolic Time Price System
///
/// Args:
///     previous_sar: Previous SAR value (if none use period low)
///     extreme_point: Highest high for the period
///     af: Acceleration factor (default 0.02)
///     low: Lowest low for t or t-1
///
/// Returns:
///     SAR value
#[pyfunction(name = "long_parabolic_time_price_system")]
fn single_long_parabolic_time_price_system(
    previous_sar: f64,
    extreme_point: f64,
    af: f64,
    low: f64,
) -> PyResult<f64> {
    Ok(ti::single::long_parabolic_time_price_system(
        previous_sar,
        extreme_point,
        af,
        low,
    ))
}

/// Calculates the short Parabolic Time Price System
///
/// Args:
///     previous_sar: Previous SAR value (if none use period high)
///     extreme_point: Lowest low for the period
///     af: Acceleration factor (default 0.02)
///     high: Highest high for t or t-1
///
/// Returns:
///     SAR value
#[pyfunction(name = "short_parabolic_time_price_system")]
fn single_short_parabolic_time_price_system(
    previous_sar: f64,
    extreme_point: f64,
    af: f64,
    high: f64,
) -> PyResult<f64> {
    Ok(ti::single::short_parabolic_time_price_system(
        previous_sar,
        extreme_point,
        af,
        high,
    ))
}

/// Calculates the Parabolic Time Price System (SAR) series (long/short mode)
///
/// Args:
///     highs: List of highs
///     lows: List of lows
///     af_start: Initial acceleration factor
///     af_step: Acceleration factor increment (default 0.02)
///     af_max: Maximum acceleration factor (default 0.2)
///     position: "long" or "short"
///     previous_sar: Previous SaR (0.0 if none)
///
/// Returns:
///     List of SAR values
#[pyfunction(name = "parabolic_time_price_system")]
fn bulk_parabolic_time_price_system(
    highs: Vec<f64>,
    lows: Vec<f64>,
    af_start: f64,
    af_step: f64,
    af_max: f64,
    position: &str,
    previous_sar: f64,
) -> PyResult<Vec<f64>> {
    Ok(ti::bulk::parabolic_time_price_system(
        &highs,
        &lows,
        af_start,
        af_step,
        af_max,
        crate::PyPosition::from_string(position)?.into(),
        previous_sar,
    ))
}

// Directional Movement System

/// Calculates the Directional Movement System
///
/// Args:
///     highs: List of highs
///     lows: List of lows
///     close: List of close prices
///     period: Period for calculation
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     List of Directional Movement System tuples (+DI, -DI, ADX, ADXR)
#[pyfunction(name = "directional_movement_system")]
fn bulk_directional_movement_system(
    highs: Vec<f64>,
    lows: Vec<f64>,
    close: Vec<f64>,
    period: usize,
    constant_model_type: &str,
) -> PyResult<Vec<(f64, f64, f64, f64)>> {
    Ok(ti::bulk::directional_movement_system(
        &highs,
        &lows,
        &close,
        period,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}

// Volume Price Trend

/// Calculates the Volume Price Trend (VPT)
///
/// Args:
///     current_price
///     previous_price
///     current_volume
///     previous_vpt: Previous VPT value (use 0.0 if none)
///
/// Returns:
///     VPT value
#[pyfunction(name = "volume_price_trend")]
fn single_volume_price_trend(
    current_price: f64,
    previous_price: f64,
    current_volume: f64,
    previous_vpt: f64,
) -> PyResult<f64> {
    Ok(ti::single::volume_price_trend(
        current_price,
        previous_price,
        current_volume,
        previous_vpt,
    ))
}

/// Calculates the Volume Price Trend (VPT) over a period
///
/// Args:
///     prices: List of prices
///     volumes: List of volumes
///     previous_vpt: Previous VPT value (use 0.0 if none)
///
/// Returns:
///     List of VPT values
#[pyfunction(name = "volume_price_trend")]
fn bulk_volume_price_trend(
    prices: Vec<f64>,
    volumes: Vec<f64>,
    previous_vpt: f64,
) -> PyResult<Vec<f64>> {
    Ok(ti::bulk::volume_price_trend(
        &prices,
        &volumes,
        previous_vpt,
    ))
}

// True Strength Index

/// Calculates the True Strength Index (TSI)
///
/// Args:
///     prices: List of prices
///     first_period: Period for first smoothing
///     first_constant_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     second_constant_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     TSI value
#[pyfunction(name = "true_strength_index")]
fn single_true_strength_index(
    prices: Vec<f64>,
    first_period: usize,
    first_constant_model: &str,
    second_constant_model: &str,
) -> PyResult<f64> {
    Ok(ti::single::true_strength_index(
        &prices,
        crate::PyConstantModelType::from_string(first_constant_model)?.into(),
        first_period,
        crate::PyConstantModelType::from_string(second_constant_model)?.into(),
    ))
}

/// Calculates the True Strength Index (TSI) over a period
///
/// Args:
///     prices: List of prices
///     first_constant_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     first_period: Period for first smoothing
///     second_constant_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     second_period: Period for second smoothing
///
/// Returns:
///     List of TSI values
#[pyfunction(name = "true_strength_index")]
fn bulk_true_strength_index(
    prices: Vec<f64>,
    first_constant_model: &str,
    first_period: usize,
    second_constant_model: &str,
    second_period: usize,
) -> PyResult<Vec<f64>> {
    Ok(ti::bulk::true_strength_index(
        &prices,
        crate::PyConstantModelType::from_string(first_constant_model)?.into(),
        first_period,
        crate::PyConstantModelType::from_string(second_constant_model)?.into(),
        second_period,
    ))
}
