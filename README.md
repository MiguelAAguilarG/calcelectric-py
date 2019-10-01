# calcelectric-py
Ultima versión y se espera general para cálculos eléctricos

## Cómo hacer un cálculo

- Para hacer un cálculo primero debes de leer datos.datos_entrada_descripcion_dict pra comprender los datos que se introducen para hacer un cálculo
```
datos.py
```
- Después ir a calcelectric-py.py y leer los comentarios de como se realiza un cálculo y correr calcelectric-py.py
```
calcelectric-py.py
```
```
#Se crea un objeto Carga que se encuentra en el módulo elementos.py
#Por el momento no hay verificación de los datos introducidos en la Carga

#Carga = elementos.Carga(datos.datos_entrada_dict, datos.datos_por_defecto_Calculos_dict)
Carga = elementos.Carga(datos.datos_entrada_dict)

#Se procede a hacer el cálculo que se desea hacer para la carga, un cálculo completo es calculo_basico, por el momento, solo hay ese cálculo completo, este esta compuesto por cálculos que se encuentran en el módulo calculos.py. calculo_basico es un método en la Clase Carga
datos_por_defecto_Calculos_dict, datos_entrada, datos_salida_dict = Carga.calculo_basico()
```
- Por último ir a datos.datos_salida_descripcion_dict para comprender la salida que te dio calcelectric-py.py
```
datos.py
```

## Ejemplos
### Ejemplo 1
Un circuito derivado originado de una fuente monofásica con voltaje de fase a neutro de 127 V tiene una carga de 1000 W con un factor de potencia de 0.9. Se desea hacer un cálculo simple con base en la NOM-001-SEDE/NEC. A la carga, interruptor o cable no se le aplicarán factores de correción, salvo los que pide la NOM-001-SEDE/NEC (ya vienen por defecto programados). La temperatura ambiente es de 30 °C. El circuito tendra una caída de tensión maxima de 3%, la longitud del circuito es de 50 m.  Se usará un conductor de cobre con aislante THHW, la temperatura de dicho aislante es de 75°C (de hecho debería de ser de 90°C, solo que algunos fabricantes ponen excepciones lo cual da por resultado que realmente sea de 75°C), la temperatura en terminales de la carga eléctrica es de 60 °C (véase NOM-001-SEDE. 110-14(c)(1)). Se usará un conductor desnudo de tierra física. Todos los conductores del circuito estarán en un tubo conduit EMT.

#### Entrada de datos. Ejemplo 1
```
datos_entrada_dict = {
'Sistema': 'monofasico',
'lineas': 1,
'Voltaje': 127,
'Carga': 1000,
'fp': 0.9,
'factor_utilizacion_carga': 1,
'factor_simultaneidad_carga': 1,
'Interruptor_forzado': 0,
'factor_Inominal_Interruptor': 1,
'tipo_circuito': 'derivado',
'caida_tension': 3,
'Longitud': 50,
'Tambiente': 30,
'aislante_conductor': 'THHW',
'Taislante': 75,
'Tterminales': 60,
'material_conductor': 'cobre',
'numero_conductores_por_fase': 1,
'numero_conductores_neutro': 1,
'factor_Inominal_fase_aplicado_neutro': 1,
'neutro_activo_factor_agrupamiento': True,
'tierra_fisica_forrada': False,
'adicionar_tierra_fisica_aislada': False, 
'canalizacion': 'conduit',
'tipo_conduit': 'EMT',
'conduit_pulg_forzado': False,
'material_canalizacion': 'acero',
'misma_canalizacion': True,
'conductores_activos_adicionales_misma_canalizacion': {},
'conductores_no_activos_adicionales_misma_canalizacion': {},
}
```

