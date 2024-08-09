# refinipy

## Info

Some helper functions to request data using the refinitiv eikon API.

Implemented at the moment are following functions:

- `ric_cds(ric_equity)`: get RIC codes of CDS for corresponding equity RIC
- `get_cds(ric_cds)`: get CDS data for corresponding CDS RIC
- `get_price_to_book(ric_equity)`: get price to book data for corresponding equity RIC
- `get_stockprice(ric_equity)`: get stock price data for corresponding equity RIC

# Sample code

The file `demo.py` contains some democode which applies the relevant functions.

Note that you need to set the refinitiv eikon API-key to be able to fetch data.

You can do this using the eikon package:

```
import eikon as ek
ek.set_app_key(your_api_apikey)
```

Or use the utils contained in this package. If you want to utilize the util-function in `config.py` from this repo, create following class stored as `credentials.py`:

```
class apikeys:
    eikon = "your_api_key"
```

Then, run `config.connect()`.

