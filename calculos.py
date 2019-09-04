from math import *

def reconocedor_conexiones(datos):
	'''funciona con el diccionario de datos'''
	conecciones_dict = {}

	for identificador, value in datos.items():
		if isinstance(datos[identificador]['coneccion'], list) or isinstance(datos[identificador]['coneccion'], tuple):
			for coneccion in datos[identificador]['coneccion']:
				if not coneccion in conecciones_dict.keys():
					#conecciones_dict = {'coneccion_1':[], 'coneccion_2': [], ...}
					conecciones_dict[coneccion] = []

				conecciones_dict[coneccion].append(identificador)

	return conecciones_dict

def pasador_datos_conecciones():
	pass

def calculador_corriente(*datos):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	Sistema = datos_totales['Sistema']
	Voltaje = datos_totales['Voltaje']
	Carga = datos_totales['Carga']
	fp = datos_totales['fp']
	factor_carga = datos_totales['factor_carga']

	if Sistema == 'monofásico':
		I_nom = Carga/(Voltaje*fp)
		I_calculada = I_nom*factor_carga

	if Sistema == 'trifásico':
		I_nom = Carga/(sqrt(3)*Voltaje*fp)
		I_calculada = I_nom*factor_carga

	Carga_corregida = Carga*factor_carga

	return {'I_nom': I_nom, 'I_calculada': I_calculada, 'Carga_corregida': Carga_corregida}

def calculador_conductores_canalizacion(*datos):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	Sistema = datos_totales['Sistema']
	numero_conductores_por_fase = datos_totales['numero_conductores_por_fase']
	mismo = datos_totales['mismo']
	neutro = datos_totales['neutro']

	if neutro == 'si':
		neutro = 1
	if neutro == 'no':
		neutro = 0

	if Sistema == 'monofásico':
		neutro = 1

		if mismo == 'si':
			conductores_canalizacion = numero_conductores_por_fase*mismo + neutro*numero_conductores_por_fase*mismo
		if mismo == 'no':
			conductores_canalizacion = 1 + neutro

	if Sistema == 'trifásico':
		if mismo == 'si':
			conductores_canalizacion = 3*numero_conductores_por_fase*mismo + neutro*numero_conductores_por_fase*mismo
		if mismo == 'no':
			conductores_canalizacion = 3 + neutro

	return {'conductores_canalizacion': conductores_canalizacion}

