use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use rust_ti::chart_trends::TrendBreakConfig;
use rust_ti::{ConstantModelType, DeviationModel, MovingAverageType, Position};

pub mod candle_indicators;
pub mod chart_trends;
pub mod correlation_indicators;
pub mod momentum_indicators;
pub mod moving_average;
pub mod other_indicators;
pub mod standard_indicators;
pub mod strength_indicators;
pub mod trend_indicators;
pub mod volatility_indicators;

#[derive(Clone)]
pub enum PyConstantModelType {
    SimpleMovingAverage,
    SmoothedMovingAverage,
    ExponentialMovingAverage,
    SimpleMovingMedian,
    SimpleMovingMode,
}

impl PyConstantModelType {
    // Add a method to create from string
    pub fn from_string(s: &str) -> PyResult<Self> {
        match s.to_lowercase().as_str() {
            "simple" | "ma" | "simple_moving_average" => Ok(PyConstantModelType::SimpleMovingAverage),
            "smoothed" | "sma" | "smoothed_moving_average" => Ok(PyConstantModelType::SmoothedMovingAverage),
            "exponential" | "ema" | "exponential_moving_average" => Ok(PyConstantModelType::ExponentialMovingAverage),
            "median" | "smm" | "simple_moving_median" => Ok(PyConstantModelType::SimpleMovingMedian),
            "mode" | "simple_moving_mode" => Ok(PyConstantModelType::SimpleMovingMode),
            _ => Err(PyValueError::new_err(format!(
                "Unknown constant model type: '{}'. Valid options are: 'simple', 'smoothed', 'exponential', 'median', 'mode'", 
                s
            )))
        }
    }
}

impl From<PyConstantModelType> for ConstantModelType {
    fn from(value: PyConstantModelType) -> Self {
        match value {
            PyConstantModelType::SimpleMovingAverage => ConstantModelType::SimpleMovingAverage,
            PyConstantModelType::SmoothedMovingAverage => ConstantModelType::SmoothedMovingAverage,
            PyConstantModelType::ExponentialMovingAverage => {
                ConstantModelType::ExponentialMovingAverage
            }
            PyConstantModelType::SimpleMovingMedian => ConstantModelType::SimpleMovingMedian,
            PyConstantModelType::SimpleMovingMode => ConstantModelType::SimpleMovingMode,
        }
    }
}

impl PyDeviationModel {
    pub fn from_string(s: &str) -> PyResult<Self> {
        match s.to_lowercase().as_str() {
            "standard" | "std" | "standard_deviation" => Ok(PyDeviationModel::StandardDeviation),
            "mean" | "mean_absolute_deviation" => Ok(PyDeviationModel::MeanAbsoluteDeviation),
            "median" | "median_absolute_deviation" => Ok(PyDeviationModel::MedianAbsoluteDeviation),
            "mode" | "mode_absolute_deviation" => Ok(PyDeviationModel::ModeAbsoluteDeviation),
            "ulcer" | "ulcer_index" => Ok(PyDeviationModel::UlcerIndex),
            _ => Err(PyValueError::new_err(format!(
                "Unknown deviation model: '{}'. Valid options are: 'standard', 'mean', 'median', 'mode', 'ulcer'",
                s
            )))
        }
    }
}

#[derive(Clone)]
pub enum PyDeviationModel {
    StandardDeviation,
    MeanAbsoluteDeviation,
    MedianAbsoluteDeviation,
    ModeAbsoluteDeviation,
    UlcerIndex,
}

impl From<PyDeviationModel> for DeviationModel {
    fn from(value: PyDeviationModel) -> Self {
        match value {
            PyDeviationModel::StandardDeviation => DeviationModel::StandardDeviation,
            PyDeviationModel::MeanAbsoluteDeviation => DeviationModel::MeanAbsoluteDeviation,
            PyDeviationModel::MedianAbsoluteDeviation => DeviationModel::MedianAbsoluteDeviation,
            PyDeviationModel::ModeAbsoluteDeviation => DeviationModel::ModeAbsoluteDeviation,
            PyDeviationModel::UlcerIndex => DeviationModel::UlcerIndex,
        }
    }
}

