# TODO

- add pma to personalised indicators that allow to input the ma model
- add more indicators
  - investopedia has loads of oscillators
  - go through the rest of Welles book https://archive.org/details/newconceptsintec00wild/page/25/mode/2up
- Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface.
- improve docstrings
- add indicators to correct directories (RSI, SO, MACD should be in momentum?)
- logging
- move docs to sphinx and readthedocs
- check what gets installed in reqs, doubt most of it is needed
- add moving mode, median, MCGin... 
- as well as their envelopes
- rename params to just be price, caller can put whatever price they want in there
- arron up/down is the period at t 0 or 1. For a list of 10 prices, going back in reverse order to figure out the period
    since high or low, the first occurence would be t would that count as 0 because you don't say that you're at period 1 at t?
- single aroon up should be similar to the bulk, accepting a list of prices and figuring out the local max, or should be renamed. Essentially extract what the bulk function is doing.