def calculador_interruptor(*datos, Interruptores):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	I_calculada = datos_totales['I_calculada']
	I_nom = datos_totales['I_nom']
	Interruptor_forzado_1 = datos_totales['Interruptor_forzado_1']
	porcentaje_Irating_1 = datos_totales['porcentaje_Irating_1']
	Interruptor_forzado_2 = datos_totales['Interruptor_forzado_2']
	porcentaje_Irating_2 = datos_totales['porcentaje_Irating_2']
	mismo_amperaje = datos_totales['mismo_amperaje']
	factor_carga = datos_totales['factor_carga']
	ajuste_factor_carga = datos_totales['ajuste_factor_carga']
	#Interruptores

	if Interruptor_forzado_1 == True:
		for x in range(len(Interruptores)):
			if I_calculada <= Interruptores[x]:
				Interruptor_1 = Interruptores[x]
				porcentaje_Irating_1 = I_calculada*100/Interruptor_1
				if porcentaje_Irating_1 <= 80:
					if Interruptores[x-1]*0.8 >= Inom  and (x-1) >= 0:
						Interruptor_1 = Interruptores[x-1]
						porcentaje_Irating_1 = I_nom*100/Interruptor_1
				break
		else:
			print('!ERROR!. No se encontro interruptor 1 tan grande. Aumenta el nivel de voltaje para esa carga')
	elif Interruptor_forzado_1 > 0:
		if I_calculada <= Interruptor_forzado_1:
			Interruptor_1 = Interruptor_forzado_1
			if I_calculada <= Interruptor_forzado_1*porcentaje_Irating_1:
				porcentaje_Irating_1 = porcentaje_Irating_1
			else:
				porcentaje_Irating_1 = I_calculada*100/Interruptor_forzado_1
		else:
			print('!ERROR!. Amperaje del Interruptor 1 forzado menor a la I calculada. Se procedio a calcular otro interruptor 1 y otro porcentaje Irating 1')
			for x in range(len(Interruptores)):
				if I_calculada <= Interruptores[x]:
					Interruptor_1 = Interruptores[x]
					porcentaje_Irating_1 = I_calculada*100/Interruptor_1
					if porcentaje_Irating_1 <= 80:
						if Interruptores[x-1]*0.8 >= Inom  and (x-1) >= 0:
							Interruptor_1 = Interruptores[x-1]
							porcentaje_Irating_1 = I_nom*100/Interruptor_1
					break
			else:
				print('!ERROR!. No se encontro interruptor 1 tan grande. Aumenta el nivel de voltaje para esa carga')
	elif Interruptor_forzado_1 == False:
		for x in Interruptores:
			if I_calculada <= x:
				Interruptor_1 = x
				porcentaje_Irating_1 = I_calculada*100/Interruptor_1
				break
			if I_nom*(factor_carga-ajuste_factor_carga/100) <= x:
				Interruptor_1 = x
				porcentaje_Irating_1 = I_calculada*100/Interruptor_1
				break
		else:
			print('No se encontro interruptor 1 tan grande. Aumenta el nivel de voltaje para esa carga')
	else:
		print('No corresponde a ninguna opción para interruptor 1')

	if mismo_amperaje == True:
		Interruptor_2 = Interruptor_1
		porcentaje_Irating_2 = porcentaje_Irating_1
	else:
		if Interruptor_forzado_2 == True:
			for x in range(len(Interruptores)):
				if I_calculada <= Interruptores[x]:
					Interruptor_2 = Interruptores[x]
					porcentaje_Irating_2 = I_calculada*100/Interruptor_2
					if porcentaje_Irating_2 <= 80:
						if Interruptores[x-1]*0.8 >= Inom  and (x-1) >= 0:
							Interruptor_2 = Interruptores[x-1]
							porcentaje_Irating_2 = I_nom*100/Interruptor_2
					break
			else:
				print('!ERROR!. No se encontro interruptor 2 tan grande. Aumenta el nivel de voltaje para esa carga')
		elif Interruptor_forzado_2 > 0:
			if I_calculada <= Interruptor_forzado_2:
				Interruptor_2 = Interruptor_forzado_2
				if I_calculada <= Interruptor_forzado_2*porcentaje_Irating_2:
					porcentaje_Irating_2 = porcentaje_Irating_2
				else:
					porcentaje_Irating_2 = I_calculada*100/Interruptor_forzado_2
			else:
				print('!ERROR!. Amperaje del Interruptor 2 forzado menor a la I calculada. Se procedio a calcular otro interruptor 2 y otro porcentaje Irating 2')
				for x in range(len(Interruptores)):
					if I_calculada <= Interruptores[x]:
						Interruptor_2 = Interruptores[x]
						porcentaje_Irating_2 = I_calculada*100/Interruptor_2
						if porcentaje_Irating_2 <= 80:
							if Interruptores[x-1]*0.8 >= Inom  and (x-1) >= 0:
								Interruptor_2 = Interruptores[x-1]
								porcentaje_Irating_2 = I_nom*100/Interruptor_2
						break
				else:
					print('!ERROR!. No se encontro interruptor 2 tan grande. Aumenta el nivel de voltaje para esa carga')
		elif Interruptor_forzado_2 == False:
			for x in Interruptores:
				if I_calculada <= x:
					Interruptor_2 = x
					porcentaje_Irating_2 = I_calculada*100/Interruptor_2
					break
				if I_nom*(factor_carga-ajuste_factor_carga/100) <= x:
					Interruptor_2 = x
					porcentaje_Irating_2 = I_calculada*100/Interruptor_2
					break
			else:
				print('No se encontro interruptor 2 tan grande. Aumenta el nivel de voltaje para esa carga')
		else:
			print('No corresponde a ninguna opción para interruptor 2')

	return {'Interruptor_1': Interruptor_1, 'porcentaje_Irating_1_salida': porcentaje_Irating_1, 'Interruptor_2': Interruptor_2, 'porcentaje_Irating_2_salida': porcentaje_Irating_2}

