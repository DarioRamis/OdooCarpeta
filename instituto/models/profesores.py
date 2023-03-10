# -*- coding: utf-8 -*-
from odoo import models, fields

#Definimos modelo Gestor Socios
class InstitutoProfesores(models.Model):

    #Nombre y descripcion del modelo
    _name = 'profesores'

    #Atributo nombre
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char( string="Apellido", required=True)    