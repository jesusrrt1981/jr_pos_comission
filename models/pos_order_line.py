from odoo import api, fields, models, _


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    comission=fields.Float("Comision",compute="get_commission",strore="True")

    @api.depends("product_id","employee_id")
    def get_commission(self):
        for line in self:
            if line.employee_id.comission_ids:
                line.comission=0
                for record in line.employee_id.comission_ids:
                    if line.product_id.id==record.product_id.id:
                        line.comission=line.price_subtotal*(record.comision/100)
            else:
                line.comission=0


    def _order_line_fields(self, line, session_id=None):
        if line and 'employee' in line[2]:
            if line[2]['employee']:
                line[2]['employee_id'] = line[2]['employee']['id']
        return super(PosOrderLine, self)._order_line_fields(line, session_id)

    employee_id = fields.Many2one("hr.employee", string="Employee", domain=[('is_commission', '=', True)])

    def _export_for_ui(self, orderline):
        res = super(PosOrderLine, self)._export_for_ui(orderline)
        res['employee_id'] = orderline.employee_id.id
        return res
