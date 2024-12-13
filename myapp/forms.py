from datetime import date
from django.core.exceptions import ValidationError
from django import forms
from .models import RegistroRacks, RegistroMaquinas

class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroRacks
        fields = [
            'RACKS',
            'ESTADO_DEL_CONDENSADOR',
            'NIVEL_DE_REFRIGERANTE',
            'PRESION_ALTA_PSIG',
            'PRESION_DE_BAJA_COMP_1',
            'PRESION_DE_BAJA_COMP_2',
            'CORRIENTE',
            'VOLTAJE',
        ]
    


class RegistroMQ(forms.ModelForm):
    class Meta:
        model = RegistroMaquinas
        fields = [
            'MAQUINA_DE_FREON',
            'HORARIO',
            'TEMPERATURA_DE_AGUA_DE_INGRESO',
            'TEMPERATURA_DE_AGUA_DE_TINA',
            'SALINIDAD_DE_AGUA_EN_TINA',
            'PRESION_BAJA_PSIG',
            'CORRIENTE',
            'VOLTAJE',
            'CONTOMETRO_1',
            'CONTOMETRO_2',
            'MOTIVO_DE_PARADA',
            'HORAS_DE_PARADA'
        ]



""""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        rcks_value = self.instance.RCKS if self.instance and self.instance.pk else self.data.get('RCKS')

        self.fields['PRESION_BAJA_PSIG'].widget = forms.HiddenInput()
        self.fields['CORRIENTE'].widget = forms.HiddenInput()
        self.fields['VOLTAJE'].widget = forms.HiddenInput()

        if rcks_value in dict(self.RCKS_CHOICES).keys():
            self.fields['PRESION_BAJA_PSIG'].widget = forms.NumberInput(attrs={**self.COMMON_STYLE, 'step': '0.01'})
            self.fields['CORRIENTE'].widget = forms.NumberInput(attrs=self.COMMON_STYLE)
            self.fields['VOLTAJE'].widget = forms.NumberInput(attrs=self.COMMON_STYLE)

        self.fields['RCKS'].label = 'RCKS'
        self.fields['ESTADO_DEL_CONDENSADOR'].label = 'Estado del Condensador'
        self.fields['NIVEL_DE_REFRIGERANTE'].label = 'Nivel de Refrigerante'
        self.fields['PRESION_ALTA_PSIG'].label = 'Presión Alta (PSIG)'
        self.fields['PRESION_BAJA_PSIG'].label = 'Presión Baja (PSIG)'
        self.fields['CORRIENTE'].label = 'Corriente'
        self.fields['VOLTAJE'].label = 'Voltaje'

class MiFormulario(forms.Form):
    TIPO_DE_GAS_CHOICES = [
        ('', 'Seleccione un gas'),
        ('NH3', 'NH3'),
        ('Otro', 'Otro')
    ]
    
    tipo_de_gas = forms.ChoiceField(choices=TIPO_DE_GAS_CHOICES, label="Tipo de Gas")
    
    # Campos adicionales
    RCKS = forms.CharField(label='RCKS', required=False)
    ESTADO_DEL_CONDENSADOR = forms.CharField(label='Estado del Condensador', required=False)
    NIVEL_DE_REFRIGERANTE = forms.CharField(label='Nivel de Refrigerante', required=False)
    PRESION_ALTA_PSIG = forms.CharField(label='Presión Alta (PSIG)', required=False)
    PRESION_BAJA_PSIG = forms.CharField(label='Presión Baja (PSIG)', required=False)
    CORRIENTE = forms.CharField(label='Corriente', required=False)
    VOLTAJE = forms.CharField(label='Voltaje', required=False)

    def __init__(self, *args, **kwargs):
        super(MiFormulario, self).__init__(*args, **kwargs)
        
        # Aquí añadimos los atributos id para poder manipularlos con JS
        self.fields['RCKS'].widget.attrs.update({'id': 'id_RCKS'})
        self.fields['ESTADO_DEL_CONDENSADOR'].widget.attrs.update({'id': 'id_ESTADO_DEL_CONDENSADOR'})
        self.fields['NIVEL_DE_REFRIGERANTE'].widget.attrs.update({'id': 'id_NIVEL_DE_REFRIGERANTE'})
        self.fields['PRESION_ALTA_PSIG'].widget.attrs.update({'id': 'id_PRESION_ALTA_PSIG'})
        self.fields['PRESION_BAJA_PSIG'].widget.attrs.update({'id': 'id_PRESION_BAJA_PSIG'})
        self.fields['CORRIENTE'].widget.attrs.update({'id': 'id_CORRIENTE'})
        self.fields['VOLTAJE'].widget.attrs.update({'id': 'id_VOLTAGE'})

        
        
def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        
        # Si el formulario es una edición (ya tiene un registro con un RACKS determinado)
        if self.instance and self.instance.RACKS == 'SISTEMA NH3':
            # Si el rack es 'SISTEMA NH3', habilitamos todos los campos
            self.fields['PRESION_DE_BAJA_COMP_1'].widget.attrs.pop['disabled', None]
            self.fields['PRESION_DE_BAJA_COMP_2'].widget.attrs['disabled'] = False
            self.fields['CORRIENTE'].widget.attrs['disabled'] = False
            self.fields['VOLTAJE'].widget.attrs['disabled'] = False
        else:
            # Si el rack no es 'SISTEMA NH3', deshabilitamos estos campos
            self.fields['PRESION_DE_BAJA_COMP_1'].widget.attrs['disabled'] = 'disabled'
            self.fields['PRESION_DE_BAJA_COMP_2'].widget.attrs['disabled'] = 'disabled'
            self.fields['CORRIENTE'].widget.attrs['disabled'] = 'disabled'
            self.fields['VOLTAJE'].widget.attrs['disabled'] = 'disabled'        
        """