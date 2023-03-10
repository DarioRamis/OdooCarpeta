# -*- coding: utf-8 -*-
from odoo import models, fields

#Definimos modelo Gestor Socios
class InstitutoModulos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'modulos'

    #Atributo nombre
    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text( string="Descripción", required=True)  
    alumnos = fields.Many2many('alumnos', required=True, index=True)
    profesores = fields.Many2many('profesores', required=True, index=True)