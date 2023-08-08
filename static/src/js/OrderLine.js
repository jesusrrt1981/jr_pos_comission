odoo.define('jr_pos_comission.Orderline', function(require) {
    'use strict';

    const OrderLine = require('point_of_sale.Orderline');
    const Registries = require('point_of_sale.Registries');
    const { useState } = owl;

    const EmployeeOrderLine = OrderLine =>
        class extends OrderLine {
            get addedClasses() {
                const res = super.addedClasses;
                Object.assign(res, {
                    employee: this.props.line.employee,
                });
                return res;
            }
            captureChangeEmployee(event) {
                let employee_id = event.target.value;
                const line = this.props.line;
                const employee = this.env.pos.db.get_employee_by_id(employee_id)
                line.set_employee(employee);
            }
        };

    Registries.Component.extend(OrderLine, EmployeeOrderLine);

    return OrderLine;
});