def calculador_factor_temperatura(*datos, Tambiente_tablas):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	Tconductor = datos_totales['Tconductor']
	Tambiente = datos_totales['Tambiente']
	#Tambiente_tablas

	factor_temperatura = sqrt((Tconductor-Tambiente)/(Tconductor-Tambiente_tablas))

	return {'factor_temperatura': factor_temperatura}

def calculador_factor_agrupamiento(*datos, tabla_factor_agrupamiento):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	conductores_canalizacion = datos_totales['conductores_canalizacion']
	Longitud = datos_totales['Longitud']
	#tabla_factor_agrupamiento 

	if Longitud <= 0.6:#Factor de agrupamiento no aplica para 60 cm o menos. 310-15.(b)(3)(a)(2)
		factor_agrupamiento = 1
	else:
		for x,y in tabla_factor_agrupamiento.items(): #Determinar factor de agrupamiento NOTA: Ir a la Tabla 310-15(b)(3)(a)
			if conductores_canalizacion <= x:
				factor_agrupamiento = y
				break
		else:
			print('Demasiados conductores en la canalizacion')#modificar cuando se hagan clases
			factor_agrupamiento = 0

	return {'factor_agrupamiento': factor_agrupamiento}

def calculador_cable_ampacidad(*datos, tabla_de_Ampacidades, calibre_tabla, Area_conductor_tabla):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	Interruptor = datos_totales['Interruptor_1']
	Interruptor_forzado_1 = datos_totales['Interruptor_forzado_1']
	porcentaje_Irating_1_salida = datos_totales['porcentaje_Irating_1_salida']
	if Interruptor_forzado_1 == True or Interruptor_forzado_1 > 0:
		Interruptor = datos_totales['porcentaje_Irating_1_salida']*datos_totales['Interruptor_1']/100
	numero_conductores_por_fase = datos_totales['numero_conductores_por_fase']
	material_conductor = datos_totales['material_conductor']
	Tconductor = datos_totales['Tconductor']
	factor_agrupamiento = datos_totales['factor_agrupamiento']
	factor_temperatura = datos_totales['factor_temperatura']
	calibre = datos_totales.get('calibre')
	#tabla_de_Ampacidades
	#calibre_tabla
	#Area_conductor_tabla

	Ampacidad_tabla = tabla_de_Ampacidades[material_conductor][Tconductor]
	Ampacidad_corregida_tabla = [x*factor_agrupamiento*factor_temperatura for x in Ampacidad_tabla]

	if calibre in calibre_tabla:

		indice = calibre_tabla.index(calibre)
		Area = Area_conductor_tabla[indice]
		Ampacidad = Ampacidad_tabla[indice]
		Ampacidad_corregida = Ampacidad_corregida_tabla[indice]

		return {'indice_ampacidad': indice, 'calibre_ampacidad': calibre, 'Area_ampacidad': Area, 'Ampacidad': Ampacidad, 'Ampacidad_corregida': Ampacidad_corregida}

	while True:
		for indice, Ampacidad_corregida in enumerate(Ampacidad_corregida_tabla):
			if Ampacidad_corregida >= Interruptor/numero_conductores_por_fase:
				calibre = calibre_tabla[indice]
				Area = Area_conductor_tabla[indice]
				Ampacidad = Ampacidad_tabla[indice]

				if Area < 53 and numero_conductores_por_fase > 1:
					print('Ampacidad')
					print('!ERROR. Tamano de conductor menor a 1/0. No se puede poner ese tamaño de conductor en paralelo.')
					print(f'Conductor elegido por ampacidad menor a 1/0: {calibre}')
					print('')
				else:
					return {'indice_ampacidad': indice, 'calibre_ampacidad': calibre, 'Area_ampacidad': Area, 'Ampacidad': Ampacidad, 'Ampacidad_corregida': Ampacidad_corregida}
		else:
			print('Ampacidad')
			print('!ERROR. Tamano de conductor demasiado grande. Fuera de rango de las tablas.')
			print('Se recomienda aumentar numero de conductores por fase')
			print('')

			return

