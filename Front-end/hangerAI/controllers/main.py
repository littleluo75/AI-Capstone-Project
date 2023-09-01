
import json
import logging
from datetime import datetime
from werkzeug.exceptions import Forbidden, NotFound
from werkzeug.urls import url_decode, url_encode, url_parse

from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.fields import Command
from odoo.http import request
from odoo.addons.base.models.ir_qweb_fields import nl2br
from odoo.addons.http_routing.models.ir_http import slug
_logger = logging.getLogger(__name__)

class HangerAPI(http.Controller):
    @http.route([
        '/hanger',
    ], type='http', auth="public", website=True)
    def hanger(self, **post):
        _logger.info("Post::::", post)
        values = {}
        return request.render("hangerAI.hanger_dashboard", values)