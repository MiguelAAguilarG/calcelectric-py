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
Un circuito derivado originado de una fuente monofásica con un voltaje de fase a neutro de 127 V tiene una carga de 1000 W con un factor de potencia de 0.9. Se desea hacer un cálculo simple con base en la NOM-001-SEDE/NEC. A la carga, interruptor y cable no se le aplicarán factores de corrección, salvo los que pide la NOM-001-SEDE/NEC (ya vienen por defecto programados). La temperatura ambiente es de 30 °C. El circuito tendrá una caída de tensión máxima de 3%, la longitud del circuito es de 50 m.  Se usará un conductor de cobre con aislante THHW, la temperatura de dicho aislante es de 75°C (de hecho debería de ser de 90°C, solo que algunos fabricantes ponen excepciones lo cual da por resultado que realmente sea de 75°C), la temperatura en terminales de la carga eléctrica es de 60 °C (véase NOM-001-SEDE. 110-14(c)(1)). Se usará un conductor desnudo de tierra física. Todos los conductores del circuito estarán en un tubo conduit EMT.

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
{'factor_utilizacion_interruptor': 0.8,
 'factor_ampacidad_cable_fase': 1.25,
 'factor_ampacidad_cable_neutro': 1.25,
 'factor_error_Interruptor': 0.01}

{'Sistema': 'monofasico',
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
 'conductores_no_activos_adicionales_misma_canalizacion': {}}

{'Carga': 1000,
 'Inominal_fase': 8.748906386701663,
 'Inominal_neutro': 8.748906386701663,
 'Icorregida_factor_ampacidad_cable_fase': 10.936132983377078,
 'Icorregida_factor_ampacidad_cable_neutro': 10.936132983377078,
 'Carga_corregida_factor_utilizacion_carga': 1000,
 'Carga_corregida_factor_simultaneidad_carga': 1000,
 'numero_conductores_por_fase': 1,
 'numero_conductores_neutro': 1,
 'factor_Inominal_fase_aplicado_neutro': 1,
 'conductores_activos_canalizacion': 2,
 'Interruptor': 15,
 'porcentaje_utilizacion_Interruptor': 58.326042578011084,
 'factor_temperatura': 1.0,
 'factor_agrupamiento': 1,
 'calibre_ampacidad_fase': '14',
 'Area_ampacidad_fase': 2.08,
 'Ampacidad_fase': 20,
 'Ampacidad_corregida_fase': 20.0,
 'calibre_caida_fase': '10',
 'Area_caida_fase': 5.26,
 'caida_tension_calculada': 2.4801628592606084,
 'calibre_cable_fase': '10',
 'Area_cable_fase': 5.26,
 'calibre_tierra_fisica': '14',
 'Area_tierra_fisica': 2.08,
 'factor_correccion_cable_tierra_fisica': 2.5288461538461537,
 'Area_tierra_fisica_corregida_caida_ideal': 5.26,
 'calibre_tierra_fisica_corregida_caida': '10',
 'Area_tierra_fisica_corregida_caida': 5.26,
 'calibre_tierra_fisica_final': '10',
 'Area_tierra_fisica_final': 5.26,
 'calibre_tierra_fisica_aislada': False,
 'Area_tierra_fisica_aislada': False,
 'calibre_ampacidad_neutro': '14',
 'Area_ampacidad_neutro': 2.08,
 'Ampacidad_neutro': 20,
 'Ampacidad_corregida_neutro': 20.0,
 'calibre_cable_neutro': '10',
 'Area_cable_neutro': 5.26,
 'conductores_circuito': {'L1': {'10': 1},
                          'L2': {False: 0},
                          'L3': {False: 0},
                          'N': {'10': 1},
                          'TF': {'10': 1},
                          'TA': {False: 0}},
 'conductores_canalizacion': {'forrados': {'10': 2}, 'desnudos': {'10': 1}},
 'Area_conductores': 36.64592432605615,
 'porcentaje_llenado_conduit': 18.690530365849604,
 'medida_conduit_in': '1/2',
 'medida_conduit_mm': 16,
 'Area_conduit': 196.066797510539}
 ```

### Ejemplo 2
Un alimentador debe alimentar un tablero eléctrico que alimenta cargas no lineales con una carga total de 10,000 W con un factor de potencia de 0.9 y que tienen un alto contenido de corrientes armónicas, debido a esto, el neutro se debe dimensionar a 1.73 veces la corriente balanceada de fase. El tablero requiere de 3 fases y neutro a 220/127 V, tierra aislada y tierra desnuda. La carga total del tablero esta compuesta de cargas que siempre trabajan a su máxima capacidad, por lo tanto, las cargas conectadas al tablero y la carga total en el tablero tienen un factor de utilización del 100%, sin embargo, estas cargas no siempre trabajan todas al mismo tiempo, por ello, se determino que la carga total del tablero tiene un factor de simultaneidad del 70%. Se desea hacer un cálculo simple con base en la NOM-001-SEDE/NEC. Al interruptor y cable no se le aplicarán factores de corrección, salvo los que pide la NOM-001-SEDE/NEC (ya vienen por defecto programados). La temperatura ambiente es de 40 °C. El circuito tendrá una caída de tensión máxima del 2%, la longitud del alimentador es de 40 m.  Se usarán conductores de cobre con aislante THHW, la temperatura de dicho aislante es de 90°C, la temperatura en terminales de todos los elementos conectados a los conductores del alimentador es de 75 °C (véase NOM-001-SEDE. 110-14(c)(1)). Todos los conductores del circuito estarán en un tubo conduit EMT.

#### Entrada de datos. Ejemplo 2
```
datos_entrada_dict = {
'Sistema': 'trifasico',
'lineas': 3,
'Voltaje': 220,
'Carga': 10000,
'fp': 0.9,
'factor_utilizacion_carga': 1,
'factor_simultaneidad_carga': 0.7,
'Interruptor_forzado': 0,
'factor_Inominal_Interruptor': 1,
'tipo_circuito': 'alimentador',
'caida_tension': 2,
'Longitud': 40,
'Tambiente': 40,
'aislante_conductor': 'THHW',
'Taislante': 90,
'Tterminales': 75,
'material_conductor': 'cobre',
'numero_conductores_por_fase': 1,
'numero_conductores_neutro': 1,
'factor_Inominal_fase_aplicado_neutro': 1.73,
'neutro_activo_factor_agrupamiento': True,
'tierra_fisica_forrada': False,
'adicionar_tierra_fisica_aislada': True, 
'canalizacion': 'conduit',
'tipo_conduit': 'EMT',
'conduit_pulg_forzado': False,
'material_canalizacion': 'acero',
'misma_canalizacion': True,
'conductores_activos_adicionales_misma_canalizacion': {},
'conductores_no_activos_adicionales_misma_canalizacion': {},
}
```

#### Salida de datos. Ejemplo 2
```
Para tipo_circuito = alimentador, el factor_ampacidad_cable_neutro para cargas continuas puede ser de 1.
Si desea hacer el cambio hagalo manualmente en datos.datos_por_defecto_Calculos_dict = {'factor_ampacidad_cable_neutro': 1}.

