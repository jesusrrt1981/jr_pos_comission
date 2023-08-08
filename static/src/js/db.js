odoo.define('jr_pos_comission.DB', function (require) {
    'use strict';
    const PosDB = require('point_of_sale.DB');
    PosDB.include({
        init: function () {
            this._super.apply(this, arguments);
            this.employee_by_id = {};
        },
        add_employees: function(employees){
            if(!(employees instanceof Array)){
                employees = [employees];
            }
            for(var i = 0, len = employees.length; i < len; i++){
                var employee = employees[i];
                if (employee.id in this.employee_by_id) continue;
                this.employee_by_id[employee.id] = employee;
            }
        },
        get_employee_by_id: function(id){
            return this.employee_by_id[id];
        },
    });
});
