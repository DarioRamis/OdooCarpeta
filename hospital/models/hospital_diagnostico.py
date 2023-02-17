# -*- coding: utf-8 -*-
from odoo import models, fields

#Definimos modelo Gestor Socios
class HospitalDiagnosticos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'diagnosticos'

    #Atributo nombre
    medico = fields.Many2one('medicos', string="Medico", required=True)
    paciente = fields.Many2one('pacientes', string="Paciente", required=True)    
    diagnostico = fields.Text(required=True)