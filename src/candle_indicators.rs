use pyo3::prelude::*;
use rust_ti::candle_indicators as ci;

/// Candle indicators are technical indicators designed for use with candlestick price charts.
///
/// They help identify trends, volatility, and price action patterns commonly used in trading and analysis.
///
/// ## When to Use
///
/// Use these indicators to analyze support/resistance, volatility bands,
/// and price channels on candle charts for both traditional and crypto assets.
///
/// ## Structure
/// - **single**: Functions that return a single value for a slice of prices.
/// - **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
#[pymodule]
pub fn candle_indicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

/// **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_moving_constant_envelopes,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_mcginley_dynamic_envelopes,
        &bulk_module
    )?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_moving_constant_bands, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_mcginley_dynamic_bands, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_ichimoku_cloud, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_donchian_channels, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_keltner_channel, &bulk_module)?)?;
    bulk_module.add_function(wrap_pyfunction!(bulk_supertrend, &bulk_module)?)?;
    parent_module.add_submodule(&bulk_module)?;
    Ok(())
}

/// **single**: Functions that return a single value for a slice of prices.
fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(
        single_moving_constant_envelopes,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(
        single_mcginley_dynamic_envelopes,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(
        single_moving_constant_bands,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(
        single_mcginley_dynamic_bands,
        &single_module
    )?)?;
    single_module.add_function(wrap_pyfunction!(single_ichimoku_cloud, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_donchian_channels, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_keltner_channel, &single_module)?)?;
    single_module.add_function(wrap_pyfunction!(single_supertrend, &single_module)?)?;
    parent_module.add_submodule(&single_module)?;
    Ok(())
}

// Moving Constant Envelopes

/// Calculates the Moving Constant Envelopes
///  
/// Args:
///     prices: List of prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     difference: Percent band width (e.g., 3.0 for +-3%)
///
/// Returns:
///     Moving Constant Envelopes tuple (lower envelope, constant model result, upper envelope)
#[pyfunction(name = "moving_constant_envelopes")]
fn single_moving_constant_envelopes(
    prices: Vec<f64>,
    constant_model_type: &str,
    difference: f64,
) -> PyResult<(f64, f64, f64)> {
    Ok(ci::single::moving_constant_envelopes(
        &prices,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        difference,
    ))
}

/// Calculates the Moving Constant Envelopes
///  
/// Args:
///     prices: List of prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     difference: Percent band width (e.g., 3.0 for +-3%)
///     period: Period over which to calculate the moving constant envelopes
///
/// Returns:
///     List of Moving Constant Envelopes tuple (lower envelope, constant model result, upper envelope)
#[pyfunction(name = "moving_constant_envelopes")]
fn bulk_moving_constant_envelopes(
    prices: Vec<f64>,
    constant_model_type: &str,
    difference: f64,
    period: usize,
) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(ci::bulk::moving_constant_envelopes(
        &prices,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        difference,
        period,
    ))
}

// McGinley dynamic envelopes

/// Calculates the McGinley dynamic envelopes
///  
/// Args:
///     prices: List of prices
///     difference: Percent band width (e.g., 3.0 for +-3%)
///     previous_mcginley_dynamic: Previous McGinley dynamic (0.0 if none)
///
/// Returns:
///     McGinley dynamic envelopes tuple (lower envelope, McGinley dynamic, upper envelope)
#[pyfunction(name = "mcginley_dynamic_envelopes")]
fn single_mcginley_dynamic_envelopes(
    prices: Vec<f64>,
    difference: f64,
    previous_mcginley_dynamic: f64,
) -> PyResult<(f64, f64, f64)> {
    Ok(ci::single::mcginley_dynamic_envelopes(
        &prices,
        difference,
        previous_mcginley_dynamic,
    ))
}

/// Calculates the McGinley dynamic envelopes
///  
/// Args:
///     prices: List of prices
///     difference: Percent band width (e.g., 3.0 for +-3%)
///     previous_mcginley_dynamic: Previous McGinley dynamic (0.0 if none)
///     period: Period over which to calculate the McGinley dynamic envelopes
///
/// Returns:
///     List of McGinley dynamic envelopes tuple (lower envelope, McGinley dynamic, upper envelope)
#[pyfunction(name = "mcginley_dynamic_envelopes")]
fn bulk_mcginley_dynamic_envelopes(
    prices: Vec<f64>,
    difference: f64,
    previous_mcginley_dynamic: f64,
    period: usize,
) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(ci::bulk::mcginley_dynamic_envelopes(
        &prices,
        difference,
        previous_mcginley_dynamic,
        period,
    ))
}

// Moving Constant bands

