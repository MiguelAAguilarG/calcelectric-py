from math import sqrt

class Calculos():
    
    def __init__(self)
    
    def calculo_corriente(self):

        if self.Sistema == 'monofasico':
            self.Inominal = self.Carga/(self.Voltaje*self.fp)
        if self.Sistema == 'trifasico':
            self.Inominal = self.Carga/(sqrt(3)*self.Voltaje*self.fp)

        self.I_corregida = self.Inominal*self.factor_carga
        self.Carga_corregida = self.Carga*self.factor_carga

        if self.Sistema == 'monofasico':
            if self.misma_canalizacion == True:
                self.conductores_canalizacion = self.numero_conductores_por_fase*int(
                    self.misma_canalizacion) + int(self.neutro_presente)*self.numero_conductores_por_fase*int(self.misma_canalizacion)
            if self.misma_canalizacion == False:
                self.conductores_canalizacion = 1 + int(self.neutro_presente)

        if self.Sistema == 'trifásico':
            if self.misma_canalizacion == True:
                self.conductores_canalizacion = 3*self.numero_conductores_por_fase*int(misma_canalizacion) + int(self.neutro_presente)*self.numero_conductores_por_fase*int(self.misma_canalizacion)
            if self.misma_canalizacion == False:
                self.conductores_canalizacion = 3 + int(self.neutro_presente)

        if self.Interruptor_forzado == True:
            for x in range(len(self.Interruptores_tabla)):
                if self.I_corregida <= self.Interruptores_tabla[x]:
                    self.Interruptor = self.Interruptores_tabla[x]
                    self.porcentaje_Irating = self.I_corregida*100/self.Interruptor
                    if porcentaje_Irating <= 80:
                        if Interruptores_tabla[x-1]*0.8 >= Inom  and (x-1) >= 0:
                            self.Interruptor = Interruptores_tabla[x-1]
                            porcentaje_Irating = Inominal*100/Interruptor
                    break
            else:
                print('!ERROR!. No se encontro interruptor tan grande. Aumenta el nivel de voltaje para esa carga')
        elif Interruptor_forzado > 0:
            if I_corregida <= Interruptor_forzado:
                Interruptor = Interruptor_forzado
                if I_corregida <= Interruptor_forzado*porcentaje_Irating:
                    porcentaje_Irating = porcentaje_Irating
                else:
                    porcentaje_Irating = I_corregida*100/Interruptor_forzado
            else:
                print('!ERROR!. Amperaje del Interruptor 1 forzado menor a la I calculada. Se procedio a calcular otro interruptor 1 y otro porcentaje Irating 1')
                for x in range(len(Interruptores_tabla)):
                    if I_corregida <= Interruptores_tabla[x]:
                        Interruptor = Interruptores_tabla[x]
                        porcentaje_Irating = I_corregida*100/Interruptor
                        if porcentaje_Irating <= 80:
                            if Interruptores_tabla[x-1]*0.8 >= Inom  and (x-1) >= 0:
                                Interruptor = Interruptores_tabla[x-1]
                                porcentaje_Irating = Inominal*100/Interruptor
                        break
                else:
                    print('!ERROR!. No se encontro interruptor 1 tan grande. Aumenta el nivel de voltaje para esa carga')
        elif Interruptor_forzado == False:
            for x in Interruptores_tabla:
                if I_corregida <= x:
                    Interruptor = x
                    porcentaje_Irating = I_corregida*100/Interruptor
                    break
                if Inominal*(factor_carga-ajuste_factor_carga/100) <= x:
                    Interruptor = x
                    porcentaje_Irating = I_corregida*100/Interruptor
                    break
            else:
                print('No se encontro interruptor 1 tan grande. Aumenta el nivel de voltaje para esa carga')
        else:
            print('No corresponde a ninguna opción para interruptor 1')

        if misma_canalizacion_amperaje == True:
            Interruptor_2 = Interruptor
            porcentaje_Irating_2 = porcentaje_Irating
        else:
            if Interruptor_forzado_2 == True:
                for x in range(len(Interruptores_tabla)):
                    if I_corregida <= Interruptores_tabla[x]:
                        Interruptor_2 = Interruptores_tabla[x]
                        porcentaje_Irating_2 = I_corregida*100/Interruptor_2
                        if porcentaje_Irating_2 <= 80:
                            if Interruptores_tabla[x-1]*0.8 >= Inom  and (x-1) >= 0:
                                Interruptor_2 = Interruptores_tabla[x-1]
                                porcentaje_Irating_2 = Inominal*100/Interruptor_2
                        break
                else:
                    print('!ERROR!. No se encontro interruptor 2 tan grande. Aumenta el nivel de voltaje para esa carga')
            elif Interruptor_forzado_2 > 0:
                if I_corregida <= Interruptor_forzado_2:
                    Interruptor_2 = Interruptor_forzado_2
                    if I_corregida <= Interruptor_forzado_2*porcentaje_Irating_2:
                        porcentaje_Irating_2 = porcentaje_Irating_2
                    else:
                        porcentaje_Irating_2 = I_corregida*100/Interruptor_forzado_2
                else:
                    print('!ERROR!. Amperaje del Interruptor 2 forzado menor a la I calculada. Se procedio a calcular otro interruptor 2 y otro porcentaje Irating 2')
                    for x in range(len(Interruptores_tabla)):
                        if I_corregida <= Interruptores_tabla[x]:
                            Interruptor_2 = Interruptores_tabla[x]
                            porcentaje_Irating_2 = I_corregida*100/Interruptor_2
                            if porcentaje_Irating_2 <= 80:
                                if Interruptores_tabla[x-1]*0.8 >= Inom  and (x-1) >= 0:
                                    Interruptor_2 = Interruptores_tabla[x-1]
                                    porcentaje_Irating_2 = Inominal*100/Interruptor_2
                            break
                    else:
                        print('!ERROR!. No se encontro interruptor 2 tan grande. Aumenta el nivel de voltaje para esa carga')
            elif Interruptor_forzado_2 == False:
                for x in Interruptores_tabla:
                    if I_corregida <= x:
                        Interruptor_2 = x
                        porcentaje_Irating_2 = I_corregida*100/Interruptor_2
                        break
                    if Inominal*(factor_carga-ajuste_factor_carga/100) <= x:
                        Interruptor_2 = x
                        porcentaje_Irating_2 = I_corregida*100/Interruptor_2
                        break
                else:
                    print('No se encontro interruptor 2 tan grande. Aumenta el nivel de voltaje para esa carga')
            else:
                print('No corresponde a ninguna opción para interruptor 2')

        Tconductor = datos_totales['Tconductor']
        Tambiente = datos_totales['Tambiente']
        #Tambiente_tablas

        factor_temperatura = sqrt((Tconductor-Tambiente)/(Tconductor-Tambiente_tablas))

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
                caida_tension_calculada = 2*Ze*Inominal*100/Voltaje/numero_conductores_por_fase
            elif Sistema == 'trifásico':
                caida_tension_calculada = sqrt(3)*Ze*Inominal*100/Voltaje/numero_conductores_por_fase

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
                    caida_tension_calculada = 2*Ze*Longitud*Inominal*100/Voltaje/numero_conductores_por_fase
                elif Sistema == 'trifásico':
                    caida_tension_calculada = sqrt(3)*Ze*Longitud*Inominal*100/Voltaje/numero_conductores_por_fase
            
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

        Ampacidad_tabla = tabla_de_Ampacidades[material_conductor][Tconductor]
        Ampacidad_corregida_tabla = [x*factor_agrupamiento*factor_temperatura for x in Ampacidad_tabla]

        if calibre in calibre_tabla:

            indice = calibre_tabla.index(calibre)
            Area = Area_conductor_tabla[indice]
            Ampacidad = Ampacidad_tabla[indice]
            Ampacidad_corregida = Ampacidad_corregida_tabla[indice]

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
            else:
                print('Ampacidad')
                print('!ERROR. Tamano de conductor demasiado grande. Fuera de rango de las tablas.')
                print('Se recomienda aumentar numero de conductores por fase')
                print('')