{'factor_utilizacion_interruptor': 0.8,
 'factor_ampacidad_cable_fase': 1.25,
 'factor_ampacidad_cable_neutro': 1.25,
 'factor_error_Interruptor': 0.01}

{'Sistema': 'trifasico',
 'lineas': 3,
 'Voltaje': 220,
 'Carga': 10000,
 'fp': 0.9,
 'factor_utilizacion_carga': 1,
 'factor_simultaneidad_carga': 0.7,
 'Interruptor_forzado': 0,
 'factor_Inominal_Interruptor': 1,
 'tipo_circuito': 'alimentador',
 'caida_tension': 2,
 'Longitud': 40,
 'Tambiente': 40,
 'aislante_conductor': 'THHW',
 'Taislante': 90,
 'Tterminales': 75,
 'material_conductor': 'cobre',
 'numero_conductores_por_fase': 1,
 'numero_conductores_neutro': 1,
 'factor_Inominal_fase_aplicado_neutro': 1.73,
 'neutro_activo_factor_agrupamiento': True,
 'tierra_fisica_forrada': False,
 'adicionar_tierra_fisica_aislada': True,
 'canalizacion': 'conduit',
 'tipo_conduit': 'EMT',
 'conduit_pulg_forzado': False,
 'material_canalizacion': 'acero',
 'misma_canalizacion': True,
 'conductores_activos_adicionales_misma_canalizacion': {},
 'conductores_no_activos_adicionales_misma_canalizacion': {}}

