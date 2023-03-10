# -*- coding: utf-8 -*-
from odoo import models, fields

#Definimos modelo Gestor Socios
class InstitutoCiclosFormativos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'ciclos'

    #Atributo nombre
    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text( string="Descripción", required=True)    
    modulosVarios = fields.Many2many('modulos', required=True, index=True)