#[derive(Clone)]
pub enum PyMovingAverageType {
    Simple,
    Smoothed,
    Exponential,
}

impl PyMovingAverageType {
    pub fn from_string(s: &str) -> PyResult<Self> {
        match s.to_lowercase().as_str() {
            "simple" => Ok(PyMovingAverageType::Simple),
            "smoothed" => Ok(PyMovingAverageType::Smoothed),
            "exponential" => Ok(PyMovingAverageType::Exponential),
            _ => Err(PyValueError::new_err(format!(
                "Unknown moving average type: '{}'. Valid options are: 'simple', 'smoothed', 'exponential'",
                s
            )))
        }
    }
}

impl From<PyMovingAverageType> for MovingAverageType {
    fn from(value: PyMovingAverageType) -> Self {
        match value {
            PyMovingAverageType::Simple => MovingAverageType::Simple,
            PyMovingAverageType::Smoothed => MovingAverageType::Smoothed,
            PyMovingAverageType::Exponential => MovingAverageType::Exponential,
        }
    }
}

#[derive(Clone)]
pub enum PyPosition {
    Long,
    Short,
}

impl PyPosition {
    pub fn from_string(s: &str) -> PyResult<Self> {
        match s.to_lowercase().as_str() {
            "long" => Ok(PyPosition::Long),
            "short" => Ok(PyPosition::Short),
            _ => Err(PyValueError::new_err(format!(
                "Unknown position: '{}'. Valid options are: `long`, `short`",
                s
            ))),
        }
    }
}

impl From<PyPosition> for Position {
    fn from(value: PyPosition) -> Self {
        match value {
            PyPosition::Long => Position::Long,
            PyPosition::Short => Position::Short,
        }
    }
}

#[derive(Clone)]
pub enum PyTrendBreakConfig {
    Default,
    Conservative,
    Moderate,
    Aggressive,
    Custom {
        max_outliers: usize,
        soft_adj_r_squared_minimum: f64,
        hard_adj_r_squared_minimum: f64,
        soft_rmse_multiplier: f64,
        hard_rmse_multiplier: f64,
        soft_durbin_watson_min: f64,
        soft_durbin_watson_max: f64,
        hard_durbin_watson_min: f64,
        hard_durbin_watson_max: f64,
    },
}

impl PyTrendBreakConfig {
    pub fn from_string(s: &str) -> PyResult<Self> {
        match s.to_lowercase().as_str() {
            "default" => Ok(PyTrendBreakConfig::Default),
            "conservative" => Ok(PyTrendBreakConfig::Conservative),
            "moderate" => Ok(PyTrendBreakConfig::Moderate),
            "aggressive" => Ok(PyTrendBreakConfig::Aggressive),
            _ => Err(PyValueError::new_err(format!(
                "Unknown trend break config: '{}'. Valid options are: 'default', 'conservative', 'moderate', 'aggressive'",
                s
            ))),
        }
    }

    pub fn custom(
        max_outliers: usize,
        soft_adj_r_squared_minimum: f64,
        hard_adj_r_squared_minimum: f64,
        soft_rmse_multiplier: f64,
        hard_rmse_multiplier: f64,
        soft_durbin_watson_min: f64,
        soft_durbin_watson_max: f64,
        hard_durbin_watson_min: f64,
        hard_durbin_watson_max: f64,
    ) -> Self {
        PyTrendBreakConfig::Custom {
            max_outliers,
            soft_adj_r_squared_minimum,
            hard_adj_r_squared_minimum,
            soft_rmse_multiplier,
            hard_rmse_multiplier,
            soft_durbin_watson_min,
            soft_durbin_watson_max,
            hard_durbin_watson_min,
            hard_durbin_watson_max,
        }
    }
}

