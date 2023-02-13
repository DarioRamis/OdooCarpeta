# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api

#Definimos modelo Gestor Socios
class PrestamosComics(models.Model):

    #Nombre y descripcion del modelo
    _name = 'prestamo'

    #Atributo nombre
    nombreComic = fields.Many2one('biblioteca.comic', string='Nombre Comic', required=True, index=True)
    nombreSocio = fields.Many2one('socios', string='Nombre Socio', required=True, index=True)    
    fechaInicio = fields.Date('Fecha Prestamo', required=True)
    fechaFinal = fields.Date('Fecha Devolucion', required=True)

    @api.constrains('fechaInicio')
    def _check_release_initial_date(self):
        # Recorremos el modelo
        for record in self:
            #Comprobamos de cada registro, primero que haya una fecha_publicacion
            #y tras ello, que la fecha no sea posterior a la actual.
            if record.fechaInicio and record.fechaInicio < fields.Date.today():
                #Si procede, lanzamos una excepcion
                raise models.ValidationError('La fecha de préstamo debe ser posterior a la actual')

    @api.constrains('fechaFinal')
    def _check_release_final_date(self):
        # Recorremos el modelo
        for record in self:
            #Comprobamos de cada registro, primero que haya una fecha_publicacion
            #y tras ello, que la fecha no sea posterior a la actual.
            if record.fechaFinal and record.fechaFinal < record.fechaInicio:
                #Si procede, lanzamos una excepcion
                raise models.ValidationError('La fecha de devolución debe ser posterior a la fecha de préstamo')

