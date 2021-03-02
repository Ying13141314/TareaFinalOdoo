# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hospital_profesional(models.Model):
    _name = "hospital.profesional"

    nombre = fields.Char(string="Nombre",required=True,help="Introduce el nombre")
    apellidos = fields.Char(string="Apellidos",required=True,help="Introduce los apellidos")
    description = fields.Text(string="Descripción")
    tipoProfesional = fields.Text(string="Tipo de profesional")
    sueldo = fields.Float(string="Sueldo")
    edad = fields.Integer(string = "Edad")

class hospital_habitacion(models.Model):
    _name = "hospital.habitacion"

    numeroHabitacion = fields.Integer(string="Número de habitación",required=True)
    cantidadCama = fields.Integer(string="Cantidad de cama")
    fechaEnUso = fields.Datetime(string="Fecha en uso")
    fechaNoUso = fields.Datetime(string="Fecha que dejo de ser usado")
    estado = fields.Selection([('0','Libre'),('1','Ocupado')],string="Estado",default="0")

class hospital_cliente(models.Model):
    _name = "hospital.cliente"

    nombre = fields.Char(string="Nombre",required=True,help="Introduce el nombre")
    apellido = fields.Char(string="Apellidos",required=True,help="Introduce los apellidos")
    edad = fields.Integer(string = "Edad")
    fechaEntrada = fields.Datetime(string="Fecha de entrada")
    fechaSalida = fields.Datetime(string="Fecha de salida")
    

# class libreria(models.Model):
#     _name = 'libreria.libreria'
#     _description = 'libreria.libreria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