def calculador_cable_caida_de_tension(*datos, tabla_de_impedancias, calibre_tabla, Area_conductor_tabla):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	Sistema = datos_totales['Sistema']
	fp = datos_totales['fp']
	Longitud = datos_totales['Longitud']
	I_nom = datos_totales['I_nom']
	Voltaje = datos_totales['Voltaje']
	caida_tension = datos_totales['caida_tension']
	numero_conductores_por_fase = datos_totales['numero_conductores_por_fase']
	material_conductor = datos_totales['material_conductor']
	material_canalizacion = datos_totales['material_canalizacion']
	I_nom = datos_totales['I_nom']
	Voltaje = datos_totales['Voltaje']
	caida_tension = datos_totales['caida_tension']
	calibre = datos_totales.get('calibre')
	#tabla_de_impedancias
	#calibre_tabla
	#Area_conductor_tabla

	resistencia_tabla = tabla_de_impedancias['resistencia'][material_conductor][material_canalizacion]
	reactancia_tabla = tabla_de_impedancias['reactancia'][material_conductor][material_canalizacion]
	
	if calibre in calibre_tabla:

		indice = calibre_tabla.index(calibre)
		Area = Area_conductor_tabla[indice]

		if indice >= 20:
			print('caída de tensión')
			print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas (calibre introducido).')
			print('Se recomienda aumentar numero de conductores por fase')
			print('')

			return

		Ze = (resistencia_tabla[indice]*fp + reactancia_tabla[indice]*sin(acos(fp)))/1000*Longitud

		if Sistema == 'monofásico':
			caida_tension_calculada = 2*Ze*I_nom*100/Voltaje/numero_conductores_por_fase
		elif Sistema == 'trifásico':
			caida_tension_calculada = sqrt(3)*Ze*I_nom*100/Voltaje/numero_conductores_por_fase

		return {'indice_caida': indice, 'calibre_caida': calibre_tabla[indice], 'Area_caida': Area, 'Ze': Ze, 'caida_tension_calculada': caida_tension_calculada}

	while True:
		for indice, Area in enumerate(Area_conductor_tabla):
			
			if indice >= 20:
				print('caída de tensión')
				print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas.')
				print('Se recomienda aumentar numero de conductores por fase')
				print('2')

				return

			Ze = (resistencia_tabla[indice]*fp + reactancia_tabla[indice]*sin(acos(fp)))/1000

			if Sistema == 'monofásico':
				caida_tension_calculada = 2*Ze*Longitud*I_nom*100/Voltaje/numero_conductores_por_fase
			elif Sistema == 'trifásico':
				caida_tension_calculada = sqrt(3)*Ze*Longitud*I_nom*100/Voltaje/numero_conductores_por_fase
		
			if caida_tension_calculada <= caida_tension:

				if Area < 53 and numero_conductores_por_fase > 1:
					print('caída de tensión')
					print('!ERROR. Tamaño de conductor menor a 1/0. No se puede poner ese tamaño de conductor en paralelo.')
					print(f'Conductor elegido por ampacidad menor a 1/0: {calibre_tabla[indice]}')
					print('')
				else:
					return {'indice_caida': indice, 'calibre_caida': calibre_tabla[indice], 'Area_caida': Area, 'Ze': Ze, 'caida_tension_calculada': caida_tension_calculada}
		else:
			print('caída de tensión')
			print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas.')
			print('Se recomienda aumentar numero de conductores por fase')
			print('3')

