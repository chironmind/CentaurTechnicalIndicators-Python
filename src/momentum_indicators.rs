use pyo3::prelude::*;
use rust_ti::momentum_indicators as mi;

/// The `momentum_indicators` module provides functions to measure the speed, strength, and direction of price movements in time series data.
///
/// These indicators are commonly used to identify overbought/oversold conditions, trend continuation, or potential reversals.
///
/// ## When to Use
/// Use momentum indicators to:
/// - Gauge the strength and velocity of price trends
/// - Identify bullish or bearish momentum
/// - Spot early signals for possible price reversals or continuations
///
/// ## Structure
/// - **single**: Functions that return a single value for a slice of prices.
/// - **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
#[pymodule]
pub fn momentum_indicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

/// **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_relative_strength_index,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_stochastic_oscillator, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_slow_stochastic, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_slowest_stochastic, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_williams_percent_r, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_money_flow_index, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_rate_of_change, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_on_balance_volume, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_commodity_channel_index,
        &bulk_module
    )?)?;
    parent_module.add_submodule(&bulk_module);
    Ok(())
}

/// **single**: Functions that return a single value for a slice of prices.
fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(
        single_relative_strength_index,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(
        single_stochastic_oscillator,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(single_slow_stochastic, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_slowest_stochastic, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_williams_percent_r, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_money_flow_index, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_rate_of_change, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_on_balance_volume, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(
        single_commodity_channel_index,
        &single_module
    )?)?;
    parent_module.add_submodule(&single_module);
    Ok(())
}

// Relative Strength Index

/// Calculates the Relative strength index (RSI)
///
/// Args:
///     prices: List of prices
///     constant_model_type: Variant of `ConstantModelType`
///
/// Returns:
///     Relative Strength Index
#[pyfunction(name = "relative_strength_index")]
fn single_relative_strength_index(
    prices: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
) -> PyResult<f64> {
    Ok(mi::single::relative_strength_index(
        &prices,
        constant_model_type.into(),
    ))
}

/// Calculates the Relative strength index (RSI)
///
/// Args:
///     prices: List of prices
///     constant_model_type: Variant of `ConstantModelType`
///     period: Period over which to calculate the RSI
///
/// Returns:
///     List of Relative Strength Index
#[pyfunction(name = "relative_strength_index")]
fn bulk_relative_strength_index(
    prices: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::relative_strength_index(
        &prices,
        constant_model_type.into(),
        period,
    ))
}

// Stochastic Oscillator

/// Calculates the stochastic oscillator
///
/// Args:
///     prices: List of prices
///
/// Returns:
///     Stochastic Oscillator
#[pyfunction(name = "stochastic_oscillator")]
fn single_stochastic_oscillator(prices: Vec<f64>) -> PyResult<f64> {
    Ok(mi::single::stochastic_oscillator(&prices))
}

/// Calculates the stochastic oscillator
///
/// Args:
///     prices: List of prices
///     period: Period over which to calculate the stochastic oscillator
///
/// Returns:
///     List of Stochastic Oscillators
#[pyfunction(name = "stochastic_oscillator")]
fn bulk_stochastic_oscillator(prices: Vec<f64>, period: usize) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::stochastic_oscillator(&prices, period))
}

// Slow Stochastic

/// Calculates the slow stochastic
///
/// Args:
///     stochastics: List of stochastics
///     constant_model_type: Variant of `ConstantModelType`
///
/// Returns:
///     Slow stochastic
#[pyfunction(name = "slow_stochastic")]
fn single_slow_stochastic(
    stochastics: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
) -> PyResult<f64> {
    Ok(mi::single::slow_stochastic(
        &stochastics,
        constant_model_type.into(),
    ))
}

/// Calculates the slow stochastic
///
/// Args:
///     stochastics: List of stochastics
///     constant_model_type: Variant of `ConstantModelType`
///     period: Period over which to calculate the slow stochastic
///
/// Returns:
///     List of Slow stochastics
#[pyfunction(name = "slow_stochastic")]
fn bulk_slow_stochastic(
    stochastics: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::slow_stochastic(
        &stochastics,
        constant_model_type.into(),
        period,
    ))
}

// Slowest Stochastic

/// Calculates the slowest Stochastic
///
/// Args:
///     slow_stochastics: List of slow stochastics
///     constant_model_type: Variant of `ConstantModelType`
///
/// Returns:
///     Slowest stochastic
#[pyfunction(name = "slowest_stochastic")]
fn single_slowest_stochastic(
    slow_stochastics: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
) -> PyResult<f64> {
    Ok(mi::single::slowest_stochastic(
        &slow_stochastics,
        constant_model_type.into(),
    ))
}

/// Calculates the slowest Stochastic
///
/// Args:
///     slow_stochastics: List of slow stochastics
///     constant_model_type: Variant of `ConstantModelType`
///     period: Period over which to calculate the slowest stochastic oscillator
///
/// Returns:
///     List of lowest stochastic
#[pyfunction(name = "slowest_stochastic")]
fn bulk_slowest_stochastic(
    slow_stochastics: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::slowest_stochastic(
        &slow_stochastics,
        constant_model_type.into(),
        period,
    ))
}