/// Calculates moving constant bands
///
/// Args:
///     prices: List of prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     deviation_model: Choice of "standard_deviation", "mean_absolute_deviation",
///         "median_absolute_deviation", "mode_absolute_deviation", or "ulcer_index"
///     deviation_multiplier: Price deviation multiplier
///
/// Returns:
///     Moving constant bands tuple (lower band, constant model result, upper lower band)
#[pyfunction(name = "moving_constant_bands")]
fn single_moving_constant_bands(
    prices: Vec<f64>,
    constant_model_type: &str,
    deviation_model: &str,
    deviation_multiplier: f64,
) -> PyResult<(f64, f64, f64)> {
    Ok(ci::single::moving_constant_bands(
        &prices,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        crate::PyDeviationModel::from_string(deviation_model)?.into(),
        deviation_multiplier,
    ))
}

/// Calculates moving constant bands
///
/// Args:
///     prices: List of prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     deviation_model: Choice of "standard_deviation", "mean_absolute_deviation",
///         "median_absolute_deviation", "mode_absolute_deviation", or "ulcer_index"
///     deviation_multiplier: Price deviation multiplier
///     period: Period over which to calculate the moving constant bands
///
/// Returns:
///     List of Moving constant bands tuple (lower band, constant model result, upper band)
#[pyfunction(name = "moving_constant_bands")]
fn bulk_moving_constant_bands(
    prices: Vec<f64>,
    constant_model_type: &str,
    deviation_model: &str,
    deviation_multiplier: f64,
    period: usize,
) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(ci::bulk::moving_constant_bands(
        &prices,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        crate::PyDeviationModel::from_string(deviation_model)?.into(),
        deviation_multiplier,
        period,
    ))
}

// McGinley dynamic bands

/// Calculates McGinley dynamic bands
///
/// Args:
///     prices: List of prices
///     deviation_model: Choice of "standard_deviation", "mean_absolute_deviation",
///         "median_absolute_deviation", "mode_absolute_deviation", or "ulcer_index"
///     deviation_multiplier: Price deviation multiplier
///     previous_mcginley_dynamic: Previous McGinley dynamic (0.0 if none)
///
/// Returns:
///     McGinley dynamic bands tuple (lower band, McGinley dynamic, upper band)
#[pyfunction(name = "mcginley_dynamic_bands")]
fn single_mcginley_dynamic_bands(
    prices: Vec<f64>,
    deviation_model: &str,
    deviation_multiplier: f64,
    previous_mcginley_dynamic: f64,
) -> PyResult<(f64, f64, f64)> {
    Ok(ci::single::mcginley_dynamic_bands(
        &prices,
        crate::PyDeviationModel::from_string(deviation_model)?.into(),
        deviation_multiplier,
        previous_mcginley_dynamic,
    ))
}

/// Calculates McGinley dynamic bands
///
/// Args:
///     prices: List of prices
///     deviation_model: Choice of "standard_deviation", "mean_absolute_deviation",
///         "median_absolute_deviation", "mode_absolute_deviation", or "ulcer_index"
///     deviation_multiplier: Price deviation multiplier
///     previous_mcginley_dynamic: Previous McGinley dynamic (0.0 if none)
///     period: Period over which to calculate the McGinley dynamic bands
///
/// Returns:
///     List of McGinley dynamic bands tuple (lower band, McGinley dynamic, upper band)
#[pyfunction(name = "mcginley_dynamic_bands")]
fn bulk_mcginley_dynamic_bands(
    prices: Vec<f64>,
    deviation_model: &str,
    deviation_multiplier: f64,
    previous_mcginley_dynamic: f64,
    period: usize,
) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(ci::bulk::mcginley_dynamic_bands(
        &prices,
        crate::PyDeviationModel::from_string(deviation_model)?.into(),
        deviation_multiplier,
        previous_mcginley_dynamic,
        period,
    ))
}

// Ichimoku Cloud

/// Calculates the Ichimoku Cloud
///
/// Args:
///     highs: List of price highs
///     lows: List of price lows
///     close: List of closing prices
///     conversion_period: Period used to calculate the conversion line
///     base_period: Period used to calculate the base line
///     span_b_period: Period used to calculate the Span B line
///
/// Returns:
///     Ichimoku cloud points tuple (leading span a, leading span b, base line, conversion_line, and most
///     revelant closing price)
#[pyfunction(name = "ichimoku_cloud")]
fn single_ichimoku_cloud(
    highs: Vec<f64>,
    lows: Vec<f64>,
    close: Vec<f64>,
    conversion_period: usize,
    base_period: usize,
    span_b_period: usize,
) -> PyResult<(f64, f64, f64, f64, f64)> {
    Ok(ci::single::ichimoku_cloud(
        &highs,
        &lows,
        &close,
        conversion_period,
        base_period,
        span_b_period,
    ))
}

