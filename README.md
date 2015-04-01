
# PQRS (Python QR Service)

PQRS is a QR code generation microservice in Python 3 built on CherryPy.

## API

### `/qrCode`
Generates a QR code and returns an SVG image of it.

Arguments:
* `data`: the data to be encoded
* `errorCorrection` (optional, default='L'): the type of error correction to use
* `boxSize` (optional, default=10): the size of each box in pixels
* `borderWidth` (optional, default=4): the width of the borders in pixels
