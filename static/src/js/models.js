/* global waitForWebfonts */
odoo.define('jr_pos_comission.models', function (require) {
"use strict";

const { PosGlobalState } = require('point_of_sale.models');
const { Orderline } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');
const { uuidv4 } = require('point_of_sale.utils');
const core = require('web.core');
const Printer = require('point_of_sale.Printer').Printer;
const { batched } = require('point_of_sale.utils')
const QWeb = core.qweb;

const EmployeePosGlobalState = (PosGlobalState) => class EmployeePosGlobalState extends PosGlobalState {
    constructor(obj) {
        super(obj);
        this.employees_commission = [];

    }
    //@override
    async _processData(loadedData) {
        await super._processData(...arguments);
        this.employees_commission = loadedData['employees_commission_list'];
        this.addEmployees(this.employees_commission);
    }

    addEmployees(employees) {
        return this.db.add_employees(employees);
    }

}
Registries.Model.extend(PosGlobalState, EmployeePosGlobalState);


const EmployeeOrderline = (Orderline) => class EmployeeOrderline extends Orderline {
  constructor() {
      super(...arguments);
      this.employee = this.employee || {};
  }
  clone(){
        const orderline = super.clone(...arguments);
        orderline.employee = this.employee;
        return orderline;
    }
  export_as_JSON() {
      const json = super.export_as_JSON(...arguments);
      json.employee = this.employee;
      return json;
  }
  init_from_JSON(json) {
      super.init_from_JSON(...arguments);
      this.set_employee(json.employee);
  }
  get_employee(){
        return this.employee;
    }
  set_employee(employee) {
        this.employee = employee;
    }
}
Registries.Model.extend(Orderline, EmployeeOrderline);



});
