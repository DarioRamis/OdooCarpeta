# -*- coding: utf-8 -*-
from odoo import models, fields

#Definimos modelo Gestor Socios
class HospitalMedicos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'medicos'

    #Atributo nombre
    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    numeroColegiado = fields.Integer(string="Numero Colegiado", required=True)