{'Carga': 7000.0,
 'Inominal_fase': 20.411373153168586,
 'Inominal_neutro': 35.311675554981655,
 'Icorregida_factor_ampacidad_cable_fase': 25.514216441460732,
 'Icorregida_factor_ampacidad_cable_neutro': 44.13959444372707,
 'Carga_corregida_factor_utilizacion_carga': 10000,
 'Carga_corregida_factor_simultaneidad_carga': 7000.0,
 'numero_conductores_por_fase': 1,
 'numero_conductores_neutro': 1,
 'factor_Inominal_fase_aplicado_neutro': 1.73,
 'conductores_activos_canalizacion': 4,
 'Interruptor': 30,
 'porcentaje_utilizacion_Interruptor': 68.03791051056196,
 'factor_temperatura': 0.9128709291752769,
 'factor_agrupamiento': 0.8,
 'calibre_ampacidad_fase': '10',
 'Area_ampacidad_fase': 5.26,
 'Ampacidad_fase': 40,
 'Ampacidad_corregida_fase': 29.21186973360886,
 'calibre_caida_fase': '8',
 'Area_caida_fase': 8.37,
 'caida_tension_calculada': 1.5406714263068788,
 'calibre_cable_fase': '8',
 'Area_cable_fase': 8.37,
 'calibre_tierra_fisica': '10',
 'Area_tierra_fisica': 5.26,
 'factor_correccion_cable_tierra_fisica': 1.591254752851711,
 'Area_tierra_fisica_corregida_caida_ideal': 8.37,
 'calibre_tierra_fisica_corregida_caida': '8',
 'Area_tierra_fisica_corregida_caida': 8.37,
 'calibre_tierra_fisica_final': '8',
 'Area_tierra_fisica_final': 8.37,
 'calibre_tierra_fisica_aislada': '8',
 'Area_tierra_fisica_aislada': 8.37,
 'calibre_ampacidad_neutro': '6',
 'Area_ampacidad_neutro': 13.3,
 'Ampacidad_neutro': 75,
 'Ampacidad_corregida_neutro': 54.772255750516614,
 'calibre_cable_neutro': '6',
 'Area_cable_neutro': 13.3,
 'conductores_circuito': {'L1': {'8': 1},
                          'L2': {'8': 1},
                          'L3': {'8': 1},
                          'N': {'6': 1},
                          'TF': {'8': 1},
                          'TA': {'8': 1}},
 'conductores_canalizacion': {'forrados': {'8': 4, '6': 1},
                              'desnudos': {'8': 1}},
 'Area_conductores': 168.0739840938145,
 'porcentaje_llenado_conduit': 30.24456484106413,
 'medida_conduit_in': '1',
 'medida_conduit_mm': 27,
 'Area_conduit': 555.7163244934985}
 ```
 
### Ejemplo 3
Se desea calcular los conductores y la protección por corto circuito de un circuito derivado para alimentar a un motor trifásico de jaula de ardilla de 200 hp a 230 V. Se desea hacer un cálculo simple con base en la NOM-001-SEDE/NEC. Al cable no se le aplicarán factores de corrección, salvo los que pide la NOM-001-SEDE/NEC (ya vienen por defecto programados). La temperatura ambiente es de 40 °C. El circuito tendrá una caída de tensión máxima del 3%, la longitud del circuito derivado es de 50 m.  Se usarán conductores de cobre con aislante THHN, la temperatura de dicho aislante es de 90°C, la temperatura en terminales de todos los elementos conectados a los conductores del circuito derivado del motor es de 75 °C (véase NOM-001-SEDE. 110-14(c)(1)). Todos los conductores del circuito estarán en un tubo conduit HDPE de 3 pulgadas. La corriente del motor para el cálculo de conductores, desconectadores y protección por corto circuito y falla a tierra lo tomo de la tabla 430-250 (FLC) y no de la placa del motor (FLA) que se usa para la protección por sobrecarga. La corriente que da la tabla para el motor es de 480 A. Debido a la alta corriente se eligió poner 2 conductores por fase en dos canalizaciones, cada una con fase A, B y C con tierra física desnuda. El interruptor para protección por corto circuito se dimensiono al 250% como lo permite la Tabla 430-52. Se supuso un factor de potencia de 0.9.

#### Entrada de datos. Ejemplo 3
```
datos_entrada_dict = {
'Sistema': 'trifasico',
'lineas': 3,
'Voltaje': 230,
'Carga': 480*sqrt(3)*230*0.9,
'fp': 0.9,
'factor_utilizacion_carga': 1,
'factor_simultaneidad_carga': 1,
'Interruptor_forzado': 0,
'factor_Inominal_Interruptor': 2.5,
'tipo_circuito': 'derivado',
'caida_tension': 3,
'Longitud': 50,
'Tambiente': 40,
'aislante_conductor': 'THHN',
'Taislante': 90,
'Tterminales': 75,
'material_conductor': 'cobre',
'numero_conductores_por_fase': 2,
'numero_conductores_neutro': 0,
'factor_Inominal_fase_aplicado_neutro': 0,
'neutro_activo_factor_agrupamiento': False,
'tierra_fisica_forrada': False,
'adicionar_tierra_fisica_aislada': False, 
'canalizacion': 'conduit',
'tipo_conduit': 'HDPE',
'conduit_pulg_forzado': '3',
'material_canalizacion': 'pvc',
'misma_canalizacion': False,
'conductores_activos_adicionales_misma_canalizacion': {},
'conductores_no_activos_adicionales_misma_canalizacion': {},
}
```

#### Salida de datos. Ejemplo 3
```
fase
Se tomo como Ampacidad_corregida la Ampacidad de Tterminales, ya que la Ampacidad_corregida de Taislante > Ampacidad de Tterminales. 110-14(c)(1)

