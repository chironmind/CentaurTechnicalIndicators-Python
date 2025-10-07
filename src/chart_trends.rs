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
///     config: Either a preset string ("default", "conservative", "moderate", "aggressive")
///             or custom parameters (all 9 parameters must be provided together)
///     max_outliers: (Optional) Allowed consecutive trend-breaks before splitting
///     soft_adj_r_squared_minimum: (Optional) Soft minimum value for adjusted r squared
///     hard_adj_r_squared_minimum: (Optional) Hard minimum value for adjusted r squared
///     soft_rmse_multiplier: (Optional) Soft RMSE multiplier
///     hard_rmse_multiplier: (Optional) Hard RMSE multiplier
///     soft_durbin_watson_min: (Optional) Soft minimum Durbin-Watson statistic
///     soft_durbin_watson_max: (Optional) Soft maximum Durbin-Watson statistic
///     hard_durbin_watson_min: (Optional) Hard minimum Durbin-Watson statistic
///     hard_durbin_watson_max: (Optional) Hard maximum Durbin-Watson statistic
///
/// Returns:
///     List of tuples containing (start_index, end_index, slope, intercept) for each trend segment
#[pyfunction]
#[pyo3(signature = (prices, config=None, max_outliers=None, soft_adj_r_squared_minimum=None, hard_adj_r_squared_minimum=None, soft_rmse_multiplier=None, hard_rmse_multiplier=None, soft_durbin_watson_min=None, soft_durbin_watson_max=None, hard_durbin_watson_min=None, hard_durbin_watson_max=None))]
fn break_down_trends(
    prices: Vec<f64>,
    config: Option<&str>,
    max_outliers: Option<usize>,
    soft_adj_r_squared_minimum: Option<f64>,
    hard_adj_r_squared_minimum: Option<f64>,
    soft_rmse_multiplier: Option<f64>,
    hard_rmse_multiplier: Option<f64>,
    soft_durbin_watson_min: Option<f64>,
    soft_durbin_watson_max: Option<f64>,
    hard_durbin_watson_min: Option<f64>,
    hard_durbin_watson_max: Option<f64>,
) -> PyResult<Vec<(usize, usize, f64, f64)>> {
    let trend_config = if let Some(config_str) = config {
        crate::PyTrendBreakConfig::from_string(config_str)?.into()
    } else if let (
        Some(max_outliers),
        Some(soft_adj_r_squared_minimum),
        Some(hard_adj_r_squared_minimum),
        Some(soft_rmse_multiplier),
        Some(hard_rmse_multiplier),
        Some(soft_durbin_watson_min),
        Some(soft_durbin_watson_max),
        Some(hard_durbin_watson_min),
        Some(hard_durbin_watson_max),
    ) = (
        max_outliers,
        soft_adj_r_squared_minimum,
        hard_adj_r_squared_minimum,
        soft_rmse_multiplier,
        hard_rmse_multiplier,
        soft_durbin_watson_min,
        soft_durbin_watson_max,
        hard_durbin_watson_min,
        hard_durbin_watson_max,
    ) {
        crate::PyTrendBreakConfig::custom(
            max_outliers,
            soft_adj_r_squared_minimum,
            hard_adj_r_squared_minimum,
            soft_rmse_multiplier,
            hard_rmse_multiplier,
            soft_durbin_watson_min,
            soft_durbin_watson_max,
            hard_durbin_watson_min,
            hard_durbin_watson_max,
        )
        .into()
    } else {
        return Err(pyo3::exceptions::PyValueError::new_err(
            "Either provide 'config' as a preset string, or all 9 custom parameters",
        ));
    };

    Ok(ct::break_down_trends(&prices, trend_config))
}
