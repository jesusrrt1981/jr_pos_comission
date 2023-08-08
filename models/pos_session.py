from odoo import models, api


class PosSession(models.Model):
    _inherit = "pos.session"

    def _pos_data_process(self, loaded_data):
        params = self._loader_params_employees_commission_list()
        employees_commission_list = self._get_pos_ui_employees_commission_list(params)
        loaded_data['employees_commission_list'] = employees_commission_list
        super(PosSession, self)._pos_data_process(loaded_data)

    def _loader_params_employees_commission_list(self):
        domain = [('company_id', '=', self.config_id.company_id.id), ('is_commission', '=', True)]
        return {'search_params': {'domain': domain, 'fields': ['id', 'name']}}

    def _get_pos_ui_employees_commission_list(self, params):
        employees = self.env['hr.employee'].search_read(**params['search_params'])
        return employees
