from pytechnicalindicators import standard_indicators

"""The purpose of these tests are just to confirm that the bindings work.

These tests are not meant to be in depth, nor to test all edge cases, those should be
done in [RustTI](https://github.com/chironmind/RustTI). These tests exist to confirm whether an update in the bindings, or
RustTI has broken functionality.

To run the tests `maturin` needs to have built the egg. To do so run the following from
your CLI

```shell
$ source you_venv_location/bin/activate

$ pip3 install -r test_requirements.txt

$ maturin develop

$ pytest .
```
"""

prices = [200.0, 210.0, 205.0, 190.0, 195.0, 192.0, 200.0, 201.0, 187.0, 188.0, 175.0, 192.0, 200.0, 210.0, 213.0,
        227.0, 231.0, 225.0, 212.0, 211.0, 205.0, 180.0, 202.0, 216.0, 222.0, 224.0, 231.0, 238.0, 242.0, 233.0,
        235.0, 229.0, 225.0, 218.0]


def test_single_simple_moving_average():
    assert standard_indicators.single.simple_moving_average(prices) == 210.7058823529412

def test_bulk_simple_moving_average():
    assert standard_indicators.bulk.simple_moving_average(prices, 30) == [208.56666666666666, 209.73333333333332, 210.36666666666667, 211.03333333333333, 211.96666666666667]

def test_single_smoothed_moving_average():
    assert standard_indicators.single.smoothed_moving_average(prices) == 214.20874647478678

def test_bulk_smoothed_moving_average():
    assert standard_indicators.bulk.smoothed_moving_average(prices, 30) == [211.97920123916037, 213.40755601685768, 214.28612990851622, 215.02097023671016, 215.64906708402194]

def test_single_exponential_moving_average():
    assert standard_indicators.single.exponential_moving_average(prices) == 217.38500644771585

def test_bulk_exponential_moving_average():
    assert standard_indicators.bulk.exponential_moving_average(prices, 30) == [215.29552232471173, 216.91990305584258, 217.89096009276992, 218.55139303267376, 218.79831857416528]

def test_single_bollinger_bands():
    assert standard_indicators.single.bollinger_bands(prices[:20]) == (175.05324174971474, 203.2, 231.34675825028523)

def test_bulk_bollinger_bands():
    assert standard_indicators.bulk.bollinger_bands(prices) == [
            (175.05324174971474, 203.2, 231.34675825028523), (175.33256768479737, 203.45, 231.5674323152026), (172.23485234766616, 201.95, 231.66514765233381),
            (172.11768203121596, 201.8, 231.48231796878406), (173.3214842545838, 203.1, 232.8785157454162), (173.8266429012102, 204.45, 235.07335709878978),
            (174.85721237208833, 206.05, 237.2427876279117), (174.7281275251926, 207.6, 240.47187247480738), (174.19393669168377, 209.45, 244.7060633083162),
            (175.81538786794613, 212.2, 248.58461213205385), (178.77101458841634, 214.45, 250.12898541158364), (185.66651372174536, 217.45, 249.23348627825462),
            (189.40618793127916, 219.3, 249.19381206872086), (191.92501091703267, 220.55, 249.17498908296736), (192.7048234206263, 220.95, 249.19517657937368)
        ]

def test_single_macd():
    assert standard_indicators.single.macd(prices) == (6.8523139433706035, 7.639538247944125, -0.7872243045735212)

def test_bulk_macd():
    assert standard_indicators.bulk.macd(prices) == [(6.8523139433706035, 7.639538247944125, -0.7872243045735212)]

def test_single_rsi():
    assert standard_indicators.single.rsi(prices[:14]) == 42.592077184575366

def test_bulk_rsi():
    assert standard_indicators.bulk.rsi(prices) == [
                42.592077184575366, 39.07611100178124, 41.09871247382122, 39.66284547209696, 45.2853564635353, 40.1425352403162, 47.78318434262897, 50.62992249205623,
                40.8694144136562, 49.9038458687852, 50.42479952844112, 47.16160259347143, 43.46680840888576, 42.21137984176537, 42.38797749407658, 38.67521414903009,
                41.02478824688674, 36.49557287277618, 40.48032320003482, 42.707931379709024, 43.48463214774521
            ]

