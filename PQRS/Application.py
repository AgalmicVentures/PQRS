
import cherrypy
import io
import qrcode
import qrcode.constants
import qrcode.image.svg

class PqrsApplication:

	def __init__(self):
		with io.open('./templates/index.html') as indexTemplateFile:
			self.indexTemplate = indexTemplateFile.read()

	@cherrypy.expose
	def index(self):
		return self.indexTemplate % {
			'title': 'Home',
		}

	@cherrypy.expose
	def qrCode(self, data, errorCorrection='L', boxSize='10', borderWidth='4'):
		parsedErrorCorrection = {
			'L': qrcode.constants.ERROR_CORRECT_L,
			'M': qrcode.constants.ERROR_CORRECT_M,
			'Q': qrcode.constants.ERROR_CORRECT_Q,
			'H': qrcode.constants.ERROR_CORRECT_H,
		}.get(errorCorrection, qrcode.constants.ERROR_CORRECT_L)

		try:
			parsedBoxSize = int(boxSize)
		except ValueError:
			parsedBoxSize = 10

		try:
			parsedBorderWidth = int(borderWidth)
		except ValueError:
			parsedBorderWidth = 4

		#Generate the image
		svg = qrcode.make(data,
			error_correction=parsedErrorCorrection,
			box_size=parsedBoxSize,
			border=parsedBorderWidth,
			image_factory=qrcode.image.svg.SvgImage)

		#Output it to a string
		output = io.BytesIO()
		svg.save(output)
		image = output.getvalue()

		cherrypy.response.headers['Content-Type'] = 'image/svg+xml'
		return image

	@cherrypy.expose
	def default(self, *args, **kwargs):
		return '<html><body><h1>PQRS - Page Not Found</h1></body></html>'
