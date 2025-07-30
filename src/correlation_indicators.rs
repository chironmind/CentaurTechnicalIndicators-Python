use pyo3::prelude::*;
use rust_ti::correlation_indicators as ci;

/// The `correlation_indicators` module provides functions to measure the co-movement
/// and statistical relationship between two different price series or assets.
///
/// ## When to Use
/// Use correlation indicators when you want to:
/// - Quantify how closely two assets move together
/// - Assess diversification or hedging effectiveness
/// - Explore relationships between assets
///
/// ## Structure
/// - **single**: Functions that return a single value for a slice of prices.
/// - **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
#[pymodule]
pub fn correlation_indicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

/// **bulk**: Functions that compute values of a slice of prices over a period and return a vector.
fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(
        bulk_correlate_asset_prices,
        &bulk_module
    )?)?;
    parent_module.add_submodule(&bulk_module)?;
    Ok(())
}
/// **single**: Functions that return a single value for a slice of prices.
fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(
        single_correlate_asset_prices,
        &single_module
    )?)?;
    parent_module.add_submodule(&single_module)?;
    Ok(())
}

/// Calculates the correlation between two asset price series.
///
/// Args:
///     prices_asset_a: List of prices for asset A
///     prices_asset_b: List of prices for asset B
///     constant_model_type: Variant of `ConstantModelType`
///     deviation_model: Variant of `DeviationModel`
///
/// Returns:
///     Correlation between the two asset price series.
#[pyfunction(name = "correlate_asset_prices")]
fn single_correlate_asset_prices(
    prices_asset_a: Vec<f64>,
    prices_asset_b: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
    deviation_model: crate::PyDeviationModel,
) -> PyResult<f64> {
    Ok(ci::single::correlate_asset_prices(
        &prices_asset_a,
        &prices_asset_b,
        constant_model_type.into(),
        deviation_model.into(),
    ))
}

/// Calculates the correlation between two asset prices over a period.
///
/// Args:
///     prices_asset_a: List of prices for asset A
///     prices_asset_b: List of prices for asset B
///     constant_model_type: Variant of `ConstantModelType`
///     deviation_model: Variant of `DeviationModel`
///     period: Period over which to calculate the correlation
///
/// Returns:
///     List of correlations for each window of the given period.
#[pyfunction(name = "correlate_asset_prices")]
fn bulk_correlate_asset_prices(
    prices_asset_a: Vec<f64>,
    prices_asset_b: Vec<f64>,
    constant_model_type: crate::PyConstantModelType,
    deviation_model: crate::PyDeviationModel,
    period: usize,
) -> PyResult<Vec<f64>> {
    Ok(ci::bulk::correlate_asset_prices(
        &prices_asset_a,
        &prices_asset_b,
        constant_model_type.into(),
        deviation_model.into(),
        period,
    ))
}
