# -*- coding: utf-8 -*-
from odoo import models, fields

#Definimos modelo Gestor Socios
class HospitalPacientes(models.Model):

    #Nombre y descripcion del modelo
    _name = 'pacientes'

    #Atributo nombre
    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    sintomas = fields.Selection([('1','Fiebre'),('2','Mucosa'),('3','Tos')])