#def seleccionador_cable(indices,factores):

def calculador_cable_tierra_fisica(*datos, interruptor_tierra_fisica_tabla, tierra_fisica_tabla, calibre_tabla, Area_tierra_tabla):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	Interruptor = datos_totales['Interruptor_1']
	Interruptor_forzado_1 = datos_totales['Interruptor_forzado_1']
	porcentaje_Irating_1_salida = datos_totales['porcentaje_Irating_1_salida']
	if Interruptor_forzado_1 == True or Interruptor_forzado_1 > 0:
		Interruptor = datos_totales['porcentaje_Irating_1_salida']*datos_totales['Interruptor_1']/100
	material_conductor_tierra = datos_totales['material_conductor']
	canalizacion = datos_totales['canalizacion']
	#interruptor_tierra_fisica_tabla
	#tierra_fisica_tabla
	#calibre_tabla
	#Area_tierra_tabla

	for x,y in enumerate(interruptor_tierra_fisica_tabla):
		if Interruptor <= y:
			calibre_tierra_fisica = tierra_fisica_tabla[material_conductor_tierra][x]
			Area_tierra_fisica = Area_tierra_tabla[calibre_tabla.index(calibre_tierra_fisica)]

			if Area_tierra_fisica < 21.2 and canalizacion == 'charola':
				print('Tierra física')
				print('Tamaño de conductor menor a 4. No se puede poner ese tamaño de conductor en una charola.')
				print(f'Conductor de tierra fisica elegido: {calibre_tierra_fisica}')
				print(f'Material de tierra fisica: {material_conductor_tierra}')
				print('')

				tierra = '4'
				Area_tierra_fisica = Area_tierra_tabla[calibre_tabla.index(calibre_tierra_fisica)]
		
			return {'calibre_tierra_fisica': calibre_tierra_fisica, 'Area_tierra_fisica': Area_tierra_fisica}
			
def calculador_tamano_conduit(*datos, designacion_tubo_conduit_tabla, dimensiones_tubo_conduit_tabla, dimensiones_cables_tabla):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	conductores_canalizacion = datos_totales['conductores_canalizacion']
	aislante_conductor = datos_totales['aislante_conductor']
	tipo_conduit = datos_totales['tipo_conduit']
	indice_conductor = datos_totales['indice']
	calibre_tierra_fisica = datos_totales['calibre_tierra_fisica']
	Area_tierra_fisica = datos_totales['Area_tierra_fisica']
	#designacion_tubo_conduit_tabla
	#dimensiones_tubo_conduit_tabla
	#dimensiones_cables_tabla
	porcentaje_ocupacion_forzado = 0

	lista_aislantes = []
	for indice1, key in enumerate(dimensiones_cables_tabla.keys()):
		lista_aislantes.append([])
		lista_aislantes[indice1] = key.split(',')
		for indice2, elemento in enumerate(lista_aislantes[indice1]):
			lista_aislantes[indice1][indice2] = elemento.strip()

		if aislante_conductor in lista_aislantes[indice1]:
			key_aislante_conductor = key

	Area_cable = (dimensiones_cables_tabla[key_aislante_conductor][indice_conductor]/2)**2*pi
	Area_total_conductores = conductores_canalizacion*Area_cable + Area_tierra_fisica

	tuberia_tabla = ['1/2', '3/4', '1', '1 1/4', '1 1/2', '2', '2 1/2', '3', '3 1/2', '4', '5', '6']
	for indice, x in enumerate(dimensiones_tubo_conduit_tabla[tipo_conduit]):
		Area_conduit = (x/2)**2*pi
		porcentaje_ocupacion_calculado = Area_total_conductores*100/Area_conduit

		if not porcentaje_ocupacion_forzado == 0:
			porcentaje_ocupacion = porcentaje_ocupacion_forzado
		else:
			porcentaje_ocupacion =  40

		if porcentaje_ocupacion_calculado <= porcentaje_ocupacion:
			medida_tuberia_pulg = tuberia_tabla[indice]
			medida_tuberia_mm = designacion_tubo_conduit_tabla[medida_tuberia_pulg]

			return {'medida_tuberia_pulg': medida_tuberia_pulg, 'medida_tuberia_mm': medida_tuberia_mm, 'Area_total_conductores': Area_total_conductores, 'Area_conduit': Area_conduit, 'porcentaje_ocupacion_calculado': porcentaje_ocupacion_calculado, 'Area_cable': Area_cable,  'Area_tierra_fisica': Area_tierra_fisica}

