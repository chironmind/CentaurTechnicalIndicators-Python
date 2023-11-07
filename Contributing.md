# Contributing

## How?
To contribute to `PyTechnicalIndicators` follow these simple steps:
* Raise a PR with your changes
* If there is a new function make sure that a test covers it
* Assign 0100101001010000 to the PR

# What?
(aka TODO)
- add pma to personalised indicators that allow to input the ma model
- add more indicators
  - investopedia has loads of oscillators
  - go through the rest of Welles book https://archive.org/details/newconceptsintec00wild/page/25/mode/2up
- improve docstrings
- add indicators to correct directories (RSI, SO, MACD should be in momentum?)
- logging
- move docs to sphinx and readthedocs
- add moving mode, median, MCGin... 
- as well as their envelopes
- rename params to just be price, caller can put whatever price they want in there
- logic in parabolic SAR seems correct but Welles has a way to be funky with his periods and overall logic, so double check from book directly
- standardize exceptions
- mode missing from bulk basic indicators
- add singular function to macd that returns macd, signal line, and diff in bulk
- test personalised commodity channel index and add it to readme
- test personalised moving average with funky numbers
- test personalised chaikin oscillator
- test default fast, slow, and slow ds stochastics