// Wiiliams %R

/// Calculates the Williams %R
///
/// Args:
///     high: List of highs
///     low: List of lows
///     close: Closing price for the observed period
///
/// Returns:
///     Williams %R
#[pyfunction(name = "williams_percent_r")]
fn single_williams_percent_r(high: Vec<f64>, low: Vec<f64>, close: f64) -> PyResult<f64> {
    Ok(mi::single::williams_percent_r(&high, &low, close))
}

/// Calculates the Williams %R
///
/// Args:
///     high: List of highs
///     low: List of lows
///     close: List of closing prices
///     period: Period over which to calculate the Williams %R
///
/// Returns:
///     List of Williams %R
#[pyfunction(name = "williams_percent_r")]
fn bulk_williams_percent_r(
    high: Vec<f64>,
    low: Vec<f64>,
    close: Vec<f64>,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::williams_percent_r(&high, &low, &close, period))
}

// Money Flow Index

/// Calculates the Money Flow Index (MFI)
///
/// Args:
///     prices: List of prices
///     volume: List of volumes
///
/// Returns:
///     Money Flow Index
#[pyfunction(name = "money_flow_index")]
fn single_money_flow_index(prices: Vec<f64>, volume: Vec<f64>) -> PyResult<f64> {
    Ok(mi::single::money_flow_index(&prices, &volume))
}

/// Calculates the Money Flow Index (MFI)
///
/// Args:
///     prices: List of prices
///     volume: List of volumes
///     period: Period over which to calculate the MFI
///
/// Returns:
///     Money Flow Index
#[pyfunction(name = "money_flow_index")]
fn bulk_money_flow_index(prices: Vec<f64>, volume: Vec<f64>, period: usize) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::money_flow_index(&prices, &volume, period))
}

// Rate of Change

/// Calculates the Rate of Change (RoC)
///
/// Args:
///     current_price
///     previous_price
///
/// Returns:
///     Rate of Change
#[pyfunction(name = "rate_of_change")]
fn single_rate_of_change(current_price: f64, previous_price: f64) -> PyResult<f64> {
    Ok(mi::single::rate_of_change(current_price, previous_price))
}

/// Calculates the Rate of Change (RoC)
///
/// Args:
///     prices: list of prices
///
/// Returns:
///     List of Rate of Change
#[pyfunction(name = "rate_of_change")]
fn bulk_rate_of_change(prices: Vec<f64>) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::rate_of_change(&prices))
}

// On Balance Volume

/// Calculates the On Balance Volume (OBV)
///
/// Args:
///     current_price
///     previous_price
///     current_volume
///     previous_on_balance_volume: use 0.0 if none
///
/// Returns:
///     On Balance Volume
#[pyfunction(name = "on_balance_volume")]
fn single_on_balance_volume(
    current_price: f64,
    previous_price: f64,
    current_volume: f64,
    previous_on_balance_volume: f64,
) -> PyResult<f64> {
    Ok(mi::single::on_balance_volume(
        current_price,
        previous_price,
        current_volume,
        previous_on_balance_volume,
    ))
}

/// Calculates the On Balance Volume (OBV)
///
/// Args:
///     prices: List of prices
///     volume: List of volumes
///     previous_on_balance_volume: use 0.0 if none
///
/// Returns:
///     List of On Balance Volume
#[pyfunction(name = "on_balance_volume")]
fn bulk_on_balance_volume(
    prices: Vec<f64>,
    volume: Vec<f64>,
    previous_on_balance_volume: f64,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::on_balance_volume(
        &prices,
        &volume,
        previous_on_balance_volume,
    ))
}

// Commodity Channel Index

/// Calculates the Commodity Channel Index (CCI)
///
/// Args:
///     prices: List of prices
///     constant_model_type: Variant of `ConstantModelType`
///     deviation_model: Variant of `DeviationModel`
///     constant_multiplier: Scale factor (normally 0.015)
///
/// Returns:
///     Commodity Channel Index
#[pyfunction(name = "commodity_channel_index")]
fn single_commodity_channel_index(
    prices: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
    deviation_model: crate::PyDeviationModel,
    constant_multiplier: f64,
) -> PyResult<f64> {
    Ok(mi::single::commodity_channel_index(
        &prices,
        constant_model_type.into(),
        deviation_model.into(),
        constant_multiplier,
    ))
}

/// Calculates the Commodity Channel Index (CCI)
///
/// Args:
///     prices: List of prices
///     constant_model_type: Variant of `ConstantModelType`
///     deviation_model: Variant of `DeviationModel`
///     constant_multiplier: Scale factor (normally 0.015)
///     period: Period over which to calculate the CCI
///
/// Returns:
///     Commodity Channel Index
#[pyfunction(name = "commodity_channel_index")]
fn bulk_commodity_channel_index(
    prices: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
    deviation_model: crate::PyDeviationModel,
    constant_multiplier: f64,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::commodity_channel_index(
        &prices,
        constant_model_type.into(),
        deviation_model.into(),
        constant_multiplier,
        period,
    ))
}
