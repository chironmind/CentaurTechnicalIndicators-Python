use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use rust_ti::{ConstantModelType, DeviationModel};

pub mod momentum_indicators;
pub mod candle_indicators;

#[pyclass(name = "ConstantModelType")]
#[derive(Clone)]
pub enum PyConstantModelType {
    SimpleMovingAverage(),
    SmoothedMovingAverage(),
    ExponentialMovingAverage(),
    PersonalisedMovingAverage(f64, f64),
    SimpleMovingMedian(),
    SimpleMovingMode(),
}

impl From<PyConstantModelType> for ConstantModelType {
    fn from(value: PyConstantModelType) -> Self {
        match value {
            PyConstantModelType::SimpleMovingAverage() => ConstantModelType::SimpleMovingAverage,
            PyConstantModelType::SmoothedMovingAverage() => {
                ConstantModelType::SmoothedMovingAverage
            }
            PyConstantModelType::ExponentialMovingAverage() => {
                ConstantModelType::ExponentialMovingAverage
            }
            PyConstantModelType::PersonalisedMovingAverage(alpha_num, alpha_den) => {
                ConstantModelType::PersonalisedMovingAverage {
                    alpha_num,
                    alpha_den,
                }
            }
            PyConstantModelType::SimpleMovingMedian() => ConstantModelType::SimpleMovingMedian,
            PyConstantModelType::SimpleMovingMode() => ConstantModelType::SimpleMovingMode,
        }
    }
}

#[pyclass(name = "DeviationModel")]
#[derive(Clone)]
pub enum PyDeviationModel {
    StandardDeviation(),
    MeanAbsoluteDeviation(),
    MedianAbsoluteDeviation(),
    ModeAbsoluteDeviation(),
    UlcerIndex(),
}

impl From<PyDeviationModel> for DeviationModel {
    fn from(value: PyDeviationModel) -> Self {
        match value {
            PyDeviationModel::StandardDeviation() => DeviationModel::StandardDeviation,
            PyDeviationModel::MeanAbsoluteDeviation() => DeviationModel::MeanAbsoluteDeviation,
            PyDeviationModel::MedianAbsoluteDeviation() => DeviationModel::MedianAbsoluteDeviation,
            PyDeviationModel::ModeAbsoluteDeviation() => DeviationModel::ModeAbsoluteDeviation,
            PyDeviationModel::UlcerIndex() => DeviationModel::UlcerIndex,
        }
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn PyTechnicalIndicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let momentum_mod = PyModule::new(m.py(), "momentum_indicators")?;
    momentum_indicators::momentum_indicators(&momentum_mod)?;
    m.add_submodule(&momentum_mod)?;
    let candle_mod = PyModule::new(m.py(), "candle_indicators")?;
    candle_indicators::candle_indicators(&candle_mod)?;
    m.add_submodule(&candle_mod)?;
    m.add_class::<PyConstantModelType>()?;
    m.add_class::<PyDeviationModel>()?;
    Ok(())
}
