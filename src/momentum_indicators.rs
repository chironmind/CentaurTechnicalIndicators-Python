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
    bulk_module.add_function(wrap_pyfunction!(
        bulk_mcginley_dynamic_commodity_channel_index,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_macd_line, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_signal_line, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_mcginley_dynamic_macd_line,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_chaikin_oscillator, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_percentage_price_oscillator,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_chande_momentum_oscillator,
        &bulk_module
    )?)?;
    parent_module.add_submodule(&bulk_module)?;
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
    single_module.add_function(wrap_pyfunction!(
        single_mcginley_dynamic_commodity_channel_index,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(single_macd_line, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_signal_line, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(
        single_mcginley_dynamic_macd_line,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(single_chaikin_oscillator, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(
        single_percentage_price_oscillator,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(
        single_chande_momentum_oscillator,
        &single_module
    )?)?;
    parent_module.add_submodule(&single_module)?;
    Ok(())
}

// Relative Strength Index

/// Calculates the Relative strength index (RSI)
///
/// Args:
///     prices: List of prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Relative Strength Index
#[pyfunction(name = "relative_strength_index")]
fn single_relative_strength_index(prices: Vec<f64>, constant_model_type: &str) -> PyResult<f64> {
    Ok(mi::single::relative_strength_index(
        &prices,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}

/// Calculates the Relative strength index (RSI)
///
/// Args:
///     prices: List of prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     period: Period over which to calculate the RSI
///
/// Returns:
///     List of Relative Strength Index
#[pyfunction(name = "relative_strength_index")]
fn bulk_relative_strength_index(
    prices: Vec<f64>,
    constant_model_type: &str,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::relative_strength_index(
        &prices,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
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
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Slow stochastic
#[pyfunction(name = "slow_stochastic")]
fn single_slow_stochastic(stochastics: Vec<f64>, constant_model_type: &str) -> PyResult<f64> {
    Ok(mi::single::slow_stochastic(
        &stochastics,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}

/// Calculates the slow stochastic
///
/// Args:
///     stochastics: List of stochastics
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     period: Period over which to calculate the slow stochastic
///
/// Returns:
///     List of Slow stochastics
#[pyfunction(name = "slow_stochastic")]
fn bulk_slow_stochastic(
    stochastics: Vec<f64>,
    constant_model_type: &str,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::slow_stochastic(
        &stochastics,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        period,
    ))
}

// Slowest Stochastic

/// Calculates the slowest Stochastic
///
/// Args:
///     slow_stochastics: List of slow stochastics
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Slowest stochastic
#[pyfunction(name = "slowest_stochastic")]
fn single_slowest_stochastic(
    slow_stochastics: Vec<f64>,
    constant_model_type: &str,
) -> PyResult<f64> {
    Ok(mi::single::slowest_stochastic(
        &slow_stochastics,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}

/// Calculates the slowest Stochastic
///
/// Args:
///     slow_stochastics: List of slow stochastics
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     period: Period over which to calculate the slowest stochastic oscillator
///
/// Returns:
///     List of lowest stochastic
#[pyfunction(name = "slowest_stochastic")]
fn bulk_slowest_stochastic(
    slow_stochastics: Vec<f64>,
    constant_model_type: &str,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::slowest_stochastic(
        &slow_stochastics,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
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
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     deviation_model: Choice of "standard_deviation", "mean_absolute_deviation",
///         "median_absolute_deviation", "mode_absolute_deviation", "ulcer_index"
///     constant_multiplier: Scale factor (normally 0.015)
///
/// Returns:
///     Commodity Channel Index
#[pyfunction(name = "commodity_channel_index")]
fn single_commodity_channel_index(
    prices: Vec<f64>,
    constant_model_type: &str,
    deviation_model: &str,
    constant_multiplier: f64,
) -> PyResult<f64> {
    Ok(mi::single::commodity_channel_index(
        &prices,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        crate::PyDeviationModel::from_string(deviation_model)?.into(),
        constant_multiplier,
    ))
}

/// Calculates the Commodity Channel Index (CCI)
///
/// Args:
///     prices: List of prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     deviation_model: Choice of "standard_deviation", "mean_absolute_deviation",
///         "median_absolute_deviation", "mode_absolute_deviation", "ulcer_index"
///     constant_multiplier: Scale factor (normally 0.015)
///     period: Period over which to calculate the CCI
///
/// Returns:
///     Commodity Channel Index
#[pyfunction(name = "commodity_channel_index")]
fn bulk_commodity_channel_index(
    prices: Vec<f64>,
    constant_model_type: &str,
    deviation_model: &str,
    constant_multiplier: f64,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::commodity_channel_index(
        &prices,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        crate::PyDeviationModel::from_string(deviation_model)?.into(),
        constant_multiplier,
        period,
    ))
}

// McGinley Dynamic Commodity Channel Index

/// Calculates the McGinley Dynamic Commodity Channel Index (CCI)
///
/// Args:
///     prices: List of prices
///     previous_mcginley_dynamic: Previous McGinley dynamic (0.0 if none)
///     deviation_model: Choice of "standard_deviation", "mean_absolute_deviation",
///         "median_absolute_deviation", "mode_absolute_deviation", "ulcer_index"
///     constant_multiplier: Scale factor (normally 0.015)
///
/// Returns:
///     A tuple with the Commodity Channel Index and McGinley Dynamic
#[pyfunction(name = "mcginley_dynamic_commodity_channel_index")]
fn single_mcginley_dynamic_commodity_channel_index(
    prices: Vec<f64>,
    previous_mcginley_dynamic: f64,
    deviation_model: &str,
    constant_multiplier: f64,
) -> PyResult<(f64, f64)> {
    Ok(mi::single::mcginley_dynamic_commodity_channel_index(
        &prices,
        previous_mcginley_dynamic,
        crate::PyDeviationModel::from_string(deviation_model)?.into(),
        constant_multiplier,
    ))
}

/// Calculates the McGinley Dynamic Commodity Channel Index (CCI)
///
/// Args:
///     prices: List of prices
///     previous_mcginley_dynamic: Previous McGinley dynamic (0.0 if none)
///     deviation_model: Choice of "standard_deviation", "mean_absolute_deviation",
///         "median_absolute_deviation", "mode_absolute_deviation", "ulcer_index"
///     constant_multiplier: Scale factor (normally 0.015)
///     period: Period over which to calculate the CCI
///
/// Returns:
///     A tuple with the Commodity Channel Index and McGinley Dynamic
#[pyfunction(name = "mcginley_dynamic_commodity_channel_index")]
fn bulk_mcginley_dynamic_commodity_channel_index(
    prices: Vec<f64>,
    previous_mcginley_dynamic: f64,
    deviation_model: &str,
    constant_multiplier: f64,
    period: usize,
) -> PyResult<Vec<(f64, f64)>> {
    Ok(mi::bulk::mcginley_dynamic_commodity_channel_index(
        &prices,
        previous_mcginley_dynamic,
        crate::PyDeviationModel::from_string(deviation_model)?.into(),
        constant_multiplier,
        period,
    ))
}

// MACD

/// Calculates the Moving Average Convergence Divergence (MACD) line
///
/// Args:
///     prices: List of prices
///     short_period: Length of the short period
///     short_period_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     long_period_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Moving Average Convergence Divergence
#[pyfunction(name = "macd_line")]
fn single_macd_line(
    prices: Vec<f64>,
    short_period: usize,
    short_period_model: &str,
    long_period_model: &str,
) -> PyResult<f64> {
    Ok(mi::single::macd_line(
        &prices,
        short_period,
        crate::PyConstantModelType::from_string(short_period_model)?.into(),
        crate::PyConstantModelType::from_string(long_period_model)?.into(),
    ))
}

/// Calculates the Moving Average Convergence Divergence (MACD) line
///
/// Args:
///     prices: List of prices
///     short_period: Length of the short period
///     short_period_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     long_period: Length of the long period
///     long_period_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Moving Average Convergence Divergence
#[pyfunction(name = "macd_line")]
fn bulk_macd_line(
    prices: Vec<f64>,
    short_period: usize,
    short_period_model: &str,
    long_period: usize,
    long_period_model: &str,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::macd_line(
        &prices,
        short_period,
        crate::PyConstantModelType::from_string(short_period_model)?.into(),
        long_period,
        crate::PyConstantModelType::from_string(long_period_model)?.into(),
    ))
}

// MACD Signal line

/// Calculates the MACD signal line divergence.
///
/// Args:
///     macds: list of MACDs
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Signal line point
#[pyfunction(name = "signal_line")]
fn single_signal_line(macds: Vec<f64>, constant_model_type: &str) -> PyResult<f64> {
    Ok(mi::single::signal_line(
        &macds,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}

/// Calculates the MACD signal line divergence.
///
/// Args:
///     macds: list of MACDs
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     period: Period over which to calculate the signal line
///
/// Returns:
///     List Signal line points
#[pyfunction(name = "signal_line")]
fn bulk_signal_line(
    macds: Vec<f64>,
    constant_model_type: &str,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::signal_line(
        &macds,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        period,
    ))
}

// McGinley Dynamic MACD

/// Calculates the McGinley dynamic MACD line
///
/// Args:
///     prices: List of prices
///     short_period: Length of the short period
///     previous_short_mcginley - Previous short model McGinley dynamic (if none use 0.0)
///     previous_long_mcginley - Previous long model McGinley dynamic (if none use 0.0)
///
/// Returns:
///     Tuple with Moving Average Convergence Divergence, short McGinley dynamic, long McGinley
///     dynamic
#[pyfunction(name = "mcginley_dynamic_macd_line")]
fn single_mcginley_dynamic_macd_line(
    prices: Vec<f64>,
    short_period: usize,
    previous_short_mcginley: f64,
    previous_long_mcginley: f64,
) -> PyResult<(f64, f64, f64)> {
    Ok(mi::single::mcginley_dynamic_macd_line(
        &prices,
        short_period,
        previous_short_mcginley,
        previous_long_mcginley,
    ))
}

/// Calculates the McGinley dynamic MACD line
///
/// Args:
///     prices: List of prices
///     short_period: Length of the short period
///     previous_short_mcginley: Previous short model McGinley dynamic (if none use 0.0)
///     long_period: Length of the long period
///     previous_long_mcginley: Previous long model McGinley dynamic (if none use 0.0)
///
/// Returns:
///     Tuple with Moving Average Convergence Divergence, short McGinley dynamic, long McGinley
///     dynamic
#[pyfunction(name = "mcginley_dynamic_macd_line")]
fn bulk_mcginley_dynamic_macd_line(
    prices: Vec<f64>,
    short_period: usize,
    previous_short_mcginley: f64,
    long_period: usize,
    previous_long_mcginley: f64,
) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(mi::bulk::mcginley_dynamic_macd_line(
        &prices,
        short_period,
        previous_short_mcginley,
        long_period,
        previous_long_mcginley,
    ))
}

// Chaikin Oscillator

/// Calculates the  Chaikin Oscillator (CO)
///
/// # Args:
///     highs: List of highs
///     lows: List of lows
///     close: List of closing prices
///     volume: List of volumes
///     short_period: Short period over which to calculate the AD
///     previous_accumulation_distribution: Previous AD value (if none use 0.0)
///     short_period_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     long_period_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Tuple of Chaikin Oscillator and Accumulation Distribution
#[pyfunction(name = "chaikin_oscillator")]
fn single_chaikin_oscillator(
    highs: Vec<f64>,
    lows: Vec<f64>,
    close: Vec<f64>,
    volume: Vec<f64>,
    short_period: usize,
    previous_accumulation_distribution: f64,
    short_period_model: &str,
    long_period_model: &str,
) -> PyResult<(f64, f64)> {
    Ok(mi::single::chaikin_oscillator(
        &highs,
        &lows,
        &close,
        &volume,
        short_period,
        previous_accumulation_distribution,
        crate::PyConstantModelType::from_string(short_period_model)?.into(),
        crate::PyConstantModelType::from_string(long_period_model)?.into(),
    ))
}

/// Calculates the  Chaikin Oscillator (CO)
///
/// # Args:
///     highs: List of highs
///     lows: List of lows
///     close: List of closing prices
///     volume: List of volumes
///     short_period: Short period over which to calculate the AD
///     long_period: Long period over which to calculate the AD
///     previous_accumulation_distribution: Previous AD value (if none use 0.0)
///     short_period_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     long_period_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     Tuple of Chaikin Oscillator and Accumulation Distribution
#[pyfunction(name = "chaikin_oscillator")]
fn bulk_chaikin_oscillator(
    highs: Vec<f64>,
    lows: Vec<f64>,
    close: Vec<f64>,
    volume: Vec<f64>,
    short_period: usize,
    long_period: usize,
    previous_accumulation_distribution: f64,
    short_period_model: &str,
    long_period_model: &str,
) -> PyResult<Vec<(f64, f64)>> {
    Ok(mi::bulk::chaikin_oscillator(
        &highs,
        &lows,
        &close,
        &volume,
        short_period,
        long_period,
        previous_accumulation_distribution,
        crate::PyConstantModelType::from_string(short_period_model)?.into(),
        crate::PyConstantModelType::from_string(long_period_model)?.into(),
    ))
}

// Percentage Price Oscillator

/// Calculates the Percentage Price Oscillator (PPO)
///
/// Args:
///     prices: List of prices
///     short_period: Length of short period.
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     The Percentage Price Oscillator
#[pyfunction(name = "percentage_price_oscillator")]
fn single_percentage_price_oscillator(
    prices: Vec<f64>,
    short_period: usize,
    constant_model_type: &str,
) -> PyResult<f64> {
    Ok(mi::single::percentage_price_oscillator(
        &prices,
        short_period,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}

/// Calculates the Percentage Price Oscillator (PPO)
///
/// Args:
///     prices: List of prices
///     short_period: Length of short period.
///     long_period: Length of long period
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///
/// Returns:
///     List of Percentage Price Oscillator
#[pyfunction(name = "percentage_price_oscillator")]
fn bulk_percentage_price_oscillator(
    prices: Vec<f64>,
    short_period: usize,
    long_period: usize,
    constant_model_type: &str,
) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::percentage_price_oscillator(
        &prices,
        short_period,
        long_period,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
    ))
}

// Chande Momentum Oscillator

/// Calculates the Chande Momentum Oscillator (CMO)
///
/// Args:
///     prices: List of prices
///     
/// Returns:
///     The Chande Momentum Oscillator
#[pyfunction(name = "chande_momentum_oscillator")]
fn single_chande_momentum_oscillator(prices: Vec<f64>) -> PyResult<f64> {
    Ok(mi::single::chande_momentum_oscillator(&prices))
}

/// Calculates the Chande Momentum Oscillator (CMO)
///
/// Args:
///     prices: List of prices
///     period: Period over which to calculate the CMO
///     
/// Returns:
///     List Chande Momentum Oscillator
#[pyfunction(name = "chande_momentum_oscillator")]
fn bulk_chande_momentum_oscillator(prices: Vec<f64>, period: usize) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::chande_momentum_oscillator(&prices, period))
}
