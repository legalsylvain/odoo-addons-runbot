# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models
from odoo.tools import config as odoo_config


class RunbotRepo(models.Model):
    _inherit = "runbot.repo"

    def clone(self):
        for repo in self:
            repo._clone()

    def update_git(self):
        for repo in self:
            repo._update_git(False)

    def update_git_force(self):
        for repo in self:
            repo._update_git(True)

    def _root(self):
        root_path = odoo_config.get("runbot_root_path", False)
        if not root_path:
            return super()._root()
        return root_path