#### Salida de datos. Ejemplo 1
```
{'factor_ampacidad_cable_fase': 1.25,
 'factor_ampacidad_cable_neutro': 1.25,
 'factor_error_Interruptor': 0.01,
 'factor_utilizacion_interruptor': 0.8}

{'Carga': 1000,
 'Interruptor_forzado': 0,
 'Longitud': 50,
 'Sistema': 'monofasico',
 'Taislante': 75,
 'Tambiente': 30,
 'Tterminales': 60,
 'Voltaje': 127,
 'adicionar_tierra_fisica_aislada': False,
 'aislante_conductor': 'THHW',
 'caida_tension': 3,
 'canalizacion': 'conduit',
 'conductores_activos_adicionales_misma_canalizacion': {},
 'conductores_no_activos_adicionales_misma_canalizacion': {},
 'conduit_pulg_forzado': False,
 'factor_Inominal_Interruptor': 1,
 'factor_Inominal_fase_aplicado_neutro': 1,
 'factor_simultaneidad_carga': 1,
 'factor_utilizacion_carga': 1,
 'fp': 0.9,
 'lineas': 1,
 'material_canalizacion': 'acero',
 'material_conductor': 'cobre',
 'misma_canalizacion': True,
 'neutro_activo_factor_agrupamiento': True,
 'numero_conductores_neutro': 1,
 'numero_conductores_por_fase': 1,
 'tierra_fisica_forrada': False,
 'tipo_circuito': 'derivado',
 'tipo_conduit': 'EMT'}

{'Ampacidad_corregida_fase': 20.0,
 'Ampacidad_corregida_neutro': 20.0,
 'Ampacidad_fase': 20,
 'Ampacidad_neutro': 20,
 'Area_ampacidad_fase': 2.08,
 'Area_ampacidad_neutro': 2.08,
 'Area_cable_fase': 5.26,
 'Area_cable_neutro': 5.26,
 'Area_caida_fase': 5.26,
 'Area_conductores': 36.64592432605615,
 'Area_conduit': 196.066797510539,
 'Area_tierra_fisica': 2.08,
 'Area_tierra_fisica_aislada': False,
 'Area_tierra_fisica_corregida_caida': 5.26,
 'Area_tierra_fisica_corregida_caida_ideal': 5.26,
 'Area_tierra_fisica_final': 5.26,
 'Carga_corregida_factor_simultaneidad_carga': 1000,
 'Carga_corregida_factor_utilizacion_carga': 1000,
 'Icorregida_factor_ampacidad_cable_fase': 10.936132983377078,
 'Icorregida_factor_ampacidad_cable_neutro': 10.936132983377078,
 'Inominal_fase': 8.748906386701663,
 'Inominal_neutro': 8.748906386701663,
 'Interruptor': 15,
 'caida_tension_calculada': 2.4801628592606084,
 'calibre_ampacidad_fase': '14',
 'calibre_ampacidad_neutro': '14',
 'calibre_cable_fase': '10',
 'calibre_cable_neutro': '10',
 'calibre_caida_fase': '10',
 'calibre_tierra_fisica': '14',
 'calibre_tierra_fisica_aislada': False,
 'calibre_tierra_fisica_corregida_caida': '10',
 'calibre_tierra_fisica_final': '10',
 'conductores_activos_canalizacion': 2,
 'conductores_canalizacion': {'desnudos': {'10': 1}, 'forrados': {'10': 2}},
 'conductores_circuito': {'L1': {'10': 1},
                          'L2': {False: 0},
                          'L3': {False: 0},
                          'N': {'10': 1},
                          'TA': {False: 0},
                          'TF': {'10': 1}},
 'factor_Inominal_fase_aplicado_neutro': 1,
 'factor_agrupamiento': 1,
 'factor_correccion_cable_tierra_fisica': 2.5288461538461537,
 'factor_temperatura': 1.0,
 'medida_conduit_in': '1/2',
 'medida_conduit_mm': 16,
 'numero_conductores_neutro': 1,
 'numero_conductores_por_fase': 1,
 'porcentaje_llenado_conduit': 18.690530365849604,
 'porcentaje_utilizacion_Interruptor': 58.326042578011084}
 ```
