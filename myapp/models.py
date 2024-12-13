from django.db import models
from datetime import datetime, time
from django.utils import timezone

# Create your models here.

class RegistroRacks(models.Model):
    RACKS = [
        ('ICESTA 1','ICESTA 1'),
        ('ICESTA 2','ICESTA 2'),
        ('ICESTA 3','ICESTA 3'),
        ('ICESTA 4','ICESTA 4'),
        ('ICESTA 5','ICESTA 5'),
        ('ICESTA 6','ICESTA 6'),
        ('RACK 7','RACK 7'),
        ('ICESTA 8','ICESTA 8'),
        ('ICESTA 9','ICESTA 9'),
        ('RACK 10-11','RACK 10-11'),
        ('RACK 12-13','RACK 12-13'),
        ('ICESTA 14','ICESTA 14'),
        ('RACK 15-16','RACK 15-16'),
        ('ICESTA 17','ICESTA 17'),
        ('ICESTA 18','ICESTA 18'),
        ('ICESTA 19','ICESTA 19'),
        ('ICESTA 20','ICESTA 20'),
        ('SISTEMA NH3','SISTEMA NH3'),
    ]
    Estado =[
        ('Muy Sucio', 'Muy Sucio'),
        ('Sucio', 'Sucio'),
        ('Limpio', 'Limpio'),
    ]
    Niveles = [
        ('Alto', 'Alto'),
        ('Medio', 'Medio'),
        ('Bajo', 'Bajo'),
    ]
    
    FECHA = models.DateField(auto_now_add=True)
    HORA = models.TimeField(auto_now_add=True)
    RACKS = models.CharField(max_length=100, choices=RACKS , default='ICESTA 1')
    ESTADO_DEL_CONDENSADOR = models.CharField(max_length=20, choices=Estado,default='Sucio')
    NIVEL_DE_REFRIGERANTE = models.CharField(max_length=20, choices=Niveles, default='Medio')
    PRESION_ALTA_PSIG = models.PositiveIntegerField()
    PRESION_DE_BAJA_COMP_1 = models.PositiveIntegerField(null=True,blank=True)
    PRESION_DE_BAJA_COMP_2 = models.PositiveIntegerField(null=True,blank=True)
    CORRIENTE = models.PositiveIntegerField(null=True,blank=True)
    VOLTAJE = models.PositiveIntegerField(null=True,blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['RACKS', 'FECHA'], name='unique_rack_per_day')
        ]

    
    def __str__(self):
        return f"Registro de {self.FECHA}"

    def save(self, *args, **kwargs):
        now = datetime.now()
        self.FECHA = now.date()
        self.HORA = now.time()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.RACKS} - {self.FECHA} {self.HORA}" 

class RegistroMaquinas(models.Model):
    MAQUINA_DE_FREON = [
        ('ICESTA 1','ICESTA 1'),
        ('ICESTA 2','ICESTA 2'),
        ('ICESTA 3','ICESTA 3'),
        ('ICESTA 4','ICESTA 4'),
        ('ICESTA 5','ICESTA 5'),
        ('ICESTA 6','ICESTA 6'),
        ('ICESTA 7','ICESTA 7'),
        ('ICESTA 8','ICESTA 8'),
        ('ICESTA 9','ICESTA 9'),
        ('ICESTA 10','ICESTA 10'),
        ('ICESTA 11','ICESTA 11'),
        ('ICESTA 12','ICESTA 12'),
        ('ICESTA 13','ICESTA 13'),
        ('ICESTA 14','ICESTA 14'),
        ('ICESTA 15','ICESTA 15'),
        ('ICESTA 16','ICESTA 16'),
        ('ICESTA 17','ICESTA 17'),
        ('ICESTA 18','ICESTA 18'),
        ('ICESTA 19','ICESTA 19'),
        ('ICESTA 20','ICESTA 20'),
        ('HOWE 1','HOWE 1'),
        ('HOWE 2','HOWE 2'),
        ('HOWE 3','HOWE 3'),
        ('GENEGLACE 1','GENEGLACE 1'),
        ('GENEGLACE 2','GENEGLACE 2'),
        ('GENEGLACE 3','GENEGLACE 3'),
        ('GENEGLACE 4','GENEGLACE 4'),
        ('CHILLER','CHILLER'),
    ]
    HORARIO =[
        ('8:00','8:00'),
        ('18:00','18:00'),
        ('22:00','22:00'),
    ]
    MOT_PARADA = [
        ('NINGUNO', 'NINGUNO'),
        ('SILO LLENO', 'SILO LLENO'),
        ('VOLTAJE ALTO', 'VOLTAJE ALTO'),
        ('FALLA ELÉCTRICA', 'FALLA ELÉCTRICA'),
        ('FALLA MECÁNICA', 'FALLA MECÁNICA'),
        ('FALLA REFRIGERACION', 'FALLA REFRIGERACION'),
        ('MTTO. PLANIFICADO', 'MTTO. PLANIFICADO'),
        ('CORTE DE ENERGÍA', 'CORTE DE ENERGÍA'),
        ('REPARACIÓN DE BAZUCA', 'REPARACIÓN DE BAZUCA'),    
    ]

    FECHA = models.DateField(auto_now_add=True)
    HORA = models.TimeField(auto_now_add=True)
    MAQUINA_DE_FREON = models.CharField(max_length=20, choices=MAQUINA_DE_FREON, default='ICESTA 1')
    HORARIO = models.CharField(max_length=20, choices=HORARIO, default="8:00")
    TEMPERATURA_DE_AGUA_DE_INGRESO = models.PositiveIntegerField()
    TEMPERATURA_DE_AGUA_DE_TINA = models.PositiveIntegerField()
    SALINIDAD_DE_AGUA_EN_TINA = models.PositiveIntegerField()
    PRESION_BAJA_PSIG = models.PositiveIntegerField()
    CORRIENTE = models.PositiveIntegerField()
    VOLTAJE = models.PositiveIntegerField()
    CONTOMETRO_1 = models.PositiveIntegerField(null=True,blank=True)
    CONTOMETRO_2 = models.PositiveIntegerField(null=True,blank=True)
    MOTIVO_DE_PARADA = models.CharField(max_length=25, choices=MOT_PARADA, default='NINGUNO')
    HORAS_DE_PARADA=models.PositiveIntegerField(null=True,blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['MAQUINA_DE_FREON', 'FECHA', 'HORARIO'], name='unique_MAQUINA_DE_FREON_per_day')
        ]

    def __str__(self):
        return f"Registro de {self.FECHA}"

    def save(self, *args, **kwargs):
        now = datetime.now()
        self.FECHA = now.date()
        self.HORA = now.time()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.MAQUINA_DE_FREON} - {self.FECHA} {self.HORA}"

class RegistroContometro(models.Model):
    FECHA = models.DateField()  # Fecha del registro
    MAQUINA = models.CharField(max_length=100)  # Máquina involucrada
    HORARIO = models.TimeField()  # Hora del registro
    CONTOMETRO = models.IntegerField(null=True,blank=True)  # Valor del contómetro
    TONELADA = models.IntegerField()
    CONTOMETRO2 = models.IntegerField(null=True,blank=True)  # Valor del contómetro
    TONELADA2 = models.IntegerField()

    class Meta:
        ordering = ['FECHA', 'HORARIO']  # Ordenar por fecha y hora
        unique_together = ('FECHA', 'MAQUINA', 'HORARIO')  # Evita duplicados
        
    def __str__(self):
        return f"{self.FECHA} - {self.MAQUINA} - {self.HORARIO} - {self.CONTOMETRO} - {self.CONTOMETRO2}"