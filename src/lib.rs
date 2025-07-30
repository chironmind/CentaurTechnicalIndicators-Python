use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use rust_ti::{ConstantModelType, DeviationModel, MovingAverageType};

pub mod candle_indicators;
pub mod momentum_indicators;
pub mod other_indicators;
pub mod strength_indicators;
pub mod trend_indicators;
pub mod standard_indicators;
pub mod chart_trends;
pub mod correlation_indicators;
pub mod volatility_indicators;
pub mod moving_average;

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

#[pyclass(name = "MovingAverageType")]
#[derive(Clone)]
pub enum PyMovingAverageType {
    Simple(),
    Smoothed(),
    Exponential(),
    Personalised(f64, f64)
}

impl From<PyMovingAverageType> for MovingAverageType {
    fn from(value: PyMovingAverageType) -> Self {
        match value {
            PyMovingAverageType::Simple() => MovingAverageType::Simple,
            PyMovingAverageType::Smoothed() => MovingAverageType::Smoothed,
            PyMovingAverageType::Exponential() => MovingAverageType::Exponential,
            PyMovingAverageType::Personalised(alpha_num, alpha_den) => MovingAverageType::Personalised {
                alpha_num,
                alpha_den,
            }
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
    let trend_mod = PyModule::new(m.py(), "trend_indicators")?;
    trend_indicators::trend_indicators(&trend_mod)?;
    m.add_submodule(&trend_mod)?;
    let strength_mod = PyModule::new(m.py(), "strength_indicators")?;
    strength_indicators::strength_indicators(&strength_mod)?;
    m.add_submodule(&strength_mod)?;
    let other_mod = PyModule::new(m.py(), "other_indicators")?;
    other_indicators::other_indicators(&other_mod)?;
    m.add_submodule(&other_mod)?;
    let standard_mod = PyModule::new(m.py(), "standard_indicators")?;
    standard_indicators::standard_indicators(&standard_mod)?;
    m.add_submodule(&standard_mod)?;
    let chart_mod = PyModule::new(m.py(), "chart_trends")?;
    chart_trends::chart_trends(&chart_mod)?;
    m.add_submodule(&chart_mod)?;
    let corr_mod = PyModule::new(m.py(), "correlation_indicators")?;
    correlation_indicators::correlation_indicators(&corr_mod)?;
    m.add_submodule(&corr_mod)?;
    let vol_mod = PyModule::new(m.py(), "volatility_indicators")?;
    volatility_indicators::volatility_indicators(&vol_mod)?;
    m.add_submodule(&vol_mod)?;
    let ma_mod = PyModule::new(m.py(), "moving_average")?;
    moving_average::moving_average(&ma_mod)?;
    m.add_submodule(&ma_mod)?;
    m.add_class::<PyConstantModelType>()?;
    m.add_class::<PyDeviationModel>()?;
    m.add_class::<PyMovingAverageType>()?;
    Ok(())
}