def calculador_cable_ampacidad(*datos, tabla_de_Ampacidades, calibre_tabla, Area_conductor_tabla):
	datos_totales = {}
	for x in datos:
		if isinstance(x, dict):
			datos_totales.update(x)

	Interruptor = datos_totales['Interruptor_1']
	Interruptor_forzado_1 = datos_totales['Interruptor_forzado_1']
	porcentaje_Irating_1_salida = datos_totales['porcentaje_Irating_1_salida']
	if Interruptor_forzado_1 == True or Interruptor_forzado_1 > 0:
		Interruptor = datos_totales['porcentaje_Irating_1_salida']*datos_totales['Interruptor_1']/100
	numero_conductores_por_fase = datos_totales['numero_conductores_por_fase']
	material_conductor = datos_totales['material_conductor']
	Tconductor = datos_totales['Tconductor']
	factor_agrupamiento = datos_totales['factor_agrupamiento']
	factor_temperatura = datos_totales['factor_temperatura']
	calibre = datos_totales.get('calibre')
	#tabla_de_Ampacidades
	#calibre_tabla
	#Area_conductor_tabla

	Ampacidad_tabla = tabla_de_Ampacidades[material_conductor][Tconductor]
	Ampacidad_corregida_tabla = [x*factor_agrupamiento*factor_temperatura for x in Ampacidad_tabla]

	if calibre in calibre_tabla:

		indice = calibre_tabla.index(calibre)
		Area = Area_conductor_tabla[indice]
		Ampacidad = Ampacidad_tabla[indice]
		Ampacidad_corregida = Ampacidad_corregida_tabla[indice]

		return {'indice_ampacidad': indice, 'calibre_ampacidad': calibre, 'Area_ampacidad': Area, 'Ampacidad': Ampacidad, 'Ampacidad_corregida': Ampacidad_corregida}

	while True:
		for indice, Ampacidad_corregida in enumerate(Ampacidad_corregida_tabla):
			if Ampacidad_corregida >= Interruptor/numero_conductores_por_fase:
				calibre = calibre_tabla[indice]
				Area = Area_conductor_tabla[indice]
				Ampacidad = Ampacidad_tabla[indice]

				if Area < 53 and numero_conductores_por_fase > 1:
					print('Ampacidad')
					print('!ERROR. Tamano de conductor menor a 1/0. No se puede poner ese tamaño de conductor en paralelo.')
					print(f'Conductor elegido por ampacidad menor a 1/0: {calibre}')
					print('')
				else:
					return {'indice_ampacidad': indice, 'calibre_ampacidad': calibre, 'Area_ampacidad': Area, 'Ampacidad': Ampacidad, 'Ampacidad_corregida': Ampacidad_corregida}
		else:
			print('Ampacidad')
			print('!ERROR. Tamano de conductor demasiado grande. Fuera de rango de las tablas.')
			print('Se recomienda aumentar numero de conductores por fase')
			print('')

			return