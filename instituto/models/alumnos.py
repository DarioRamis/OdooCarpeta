# -*- coding: utf-8 -*-
from odoo import models, fields

#Definimos modelo Gestor Socios
class InstitutoAlumnos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'alumnos'

    #Atributo nombre
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char( string="Apellido", required=True)    
    