/// Calculates the Ichimoku Cloud
///
/// Args:
///     highs: List of price highs
///     lows: List of price lows
///     close: List of closing prices
///     conversion_period: Period used to calculate the conversion line
///     base_period: Period used to calculate the base line
///     span_b_period: Period used to calculate the Span B line
///
/// Returns:
///     A list of Ichimoku cloud points tuple (leading span a, leading span b, base line, conversion_line, and most
///     revelant closing price)
#[pyfunction(name = "ichimoku_cloud")]
fn bulk_ichimoku_cloud(
    highs: Vec<f64>,
    lows: Vec<f64>,
    close: Vec<f64>,
    conversion_period: usize,
    base_period: usize,
    span_b_period: usize,
) -> PyResult<Vec<(f64, f64, f64, f64, f64)>> {
    Ok(ci::bulk::ichimoku_cloud(
        &highs,
        &lows,
        &close,
        conversion_period,
        base_period,
        span_b_period,
    ))
}

// Donchian Channels

/// Calculates the Donchian Channels over a given period.
///
/// Args:
///     high: List of highs
///     low: List of lows
///
/// Returns:
///     Donchian channel tuple (lower, average, upper)
#[pyfunction(name = "donchian_channels")]
fn single_donchian_channels(high: Vec<f64>, low: Vec<f64>) -> PyResult<(f64, f64, f64)> {
    Ok(ci::single::donchian_channels(&high, &low))
}

/// Calculates the Donchian Channels over a given period.
///
/// Args:
///     high: List of highs
///     low: List of lows
///     period: Period over which to calculate the Donchian channels
///
/// Returns:
///     List of Donchian channel tuples (lower, average, upper)
#[pyfunction(name = "donchian_channels")]
fn bulk_donchian_channels(
    high: Vec<f64>,
    low: Vec<f64>,
    period: usize,
) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(ci::bulk::donchian_channels(&high, &low, period))
}

// Keltner Channels

/// Calculates the Keltner Channel over a given period
///
/// Args:
///     high: List of highs
///     low: List of lows
///     close: List of previous closing prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///         for the function
///     atr_constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///         for the ATR
///     multiplier: Multiplier for the ATR
///
/// Returns:
///     Keltner channel tuple
#[pyfunction(name = "keltner_channel")]
fn single_keltner_channel(
    high: Vec<f64>,
    low: Vec<f64>,
    close: Vec<f64>,
    constant_model_type: &str,
    atr_constant_model_type: &str,
    multiplier: f64,
) -> PyResult<(f64, f64, f64)> {
    Ok(ci::single::keltner_channel(
        &high,
        &low,
        &close,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        crate::PyConstantModelType::from_string(atr_constant_model_type)?.into(),
        multiplier,
    ))
}

/// Calculates the Keltner Channel over a given period
///
/// Args:
///     high: List of highs
///     low: List of lows
///     close: List of previous closing prices
///     constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///         for the function
///     atr_constant_model_type: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///         for the ATR
///     multiplier: Multiplier for the ATR
///     period: Period over which to calculate the Keltner Channel
///
/// Returns:
///     List of Keltner channel tuples
#[pyfunction(name = "keltner_channel")]
fn bulk_keltner_channel(
    high: Vec<f64>,
    low: Vec<f64>,
    close: Vec<f64>,
    constant_model_type: &str,
    atr_constant_model_type: &str,
    multiplier: f64,
    period: usize,
) -> PyResult<Vec<(f64, f64, f64)>> {
    Ok(ci::bulk::keltner_channel(
        &high,
        &low,
        &close,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        crate::PyConstantModelType::from_string(atr_constant_model_type)?.into(),
        multiplier,
        period,
    ))
}

/// Calculates the Super Trend indicator
///
/// Args
///     high: List of highs
///     low: List of lows
///     close: List of previous closing prices
///     constant_type_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     multiplier: Multiplier for the ATR
///
/// Returns:
///     Super Trend indicator
#[pyfunction(name = "supertrend")]
fn single_supertrend(
    high: Vec<f64>,
    low: Vec<f64>,
    close: Vec<f64>,
    constant_model_type: &str,
    multiplier: f64,
) -> PyResult<f64> {
    Ok(ci::single::supertrend(
        &high,
        &low,
        &close,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        multiplier,
    ))
}

/// Calculates the Super Trend indicator
///
/// Args
///     high: List of highs
///     low: List of lows
///     close: List of previous closing prices
///     constant_type_model: Choice of "simple_moving_average", "smoothed_moving_average",
///         "exponential_moving_average", "simple_moving_median", or "simple_moving_mode"
///     multiplier: Multiplier for the ATR
///     period: Period over which to calculate the supertrend
///
/// Returns:
///     List of Super Trend indicators
#[pyfunction(name = "supertrend")]
fn bulk_supertrend(
    high: Vec<f64>,
    low: Vec<f64>,
    close: Vec<f64>,
    constant_model_type: &str,
    multiplier: f64,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(ci::bulk::supertrend(
        &high,
        &low,
        &close,
        crate::PyConstantModelType::from_string(constant_model_type)?.into(),
        multiplier,
        period,
    ))
}
