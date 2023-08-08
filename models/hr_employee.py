from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    is_commission = fields.Boolean(default=False, string="Is commission?")

    comission_ids=fields.One2many("employee.comission","employee_id")

class Comissions(models.Model):
    _name="employee.comission"

    employee_id=fields.Many2one("hr.employee")
    product_id=fields.Many2one("product.product",string="Producto")
    comision=fields.Float("Comission %")

class reportcomission(models.TransientModel):
    _name="report.comission1"

    start=fields.Date(string="Fecha inicio")
    end=fields.Date(string="Fecha Fin")
    empleados=fields.Many2many("hr.employee",string="Empleados",domain="[('is_commission','=',True)]")

    def generate(self):
        report = self.env.ref("jr_pos_comission.pos_summary_report")
        return report.report_action(self)

    def get_data(self):
        obj=self.env["pos.order.line"].search([
            ("order_id.date_order",">=",self.start),
            ("order_id.date_order","<=",self.end),
            ("employee_id","in",self.empleados.ids),
        ])

        return obj

    def totales(self):
        obj=self.get_data()
        eployee=obj.mapped("employee_id")

        sumary=[
            [empleado, sum(com.comission for com in obj.filtered(lambda x: x.employee_id==empleado))]
            for empleado in eployee
        ]

        return sumary