{'factor_utilizacion_interruptor': 0.8,
 'factor_ampacidad_cable_fase': 1.25,
 'factor_ampacidad_cable_neutro': 1.25,
 'factor_error_Interruptor': 0.01}

{'Sistema': 'trifasico',
 'lineas': 3,
 'Voltaje': 230,
 'Carga': 172096.56824004362,
 'fp': 0.9,
 'factor_utilizacion_carga': 1,
 'factor_simultaneidad_carga': 1,
 'Interruptor_forzado': 0,
 'factor_Inominal_Interruptor': 2.5,
 'tipo_circuito': 'derivado',
 'caida_tension': 3,
 'Longitud': 50,
 'Tambiente': 40,
 'aislante_conductor': 'THHN',
 'Taislante': 90,
 'Tterminales': 75,
 'material_conductor': 'cobre',
 'numero_conductores_por_fase': 2,
 'numero_conductores_neutro': 0,
 'factor_Inominal_fase_aplicado_neutro': 0,
 'neutro_activo_factor_agrupamiento': False,
 'tierra_fisica_forrada': False,
 'adicionar_tierra_fisica_aislada': False,
 'canalizacion': 'conduit',
 'tipo_conduit': 'HDPE',
 'conduit_pulg_forzado': '3',
 'material_canalizacion': 'pvc',
 'misma_canalizacion': False,
 'conductores_activos_adicionales_misma_canalizacion': {},
 'conductores_no_activos_adicionales_misma_canalizacion': {}}

{'Carga': 172096.56824004362,
 'Inominal_fase': 479.9999999999999,
 'Inominal_neutro': 0.0,
 'Icorregida_factor_ampacidad_cable_fase': 599.9999999999999,
 'Icorregida_factor_ampacidad_cable_neutro': 0.0,
 'Carga_corregida_factor_utilizacion_carga': 172096.56824004362,
 'Carga_corregida_factor_simultaneidad_carga': 172096.56824004362,
 'numero_conductores_por_fase': 2,
 'numero_conductores_neutro': 0,
 'factor_Inominal_fase_aplicado_neutro': 0,
 'conductores_activos_canalizacion': 3,
 'Interruptor': 1200,
 'porcentaje_utilizacion_Interruptor': 39.999999999999986,
 'factor_temperatura': 0.9128709291752769,
 'factor_agrupamiento': 1,
 'calibre_ampacidad_fase': '350',
 'Area_ampacidad_fase': 177,
 'Ampacidad_fase': 350,
 'Ampacidad_corregida_fase': 310,
 'calibre_caida_fase': '3/0',
 'Area_caida_fase': 85.01,
 'caida_tension_calculada': 2.6012644387313197,
 'calibre_cable_fase': '350',
 'Area_cable_fase': 177,
 'calibre_tierra_fisica': '3/0',
 'Area_tierra_fisica': 85.01,
 'factor_correccion_cable_tierra_fisica': 0.48028248587570627,
 'Area_tierra_fisica_corregida_caida_ideal': 40.82881412429379,
 'calibre_tierra_fisica_corregida_caida': '1',
 'Area_tierra_fisica_corregida_caida': 42.4,
 'calibre_tierra_fisica_final': '3/0',
 'Area_tierra_fisica_final': 85.01,
 'calibre_tierra_fisica_aislada': False,
 'Area_tierra_fisica_aislada': False,
 'calibre_ampacidad_neutro': False,
 'Area_ampacidad_neutro': False,
 'Ampacidad_neutro': False,
 'Ampacidad_corregida_neutro': False,
 'calibre_cable_neutro': False,
 'Area_cable_neutro': False,
 'conductores_circuito': {'L1': {'350': 2},
                          'L2': {'350': 2},
                          'L3': {'350': 2},
                          'N': {False: 0},
                          'TF': {'3/0': 2},
                          'TA': {False: 0}},
 'conductores_canalizacion': {'forrados': {False: 0, '350': 3},
                              'desnudos': {'3/0': 1}},
 'Area_conductores': 1099.4989901834415,
 'porcentaje_llenado_conduit': 23.428579929977225,
 'medida_conduit_in': '3',
 'medida_conduit_mm': 78,
 'Area_conduit': 4692.981791767139}
 ```
