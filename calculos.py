from math import sqrt, sin, acos, floor, ceil
import tablas

class Calculos():
    
    def __init__(self, datos_por_defecto_Calculos_dict = None):

        self.datos_por_defecto_Calculos_dict = {
        'factor_utilizacion_interruptor': 0.8,
        'factor_ampacidad_cable_fase': 1.25,
        'factor_ampacidad_cable_neutro': 1.25,
        'factor_error_Interruptor': 0.01,
        }

        datos_por_defecto_Calculos_descripcion_dict = {
        'factor_utilizacion_interruptor': 'Corriente de uso recomendable/Corriente nominal (>0-1) NOTA: Como regla general es del 80%',
        'factor_ampacidad_cable_fase': 'Factor propuesto en la NOM-001-SEDE (1.25) antes de aplicar cualquier factor de correción y calculo debido al factor_utilizacion_interruptor para que no haya sobrecarga en las terminales del interruptor',
        'factor_ampacidad_cable_neutro': 'Factor de 1.25 para estar acorde al factor_ampacidad_cable_fase. Considerar cada caso en particular',
        'factor_error_Interruptor': '(0 o algun valor pequeño). Factor para elegir interruptor y se pueda elegir uno de menor tamaño como lo indica en algunas partes de la NOM-001-SEDE (Ejemplo: 240-4(b) Dispositivos de sobrecorriente de 800 amperes o menos). Solo se aplica para interruptores de 800A o menos',
        }

        if isinstance(datos_por_defecto_Calculos_dict, dict):
            self.datos_por_defecto_Calculos_dict.update(datos_por_defecto_Calculos_dict)

        self.datos_por_defecto_Calculos = self.datos_por_defecto_Calculos_dict

        self.factor_utilizacion_interruptor = self.datos_por_defecto_Calculos['factor_utilizacion_interruptor']
        self.factor_ampacidad_cable_fase = self.datos_por_defecto_Calculos['factor_ampacidad_cable_fase']
        self.factor_ampacidad_cable_neutro = self.datos_por_defecto_Calculos['factor_ampacidad_cable_neutro']
        self.factor_error_Interruptor = self.datos_por_defecto_Calculos['factor_error_Interruptor']
    
    def calculo_Inominal(self, Sistema, lineas, numero_conductores_neutro, Carga, Voltaje, fp,factor_Inominal_fase_aplicado_neutro):

        if Sistema == 'monofasico':
            if lineas == 1:
                Inominal_fase = Carga/(Voltaje*fp)
                Inominal_neutro = Inominal_fase
            elif lineas == 2:
                Inominal_fase = Carga/(Voltaje*fp)
                Inominal_neutro = 0
        elif Sistema == 'trifasico':
            if lineas == 1:
                Inominal_fase = Carga/(Voltaje/sqrt(3)*fp)
                Inominal_neutro = Inominal_fase
            elif lineas == 2:
                if numero_conductores_neutro > 0:
                    Inominal_fase = (Carga/2)/(Voltaje/sqrt(3)*fp)
                    Inominal_neutro = Inominal_fase
                else:
                    Inominal_fase = Carga/(Voltaje*fp)
                    Inominal_neutro = 0
            elif lineas == 3:
                Inominal_fase = Carga/(sqrt(3)*Voltaje*fp)
                Inominal_neutro = 0

        Inominal_neutro = Inominal_fase*factor_Inominal_fase_aplicado_neutro

        return Inominal_fase, Inominal_neutro
    
    def calculo_Icorregida_factor_ampacidad_cable(self, Inominal, factor_ampacidad_cable):
        '''Nota calculos.Calculos.calculo_Icorregida_factor_ampacidad_cable:\nLa ampacidad del cable se determino con un factor de 1.25,\npara cambiar este factor de ampacidad (corriente máxima) del cable, agregar a los datos, ejemplo:\ndatos_por_defecto_Calculos_dict = {{'factor_ampacidad_cable': 1.0}}\nclase = calculos.Calculos(datos_por_defecto_Calculos_dict)\nclase = elementos.Carga(datos_por_defecto_Calculos_dict)'''

        Icorregida_factor_ampacidad_cable = Inominal*factor_ampacidad_cable

        return Icorregida_factor_ampacidad_cable

    def calculo_Carga_corregida_factor_utilizacion_carga(self, Carga, factor_utilizacion_carga):

        Carga_corregida_factor_utilizacion_carga = Carga*factor_utilizacion_carga
    
        return Carga_corregida_factor_utilizacion_carga

    def calculo_Carga_corregida_factor_simultaneidad_carga(self, Carga, factor_simultaneidad_carga):

        Carga_corregida_factor_simultaneidad_carga = Carga*factor_simultaneidad_carga
    
        return Carga_corregida_factor_simultaneidad_carga

    def calculo_conductores_activos_canalizacion(self, conductores_activos_adicionales_misma_canalizacion, misma_canalizacion, lineas, numero_conductores_por_fase, neutro_activo, numero_conductores_neutro, Inominal_fase, Inominal_neutro):

        conductores_adicionales_totales = 0
        for calibre_conductores_adicionales, numero_conductores_adicionales in conductores_activos_adicionales_misma_canalizacion.items():
            conductores_adicionales_totales = conductores_adicionales_totales + numero_conductores_adicionales

        if Inominal_neutro >= Inominal_fase:
            if numero_conductores_por_fase > numero_conductores_neutro:
                print('Precaución: Inominal_fase >= Inominal_neutro\npero numero_conductores_por_fase diferente a numero_conductores_neutro')
                print('Se precedio a numero_conductores_neutro = numero_conductores_por_fase\n')
                numero_conductores_neutro = numero_conductores_por_fase
            if neutro_activo == False:
                print('Precaución: neutro_activo == False, pero Inominal_neutro >= Inominal_fase')
                print('Se precedio a neutro_activo == True\n')
                neutro_activo = True

        if misma_canalizacion == True:
            conductores_activos_canalizacion = lineas*numero_conductores_por_fase + int(neutro_activo)*numero_conductores_neutro + conductores_adicionales_totales
        elif misma_canalizacion == False:
            conductores_activos_canalizacion = lineas + int(neutro_activo)*ceil(numero_conductores_neutro/numero_conductores_por_fase) + conductores_adicionales_totales

        return conductores_activos_canalizacion, numero_conductores_por_fase, numero_conductores_neutro, neutro_activo

    def calculo_Interruptor(self, Inominal, Interruptor_forzado, factor_utilizacion_interruptor, Interruptores, factor_Inominal_Interruptor):
        '''Interruptores = tablas.Tablas.Interruptores_tabla\nSe puede cambiar\nfactor_error_Interruptor = 0.01\nSe pude cambiar'''
        
        def calculo_Interruptor_parte_iterativa(Inominal, Interruptor_forzado, factor_utilizacion_interruptor, Interruptores, factor_Inominal_Interruptor):
            for x, Interruptor in enumerate(Interruptores):
                if Interruptor > 800:
                    self.factor_error_Interruptor = 0
                if Inominal <= Interruptor*(factor_utilizacion_interruptor - self.factor_error_Interruptor) and factor_Inominal_Interruptor <= 1/factor_utilizacion_interruptor:
                    porcentaje_utilizacion_Interruptor = Inominal*100/Interruptor
                    return Interruptor, porcentaje_utilizacion_Interruptor
                elif Inominal*factor_Inominal_Interruptor <= Interruptor*(1 - self.factor_error_Interruptor) and factor_Inominal_Interruptor > 1/factor_utilizacion_interruptor:
                    porcentaje_utilizacion_Interruptor = Inominal*100/Interruptor
                    return Interruptor, porcentaje_utilizacion_Interruptor
            else:
                print('!ERROR!. No se encontro un interruptor tan grande. Aumenta el nivel de voltaje para esa carga')

        if Interruptor_forzado == 0:
            Interruptor, porcentaje_utilizacion_Interruptor = calculo_Interruptor_parte_iterativa(Inominal, Interruptor_forzado, factor_utilizacion_interruptor, Interruptores, factor_Inominal_Interruptor)
        else:
            if Inominal <= Interruptor_forzado*(factor_utilizacion_interruptor - self.factor_error_Interruptor):
                    Interruptor = Interruptor_forzado
                    porcentaje_utilizacion_Interruptor = Inominal*100/Interruptor
            else:
                print('!ERROR!. Amperaje del Interruptor forzado menor a la Icorregida. Se procedio a calcular otro interruptor y porcentaje_utilizacion_Interruptor')
                Interruptor, porcentaje_utilizacion_Interruptor = calculo_Interruptor_parte_iterativa(Inominal, Interruptor_forzado, factor_utilizacion_interruptor, Interruptores)
        
        return Interruptor, porcentaje_utilizacion_Interruptor

    def calculo_factor_temperatura(self, Tambiente_tabla_factor_temperatura, Taislante, Tambiente):

        factor_temperatura = sqrt((Taislante - Tambiente)/(Taislante - Tambiente_tabla_factor_temperatura))

        return factor_temperatura

    def calculo_factor_agrupamiento(self, tabla_factor_agrupamiento, Longitud, conductores_activos_canalizacion):

        if Longitud <= 0.6:#Factor de agrupamiento no aplica para 60 cm o menos. 310-15.(b)(3)(a)(2)
            factor_agrupamiento = 1
        else:
            for numero_conductores, factor in tabla_factor_agrupamiento.items(): #Determinar factor de agrupamiento NOTA: Ir a la Tabla 310-15(b)(3)(a)
                if conductores_activos_canalizacion <= numero_conductores:
                    factor_agrupamiento = factor
                    break
            else:
                print('Demasiados conductores en la canalizacion')#modificar cuando se hagan clases
                factor_agrupamiento = 0

        return factor_agrupamiento

    def calculo_cable_ampacidad(self, calibres_tabla, Area_conductor_tabla, parte_adecuada_tabla_ampacidad_dict, Taislante, Tterminales, factor_agrupamiento, factor_temperatura, Interruptor, numero_conductores_por, Tambiente_tabla_factor_temperatura, Tambiente, Icorregida_factor_ampacidad_cable, factor_Inominal_Interruptor, palabra_control):

        Ampacidad_tabla_Taislante = parte_adecuada_tabla_ampacidad_dict[Taislante]
        Ampacidad_tabla_Tterminales = parte_adecuada_tabla_ampacidad_dict[Tterminales]

        Ampacidad_corregida_tabla_Taislante = [x*factor_agrupamiento*factor_temperatura for x in Ampacidad_tabla_Taislante]

        Ampacidad_tabla = Ampacidad_tabla_Taislante
        Ampacidad_corregida_tabla = Ampacidad_corregida_tabla_Taislante

        condicion = False
        while True:
            for indice, Ampacidad_corregida in enumerate(Ampacidad_corregida_tabla):
                if palabra_control == 'fase':
                    if Ampacidad_corregida >= Interruptor/numero_conductores_por and factor_Inominal_Interruptor <= 1:
                        if Ampacidad_corregida >= Icorregida_factor_ampacidad_cable/numero_conductores_por and factor_Inominal_Interruptor <= 1:
                            condicion = True
                    elif Ampacidad_corregida >= Icorregida_factor_ampacidad_cable/numero_conductores_por and factor_Inominal_Interruptor >= 1:
                            condicion = True
                elif palabra_control == 'neutro':
                    if numero_conductores_por == 0:
                        return False, False, False, False, False
                    elif Ampacidad_corregida >= Icorregida_factor_ampacidad_cable/numero_conductores_por:
                        condicion = True

                if condicion == True:

                    indice_ampacidad = indice
                    calibre_ampacidad = calibres_tabla[indice]
                    Area_ampacidad = Area_conductor_tabla[indice]
                    Ampacidad = Ampacidad_tabla[indice]
                    Ampacidad_corregida = Ampacidad_corregida

                    if Taislante > Tterminales and (factor_agrupamiento != 1 or Tambiente_tabla_factor_temperatura != Tambiente):

                        if Ampacidad_corregida > Ampacidad_tabla_Tterminales[indice]:
                            print(palabra_control)
                            print('Se tomo como Ampacidad_corregida la Ampacidad de Tterminales, ya que la Ampacidad_corregida de Taislante > Ampacidad de Tterminales. 110-14(c)(1)\n')
                            Ampacidad = Ampacidad_corregida
                            Ampacidad_corregida = Ampacidad_tabla_Tterminales[indice]

                    return indice_ampacidad, calibre_ampacidad, Area_ampacidad, Ampacidad, Ampacidad_corregida
            else:
                print('Ampacidad')
                print('!ERROR. Tamano de conductor demasiado grande. Fuera de rango de las tablas.')
                print('Se recomienda aumentar numero de conductores\n')

                return

    def calculo_cable_caida_de_tension(self, calibres_tabla, Area_conductor_tabla, resistencia_tabla, reactancia_tabla, caida_tension, Sistema, lineas, fp, Longitud, Inominal, Voltaje, numero_conductores_por_fase):

        while True:
            for indice_caida, Area_caida in enumerate(Area_conductor_tabla):
                calibre_caida = calibres_tabla[indice_caida]
                if indice_caida >= 20:
                    print('caída de tensión')
                    print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas.')
                    print('Se recomienda aumentar numero de conductores por fase\n')

                    return

                Ze = (resistencia_tabla[indice_caida]*fp + reactancia_tabla[indice_caida]*sin(acos(fp)))/1000

                if Sistema == 'monofasico':
                    if lineas == 1:
                        caida_tension_calculada = 2*Ze*Longitud*Inominal*100/Voltaje/numero_conductores_por_fase
                    elif lineas == 2:
                        caida_tension_calculada = 2*Ze*Longitud*Inominal*100/Voltaje/numero_conductores_por_fase
                elif Sistema == 'trifasico':
                    if lineas == 1:
                        caida_tension_calculada = 2*Ze*Longitud*Inominal*100/(Voltaje/sqrt(3))/numero_conductores_por_fase
                    elif lineas == 2:
                        caida_tension_calculada = 2*Ze*Longitud*Inominal*100/Voltaje/numero_conductores_por_fase
                    elif lineas == 3:
                        caida_tension_calculada = sqrt(3)*Ze*Longitud*Inominal*100/Voltaje/numero_conductores_por_fase
            
                if caida_tension_calculada <= caida_tension:
                    return indice_caida, calibre_caida, Area_caida, caida_tension_calculada
            else:
                print('caída de tensión')
                print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas.')
                print('Se recomienda aumentar numero de conductores por fase\n')

    def calculo_cable_tierra_fisica(self, calibres_tabla, Area_tierra_tabla, interruptor_tierra_fisica_tabla, tierra_fisica_tabla, Interruptor, canalizacion, Area_caida, Area_ampacidad):

        for indice_tierra_fisica, interruptor_tierra_fisica in enumerate(interruptor_tierra_fisica_tabla):
            if Interruptor <= interruptor_tierra_fisica:
                calibre_tierra_fisica = tierra_fisica_tabla[indice_tierra_fisica]
                Area_tierra_fisica = Area_tierra_tabla[calibres_tabla.index(calibre_tierra_fisica)]
            
                return indice_tierra_fisica, calibre_tierra_fisica, Area_tierra_fisica

    def calculo_cable_tierra_fisica_corregida(self, calibres_tabla, Area_conductor_tabla, Area_caida, Area_ampacidad, Area_tierra_fisica, tipo_circuito):

        if tipo_circuito == 'acometida':
            return False, False, False, False, False
        else:
            factor_correccion_cable_tierra_fisica = Area_caida/Area_ampacidad
            Area_tierra_fisica_corregida_caida_ideal = Area_tierra_fisica*factor_correccion_cable_tierra_fisica

            while True:
                for indice_tierra_fisica_corregida, Area_tierra_fisica_corregida_caida in enumerate(Area_conductor_tabla):
                    if Area_tierra_fisica_corregida_caida >= Area_tierra_fisica_corregida_caida_ideal:
                        calibre_tierra_fisica_corregida_caida = calibres_tabla[indice_tierra_fisica_corregida]

                        return factor_correccion_cable_tierra_fisica, Area_tierra_fisica_corregida_caida_ideal, indice_tierra_fisica_corregida, calibre_tierra_fisica_corregida_caida, Area_tierra_fisica_corregida_caida

    def calculo_eleccion_cable_ampacidad_VS_caida(self, indice_ampacidad, calibre_ampacidad, Area_ampacidad, indice_caida, calibre_caida, Area_caida, canalizacion, numero_conductores):

        if indice_ampacidad > indice_caida:
            indice_cable = indice_ampacidad
            calibre_cable = calibre_ampacidad
            Area_cable = Area_ampacidad
        else:
            indice_cable = indice_caida
            calibre_cable = calibre_caida
            Area_cable = Area_caida

        if 'charola' in canalizacion and indice_cable <= 5:
            print('fase\ncalculos.Calculos.calculo_eleccion_cable_ampacidad_VS_caida')
            print('!ERROR. Tamaño del conductor menor a 4.')
            print('***De forma automatica se procederá a seleccionar calibre 4***')
            print('No se puede poner ese tamaño de conductor en una charola. Artículo 392\n')

            indice_cable = 6
            calibre_cable = '4'
            Area_cable = 21.2

        if indice_cable <= 9 and numero_conductores > 1:
            print('fase\ncalculos.Calculos.calculo_eleccion_cable_ampacidad_VS_caida')
            print('!ERROR. Tamaño de conductor menor a 1/0.')
            print(f'Conductor elegido: {calibre_cable}')
            print('***De forma automatica se procederá a seleccionar calibre 1/0***')
            print('No se puede poner ese tamaño de conductor en paralelo.\n300-3. Conductores. b) Conductores del mismo circuito. 1) Instalaciones en paralelo. Se permitirá tender los conductores en paralelo de acuerdo con las disposiciones de 310-10(h) ... y los conductores de puesta a tierra del equipo deben cumplir con las disposiciones de 250-122. \n310-10. h) Conductores en paralelo. 1) Generalidades. Se permitirá que los conductores de aluminio, de aluminio recubierto de cobre o de cobre de tamaño 53.5 mm2 (1/0 AWG) y mayor, que sean los de fase, polaridad, neutro o el puesto a tierra del circuito estén conectados en paralelo (unidos eléctricamente en ambos extremos) cuando se instalen de acuerdo con (2) a (6) siguientes.\n')

            indice_cable = 10
            calibre_cable = '1/0'
            Area_cable = 53.49

        return indice_cable, calibre_cable, Area_cable

    def calculo_eleccion_cable_tierra_fisica(self, indice_tierra_fisica, calibre_tierra_fisica, Area_tierra_fisica, indice_tierra_fisica_corregida, calibre_tierra_fisica_corregida_caida, Area_tierra_fisica_corregida_caida, indice_cable_fase, calibre_cable_fase, Area_cable_fase, canalizacion, adicionar_tierra_fisica_aislada):

        if indice_tierra_fisica > indice_tierra_fisica_corregida:
            indice_tierra_fisica_final = indice_tierra_fisica
            calibre_tierra_fisica_final = calibre_tierra_fisica
            Area_tierra_fisica_final = Area_tierra_fisica
        else:
            indice_tierra_fisica_final = indice_tierra_fisica_corregida
            calibre_tierra_fisica_final = calibre_tierra_fisica_corregida_caida
            Area_tierra_fisica_final = Area_tierra_fisica_corregida_caida

        if 'charola' in canalizacion and indice_tierra_fisica_final <= 5:
            print('calculos.Calculos.calculo_eleccion_cable_tierra_fisica')
            print('tierra fisica')
            print('!ERROR. Tamaño del conductor menor a 4.')
            print('***De forma automatica se procederá a seleccionar calibre 4***')
            print('No se puede poner ese tamaño de conductor en una charola. Artículo 392\n')

            indice_tierra_fisica_final = 6
            calibre_tierra_fisica_final = '4'
            Area_tierra_fisica_final = 21.2

        if adicionar_tierra_fisica_aislada == True:
            indice_tierra_fisica_aislada = indice_tierra_fisica_final
            calibre_tierra_fisica_aislada = calibre_tierra_fisica_final
            Area_tierra_fisica_aislada = Area_tierra_fisica_final

            if 'charola' in canalizacion and indice_tierra_fisica_aislada <= 5:
                print('calculos.Calculos.calculo_eleccion_cable_tierra_fisica')
                print('tierra fisica aislada')
                print('!ERROR. Tamaño del conductor menor a 4.')
                print('***De forma automatica se procederá a seleccionar calibre 4***')
                print('No se puede poner ese tamaño de conductor en una charola. Artículo 392\n')

                indice_tierra_fisica_aislada = 6
                calibre_tierra_fisica_aislada = '4'
                Area_tierra_fisica_aislada = 21.2

        else:
            indice_tierra_fisica_aislada = False
            calibre_tierra_fisica_aislada = False
            Area_tierra_fisica_aislada = False

        if indice_tierra_fisica_final > indice_cable_fase:
            print('calculos.Calculos.calculo_eleccion_cable_tierra_fisica')
            print('!ERROR. indice_tierra_fisica_final > indice_cable_fase.')
            print('***De forma automatica se procederá a seleccionar un calibre de tierra fisica igual que el de fase***')
            print('250-122. Tamaño de los conductores de puesta a tierra de equipos a) General. Los conductores de puesta a tierra de equipos, de cobre, aluminio, o aluminio recubierto de cobre, del tipo alambre, no deben ser de tamaño menor a los mostrados en la Tabla 250-122, pero en ningún caso se exigirá que sean mayores que los conductores de los circuitos que alimentan el equipo.\n')

            indice_tierra_fisica_final = indice_cable_fase
            calibre_tierra_fisica_final = calibre_cable_fase
            Area_tierra_fisica_final = Area_cable_fase

            if adicionar_tierra_fisica_aislada == True:
                indice_tierra_fisica_aislada = indice_cable_fase
                calibre_tierra_fisica_aislada = calibre_cable_fase
                Area_tierra_fisica_aislada = Area_cable_fase

        return indice_tierra_fisica_final, calibre_tierra_fisica_final, Area_tierra_fisica_final, indice_tierra_fisica_aislada, calibre_tierra_fisica_aislada, Area_tierra_fisica_aislada

    def calculo_conductor_electrodo(self, numero_conductores_por_fase, Area_cable_fase, calibres_tabla, Area_conductor_tabla, tabla_conductor_entrada_dict, tabla_conductor_electrodo_lista):

        Area_fase = Area_cable_fase*numero_conductores_por_fase
        indice_tabla_conductor_electrodo = 0
        for Area_conductor_entrada_menor, Area_conductor_entrada_mayor in tabla_conductor_entrada_dict.items():
            if Area_fase >= Area_conductor_entrada_menor and Area_fase <= Area_conductor_entrada_mayor:

                calibre_conductor_electrodo = tabla_conductor_electrodo_lista[indice_tabla_conductor_electrodo]
                indice_conductor_electrodo = calibres_tabla.index(calibre_conductor_electrodo)
                Area_conductor_electrodo = Area_conductor_tabla[indice_conductor_electrodo]

                if indice_tabla_conductor_electrodo == 6:
                    factor_Area_fase_VS_Area_conductor_electrodo = Area_fase/Area_conductor_electrodo
                    if factor_Area_fase_VS_Area_conductor_electrodo >= 0.125:
                        pass
                    else:
                        print('calculos.Calculos.calculo_conductor_electrodo\nAdvertencia. factor_Area_fase_VS_Area_conductor_electrodo = Area_fase/Area_conductor_electrodo < 0.125\n Se procederá a calcular automáticamente otro conductor con un factor_Area_fase_VS_Area_conductor_electrodo > 0.125\n')
                        for indice_conductor, Area_conductor in Area_conductor_tabla:
                            factor_Area_fase_VS_Area_conductor_electrodo = Area_fase/Area_conductor
                            if factor_Area_fase_VS_Area_conductor_electrodo >= 0.125:

                                indice_conductor_electrodo = indice_conductor
                                calibre_conductor_electrodo = calibres_tabla[indice_conductor]
                                Area_conductor_electrodo = Area_conductor

                                break

                return indice_conductor_electrodo, calibre_conductor_electrodo, Area_conductor_electrodo
            
            indice_tabla_conductor_electrodo = indice_tabla_conductor_electrodo + 1

    def calculo_eleccion_cable_neutro(self, indice_cable_fase, calibre_cable_fase, Area_cable_fase, indice_ampacidad_neutro, calibre_ampacidad_neutro, Area_ampacidad_neutro, indice_tierra_fisica_final, calibre_tierra_fisica_final, Area_tierra_fisica_final, Inominal_fase, Inominal_neutro, factor_ampacidad_cable_neutro, tipo_circuito, numero_conductores_neutro):

        if Inominal_fase == Inominal_neutro and numero_conductores_neutro > 0:
            indice_cable_neutro = indice_cable_fase
            calibre_cable_neutro = calibre_cable_fase
            Area_cable_neutro = Area_cable_fase

            return indice_cable_neutro, calibre_cable_neutro, Area_cable_neutro

        else:
            if numero_conductores_neutro > 0:

                indice_cable_neutro = indice_ampacidad_neutro
                calibre_cable_neutro = calibre_ampacidad_neutro
                Area_cable_neutro = Area_ampacidad_neutro

                if tipo_circuito == 'derivado':
                    pass
                elif tipo_circuito == 'alimentador':
                    if factor_ampacidad_cable_neutro != 1:
                        print('Para tipo_circuito = alimentador, el factor_ampacidad_cable_neutro para cargas continuas puede ser de 1.\nSi desea hacer el cambio hagalo manualmente en datos.datos_por_defecto_Calculos_dict = {\'factor_ampacidad_cable_neutro\': 1}.\n')
                    if indice_ampacidad_neutro <= indice_tierra_fisica_final:
                        print('Para tipo_circuito = alimentador, el calibre_cable_neutro no puede ser menor a calibre_tierra_fisica_final\nSe procederá a hacer el cambio automáticamente\n')
                        indice_cable_neutro = indice_tierra_fisica_final
                        calibre_cable_neutro = calibre_tierra_fisica_final
                        Area_cable_neutro = Area_tierra_fisica_final
                elif tipo_circuito == 'acometida':
                    if indice_ampacidad_neutro <= indice_tierra_fisica_final:
                        print('Para tipo_circuito = acometida, el calibre_cable_neutro no puede ser menor a calibre_tierra_fisica_final(Se refiere al conductor de electrodo)\nSe procederá a hacer el cambio automáticamente\n')
                        indice_cable_neutro = indice_tierra_fisica_final
                        calibre_cable_neutro = calibre_tierra_fisica_final
                        Area_cable_neutro = Area_tierra_fisica_final
                elif tipo_circuito == 'derivacion':
                    pass
                elif tipo_circuito == 'motor':
                    pass
                else:
                    pass

                return indice_cable_neutro, calibre_cable_neutro, Area_cable_neutro

            else:
                return False, False, False


