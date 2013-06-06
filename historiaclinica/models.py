from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    primer_pellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateTimeField(max_length=30)
    lugar_nacimiento = models.CharField(max_length=30)
    edad = models.CharField(max_length=20) 
    TIPO_DOCUMENTO_CHOICES = (
        ('RC', 'Registro Civil'),
        ('TI', 'Tarjeta de Identidad'),
        ('CC', 'Cedula de Ciudadania'),
        ('CE', 'Cedula de Extranjeria'),
        ('PA', 'Pasaporte'),
        )
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES, default='RC')    
    numero_documento = models.CharField(max_length=30)
    lugar_expedicion = models.CharField(max_length=30)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    motivo_consulta = models.CharField(max_length=1000)
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
class HistoriaClinica(models.Model):
    fecha_toma_examen = models.DateTimeField(max_length=30)
    cuadro_clinico = models.CharField(max_length=1000)
    antecedentes_clinico = models.CharField(max_length=1000)
    hallazgos_examen = models.CharField(max_length=1000)
    diagnostico = models.CharField(max_length=1000)
    observaciones = models.CharField(max_length=1000)
    talla = models.FloatField(max_length=30)
    peso = models.FloatField(max_length=30)
    paciente = models.ForeignKey(Paciente, related_name='historias')
