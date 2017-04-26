
# Copyright (c) 2015-2017 Agalmic Ventures LLC (www.agalmicventures.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import cherrypy
import io
import qrcode
import qrcode.constants
import qrcode.image.svg

class PqrsApplication(object):

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
