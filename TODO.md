# TODO

- add pma to personalised indicators that allow to input the ma model
- add more indicators
  - investopedia has loads of oscillators but probably do pdf first
- Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface.
- improve docstrings
- add indicators to correct folders (RSI, SO, MACD should be in momentum?)
- logging
- go through the rest of Welles book https://archive.org/details/newconceptsintec00wild/page/25/mode/2up
- do hand calcs for chart_trends.py break_down_trends
- move docs to sphinx and readthedocs
- check what gets installed in reqs, doubt most of it is needed
- add moving mode, median, MCGin... 
- as well as their envelopes
## From notebook
- on balance volume and commodity channel index need docstrings
- for aroon have the function figure out the time since last high and low based on the provided period.
- rename params to just be price, caller can put whatever price they want in there
- icloud may need the baseline to also be returned?
- williams %R needs to either do the max in single function or doc string needs to tell people to do the max for the period before passing it on
- bulk other > value added personalised needs to be renamed
- no exception handling in peaks.py, valleys.py
- get overall trend needs to just accept prices as floats, then the function should add the indexes by iterating over the list
- improve break down trends for when there are only two variables, do something along the lines of exponential ma, where an extra variable or something gets added to the multiplier so that it is more flexible witht eh number of variables it takes into account. Determine whether it should be the current price being outside of the multiplier that counts or the rework of the trend. Or have it as an option. Have a new paraeter where called denominator, that essentially does the following: std_mult + (1/denom)^length of list. So that the caller can determine the sensitivity to shorter lists. This would get done to the multiplier befoe it gets applied to the bracket.
- in break down trends determine if it is best to start a new trend if the price is outside of the brakcet or the newly calculated trend. Do the two and chart it.
- bulk support and resistance needs to be done for it to be useable