use rust_ti::momentum_indicators as mi;
use pyo3::prelude::*;

#[pymodule]
pub fn momentum_indicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    register_bulk_module(m)?;
    register_single_module(m)?;
    Ok(())
}

fn register_bulk_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let bulk_module = PyModule::new(parent_module.py(), "bulk")?;
    bulk_module.add_function(wrap_pyfunction!(bulk_relative_strength_index, &bulk_module)?)?;
    parent_module.add_submodule(&bulk_module);
    Ok(())
}

fn register_single_module(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let single_module = PyModule::new(parent_module.py(), "single")?;
    single_module.add_function(wrap_pyfunction!(single_relative_strength_index, &single_module)?)?;
    parent_module.add_submodule(&single_module);
    Ok(())
}

#[pyfunction(name = "relative_strength_index")]
fn single_relative_strength_index(prices: Vec<f64>, model: crate::PyConstantModelType) -> PyResult<f64> {
    Ok(mi::single::relative_strength_index(&prices, model.into()))
}

#[pyfunction(name = "relative_strength_index")]
fn bulk_relative_strength_index(prices: Vec<f64>, model: crate::PyConstantModelType, period: usize) -> PyResult<Vec<f64>> {
    Ok(mi::bulk::relative_strength_index(&prices, model.into(), period))
}