''' def calculo_Area_conductores(self):

        for indice_conduit, conduit in enumerate(tabla_conduit_adecuada_lista):


        if tabla_conduit_adecuada_lista
            indice_cable_fase = indice_ampacidad
            calibre_cable_fase = calibre_ampacidad
            Area_cable_fase = Area_ampacidad
        else:
            indice_cable_fase = indice_caida
            calibre_cable_fase = calibre_caida
            Area_cable_fase = Area_caida

        return indice_cable_fase, calibre_cable_fase, Area_cable_fase

    def calculo_dimension_conduit(self, tabla_conduit_adecuada_lista, indice_ampacidad, calibre_cable_fase = calibre_ampacidad
                Area_cable_fase = Area_ampacidad
            else:
                indice_cable_fase = indice_caida
                calibre_cable_fase = calibre_caida
                Area_cable_fase = Area_caida):

        for indice_conduit, conduit in enumerate(tabla_conduit_adecuada_lista):

            if tabla_conduit_adecuada_lista
                indice_cable_fase = indice_ampacidad
                calibre_cable_fase = calibre_ampacidad
                Area_cable_fase = Area_ampacidad
            else:
                indice_cable_fase = indice_caida
                calibre_cable_fase = calibre_caida
                Area_cable_fase = Area_caida

        return indice_cable_fase, calibre_cable_fase, Area_cable_fase'''

    