impl From<PyTrendBreakConfig> for TrendBreakConfig {
    fn from(value: PyTrendBreakConfig) -> Self {
        match value {
            PyTrendBreakConfig::Default => TrendBreakConfig::default(),
            PyTrendBreakConfig::Conservative => TrendBreakConfig {
                max_outliers: 2,
                soft_adj_r_squared_minimum: 0.4,
                hard_adj_r_squared_minimum: 0.2,
                soft_rmse_multiplier: 1.5,
                hard_rmse_multiplier: 2.5,
                soft_durbin_watson_min: 1.2,
                soft_durbin_watson_max: 2.8,
                hard_durbin_watson_min: 0.9,
                hard_durbin_watson_max: 3.1,
            },
            PyTrendBreakConfig::Moderate => TrendBreakConfig::default(),
            PyTrendBreakConfig::Aggressive => TrendBreakConfig {
                max_outliers: 0,
                soft_adj_r_squared_minimum: 0.1,
                hard_adj_r_squared_minimum: 0.01,
                soft_rmse_multiplier: 1.1,
                hard_rmse_multiplier: 1.5,
                soft_durbin_watson_min: 0.8,
                soft_durbin_watson_max: 3.2,
                hard_durbin_watson_min: 0.5,
                hard_durbin_watson_max: 3.5,
            },
            PyTrendBreakConfig::Custom {
                max_outliers,
                soft_adj_r_squared_minimum,
                hard_adj_r_squared_minimum,
                soft_rmse_multiplier,
                hard_rmse_multiplier,
                soft_durbin_watson_min,
                soft_durbin_watson_max,
                hard_durbin_watson_min,
                hard_durbin_watson_max,
            } => TrendBreakConfig {
                max_outliers,
                soft_adj_r_squared_minimum,
                hard_adj_r_squared_minimum,
                soft_rmse_multiplier,
                hard_rmse_multiplier,
                soft_durbin_watson_min,
                soft_durbin_watson_max,
                hard_durbin_watson_min,
                hard_durbin_watson_max,
            },
        }
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn pytechnicalindicators(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let momentum_mod = PyModule::new(m.py(), "momentum_indicators")?;
    let _ = momentum_indicators::momentum_indicators(&momentum_mod)?;
    m.add_submodule(&momentum_mod)?;
    let candle_mod = PyModule::new(m.py(), "candle_indicators")?;
    let _ = candle_indicators::candle_indicators(&candle_mod)?;
    m.add_submodule(&candle_mod)?;
    let trend_mod = PyModule::new(m.py(), "trend_indicators")?;
    let _ = trend_indicators::trend_indicators(&trend_mod)?;
    m.add_submodule(&trend_mod)?;
    let strength_mod = PyModule::new(m.py(), "strength_indicators")?;
    let _ = strength_indicators::strength_indicators(&strength_mod)?;
    m.add_submodule(&strength_mod)?;
    let other_mod = PyModule::new(m.py(), "other_indicators")?;
    let _ = other_indicators::other_indicators(&other_mod)?;
    m.add_submodule(&other_mod)?;
    let standard_mod = PyModule::new(m.py(), "standard_indicators")?;
    let _ = standard_indicators::standard_indicators(&standard_mod)?;
    m.add_submodule(&standard_mod)?;
    let chart_mod = PyModule::new(m.py(), "chart_trends")?;
    let _ = chart_trends::chart_trends(&chart_mod)?;
    m.add_submodule(&chart_mod)?;
    let corr_mod = PyModule::new(m.py(), "correlation_indicators")?;
    let _ = correlation_indicators::correlation_indicators(&corr_mod)?;
    m.add_submodule(&corr_mod)?;
    let vol_mod = PyModule::new(m.py(), "volatility_indicators")?;
    let _ = volatility_indicators::volatility_indicators(&vol_mod)?;
    m.add_submodule(&vol_mod)?;
    let ma_mod = PyModule::new(m.py(), "moving_average")?;
    let _ = moving_average::moving_average(&ma_mod)?;
    m.add_submodule(&ma_mod)?;
    Ok(())
}
