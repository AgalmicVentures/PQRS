# PQRS (Python QR Service)
PQRS is a [QR code](http://en.wikipedia.org/wiki/QR_code) generation microservice in Python 3 built on CherryPy. For testing and convenience, it includes a human-usable front end.

## API

### `/qrCode`
Generates a QR code and returns an SVG image of it.

Arguments:
* `data`: the data to be encoded
* `errorCorrection` (optional, default='L'): the type of error correction to use (L, M, Q, or H)
* `boxSize` (optional, default=10): the size of each box in pixels
* `borderWidth` (optional, default=4): the width of the borders in pixels

## Scripts

### `start.sh`, `stop.sh`, `restart.sh`
These scripts will start, stop, and restart a background instance of PQRS using `server.conf` as the configuration.