'''
for n=1:length(calibre_tabla)
  if cell2mat(tierra) == cell2mat(calibre_tabla(n))
  aux_3 = n;
  
  if canalizacion == 2 && aux_3 <=5
  disp('NOTA. Tierra fisica forzada a calibre 4 por estar en charola');
  aux_3 = 6;  
  end
  
  break
  end
end
Area_cable = conductores_canalizacion*Area_cable_tablas(aux_2)+Area_cable_tablas(aux_3);
%///////////////////////////////////////////////////////////////////////////////
%///////////////////////////////////////////////////////////////////////////////
ancho_charola_tablas = [50 100 150 200 225 300 400 450 500 600 750 900];
charola_columna1 = [1400 2800 4200 5600 6100 8400 11200 12600 14000 16800 21000 25200];
if canalizacion == 2
  
if Sistema == 1
  suma_diametros = 1*numero_conductores*Diametro_cable_tablas(aux_2) + neutro*numero_conductores*Diametro_cable_tablas(aux_2) + Diametro_cable_tablas(aux_3);
  suma_area = 1*numero_conductores*Area_cable_tablas(aux_2) + neutro*numero_conductores*Area_cable_tablas(aux_2) + Area_cable_tablas(aux_3);
elseif Sistema == 3
  suma_diametros = 3*numero_conductores*Diametro_cable_tablas(aux_2) + neutro*numero_conductores*Diametro_cable_tablas(aux_2) + Diametro_cable_tablas(aux_3);
  suma_area = 3*numero_conductores*Area_cable_tablas(aux_2) + neutro*numero_conductores*Area_cable_tablas(aux_2) + Area_cable_tablas(aux_3);
end

%///////////////////////////////////////////////////////////////////////////////
  if aux_2 >= 24 && aux_3 >= 24
    condicion = 'a';
    for n=1:length(ancho_charola)
      if suma_diametros <= ancho_charola_tablas(n)
        ancho_charola = ancho_charola_tablas(n);
        break
      end
    end
%///////////////////////////////////////////////////////////////////////////////
  elseif (aux_2 >= 14 && aux_2 <= 23) && (aux_3 >= 14 && aux_3 <= 23)
    condicion = 'b';
    for n=1:length(ancho_charola_tablas)
      if suma_area <= charola_columna1(n)
        ancho_charola = ancho_charola_tablas(n);
        break
      end
    end
%///////////////////////////////////////////////////////////////////////////////
  elseif aux_2 >= 24 && aux_3 < 24
    condicion = 'c';
    Sd = Diametro_cable_tablas(aux_2)*conductores_canalizacion;
    charola_columna2 = charola_columna1 - 28*Sd;
    for n=1:length(ancho_charola_tablas)
      if suma_area <= charola_columna2(n)
        ancho_charola = ancho_charola_tablas(n);
        break
      end
    end
%///////////////////////////////////////////////////////////////////////////////
  elseif (aux_2 >= 6 && aux_2 <= 13) || (aux_3 >= 6 && aux_3 <= 13)
    condicion = 'd';
    for n=1:length(ancho_charola_tablas)
      if suma_diametros <= ancho_charola_tablas(n)
        ancho_charola = ancho_charola_tablas(n);
        break
      end
    end
  else
    disp('Error. Diametro de conductor activo menor a calibre 4');
  end
%///////////////////////////////////////////////////////////////////////////////
    if suma_diametros ~=0
      suma_area = 0;
    elseif suma_area ~= 0
      suma_diametros =0
    end
end
'''