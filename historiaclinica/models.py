from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    fecha_nacimiento = CharField(max_length=30)
    lugar_nacimiento = CharField(max_length=30)
    edad = CharField(max_length=30)
    tipo_documento =  CharField(max_length=30)
    numero_documento = CharField(max_length=30)
    lugar_expedicion = CharField(max_length=30)
    direccion = CharField(max_length=30)
    ciudad = CharField(max_length=30)
    departamento = ChardField(max_length=30)
    telefono = CharField(max_length=30)
    motivo_consulta = CharField(max_length=30)
    object_paciente = generic.GenericForeignKey()

class HistoriaClinica(models.Model):
    primer_apellido = CharField(max_length=30)
    segundo_apellido = CharField(max_length=30)
    nombre_completo = CharField(max_length=30)
    edad = CharField(max_length=30)
    sexo = CharField(max_length=30)
    fecha= CharField(max_length=30)
    numero_documento = CharField(max_length=30)
    direccion = CharField(max_length=30)
    lugar_residencia = CharField(max_length=30)
    cuadro_clinico = CharField(max_length=1000)
    antecedentes_clinico = CharField(max_length=1000)
    hallazgos_examen = CharField(max_length=1000)
    diagnostico = CharField(max_length=1000)
    observaciones = CharField(max_length=1000)
    talla = CharField(max_legth=30)
    peso = CharField(max_length=30)
    object_historia_clinica = generic.GenericForeignKey()

class VerHistoria(models.Model):
    numero_identificacion = CharField(max_length=30)
    fecha_examen = CharField(max_length=30)
    primer_apellido = CharField(max_length=30)
    segundo_apellido = CharField(max_length=30)
    nombre_completo = CharField(max_length=30)
    object_ver_historia = generic.GenericForeignKey()
