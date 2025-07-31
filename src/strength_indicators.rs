use pyo3::prelude::*;
use rust_ti::strength_indicators as si;

/// The `strength_indicators` module provides functions to assess the strength and conviction of
/// price movements and trends using volume and price-based calculations.
///
/// ## When to Use
/// Use these indicators to:
/// - Analyze volume-price relationships
/// - Gauge market conviction
/// - Identify trend strength
///
/// ## Structure
/// - **single**: Functions that return a single value for a slice of prices.
/// - **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
#[pymodule]
pub fn strength_indicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

/// **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_accumulation_distribution,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_positive_volume_index, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_negative_volume_index, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_relative_vigor_index, &bulk_module)?)?;
    parent_module.add_submodule(&bulk_module)?;
    Ok(())
}

/// **single**: Functions that return a single value for a slice of prices.
fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(
        single_accumulation_distribution,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(single_volume_index, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(
        single_relative_vigor_index,
        &single_module
    )?)?;
    parent_module.add_submodule(&single_module)?;
    Ok(())
}

// Accumulation Distribution

/// Calculates the accumulation distribution
///
/// Args:
///     high: High price
///     low: Low price
///     close: Close price
///     volume: Volume
///     previous_accumulation_distribution: Previous AD (0.0 if none)
///
/// Returns:
///     Accumulation Distribution value
#[pyfunction(name = "accumulation_distribution")]
fn single_accumulation_distribution(
    high: f64,
    low: f64,
    close: f64,
    volume: f64,
    previous_accumulation_distribution: f64,
) -> PyResult<f64> {
    Ok(si::single::accumulation_distribution(
        high,
        low,
        close,
        volume,
        previous_accumulation_distribution,
    ))
}

/// Calculates the accumulation distribution
///
/// Args:
///     highs: List of highs
///     lows: List of lows
///     close: List of closing prices
///     volume: List of volumes
///     previous_accumulation_distribution: Previous AD (0.0 if none)
///
/// Returns:
///     List of Accumulation Distribution values
#[pyfunction(name = "accumulation_distribution")]
fn bulk_accumulation_distribution(
    highs: Vec<f64>,
    lows: Vec<f64>,
    close: Vec<f64>,
    volume: Vec<f64>,
    previous_accumulation_distribution: f64,
) -> PyResult<Vec<f64>> {
    Ok(si::bulk::accumulation_distribution(
        &highs,
        &lows,
        &close,
        &volume,
        previous_accumulation_distribution,
    ))
}

// Volume Index

/// Calculates a generic volume index used in Positive and Negative Volume Index
///
/// Args:
///     current_close: Current close price
///     previous_close: Previous close price
///     previous_volume_index: Previous PVI/NVI value (0.0 if none)
///
/// Returns:
///     Volume Index value
#[pyfunction(name = "volume_index")]
fn single_volume_index(
    current_close: f64,
    previous_close: f64,
    previous_volume_index: f64,
) -> PyResult<f64> {
    Ok(si::single::volume_index(
        current_close,
        previous_close,
        previous_volume_index,
    ))
}

/// Calculates the Positive Volume Index (PVI)
///
/// Args:
///     close: List of closing prices
///     volume: List of volumes
///     previous_volume_index: Previous PVI value (0.0 if none)
///
/// Returns:
///     List of Positive Volume Index values
#[pyfunction(name = "positive_volume_index")]
fn bulk_positive_volume_index(
    close: Vec<f64>,
    volume: Vec<f64>,
    previous_volume_index: f64,
) -> PyResult<Vec<f64>> {
    Ok(si::bulk::positive_volume_index(
        &close,
        &volume,
        previous_volume_index,
    ))
}

/// Calculates the Negative Volume Index (NVI)
///
/// Args:
///     close: List of closing prices
///     volume: List of volumes
///     previous_volume_index: Previous NVI value (0.0 if none)
///
/// Returns:
///     List of Negative Volume Index values
#[pyfunction(name = "negative_volume_index")]
fn bulk_negative_volume_index(
    close: Vec<f64>,
    volume: Vec<f64>,
    previous_volume_index: f64,
) -> PyResult<Vec<f64>> {
    Ok(si::bulk::negative_volume_index(
        &close,
        &volume,
        previous_volume_index,
    ))
}

// Relative Vigor Index

/// Calculates the Relative Vigor Index (RVI)
///
/// Args:
///     open: List of opening prices
///     high: List of highs
///     low: List of lows
///     close: List of closing prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Relative Vigor Index value
#[pyfunction(name = "relative_vigor_index")]
fn single_relative_vigor_index(
    open: Vec<f64>,
    high: Vec<f64>,
    low: Vec<f64>,
    close: Vec<f64>,
    constant_model_type: &str,
) -> PyResult<f64> {
    Ok(si::single::relative_vigor_index(
        &open,
        &high,
        &low,
        &close,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}

/// Calculates the Relative Vigor Index (RVI)
///
/// Args:
///     open: List of opening prices
///     high: List of highs
///     low: List of lows
///     close: List of closing prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     period: Period over which to calculate the RVI
///
/// Returns:
///     List of Relative Vigor Index values
#[pyfunction(name = "relative_vigor_index")]
fn bulk_relative_vigor_index(
    open: Vec<f64>,
    high: Vec<f64>,
    low: Vec<f64>,
    close: Vec<f64>,
    constant_model_type: &str,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(si::bulk::relative_vigor_index(
        &open,
        &high,
        &low,
        &close,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        period,
    ))
}
