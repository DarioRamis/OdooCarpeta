# -*- coding: utf-8 -*-
from odoo import models, fields

#Definimos modelo Gestor Socios
class GestorSocios(models.Model):

    #Nombre y descripcion del modelo
    _name = 'socios'

    #Atributo nombre
    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    id = fields.Char(string='ID', required=True)
    