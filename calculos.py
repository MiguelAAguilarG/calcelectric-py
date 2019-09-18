from math import sqrt, sin, acos
import tablas

class Calculos():
    
    def __init__(self, datos_por_defecto_Calculos_dict = None, *args, **kargs):
        if isinstance(datos_por_defecto_Calculos_dict, dict):
            self.datos_por_defecto_Calculos_dict = datos_por_defecto_Calculos_dict
        else:
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

        self.datos_por_defecto_Calculos = self.datos_por_defecto_Calculos_dict

        self.factor_utilizacion_interruptor = self.datos_por_defecto_Calculos['factor_utilizacion_interruptor']
        self.factor_ampacidad_cable_fase = self.datos_por_defecto_Calculos['factor_ampacidad_cable_fase']
        self.factor_ampacidad_cable_neutro = self.datos_por_defecto_Calculos['factor_ampacidad_cable_neutro']
        self.factor_error_Interruptor = self.datos_por_defecto_Calculos['factor_error_Interruptor']
    
    def calculo_Inominal(self, Sistema, Carga, Voltaje, fp):

        if Sistema == 'monofasico':
            Inominal = Carga/(Voltaje*fp)
        if Sistema == 'trifasico':
            Inominal = Carga/(sqrt(3)*Voltaje*fp)

        return Inominal
    
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

    def calculo_conductores_activos_canalizacion(self, conductores_activos_adicionales_misma_canalizacion, misma_canalizacion, lineas, numero_conductores_por_fase, neutro_activo, numero_conductores_neutro):

        conductores_adicionales_totales = 0
        for calibre_conductores_adicionales, numero_conductores_adicionales in conductores_activos_adicionales_misma_canalizacion.items():
            conductores_adicionales_totales = conductores_adicionales_totales + numero_conductores_adicionales

        if misma_canalizacion == True:
            conductores_activos_canalizacion = lineas*numero_conductores_por_fase + int(neutro_activo)*numero_conductores_neutro + conductores_adicionales_totales
        elif misma_canalizacion == False:
            conductores_activos_canalizacion = lineas + int(neutro_activo)*numero_conductores_neutro + conductores_adicionales_totales

        return conductores_activos_canalizacion

    def calculo_Interruptor(self, Inominal, Interruptor_forzado, factor_utilizacion_interruptor, Interruptores):
        '''Interruptores = tablas.Tablas.Interruptores_tabla\nSe puede cambiar\nfactor_error_Interruptor = 0.01\nSe pude cambiar'''
        
        def calculo_Interruptor_parte_iterativa(Inominal, Interruptor_forzado, factor_utilizacion_interruptor, Interruptores):
            for x, Interruptor in enumerate(Interruptores):
                if Interruptor > 800:
                    self.factor_error_Interruptor = 0
                if Inominal <= Interruptor*(factor_utilizacion_interruptor - self.factor_error_Interruptor):
                    porcentaje_utilizacion_Interruptor = Inominal*100/Interruptor
                    return Interruptor, porcentaje_utilizacion_Interruptor
            else:
                print('!ERROR!. No se encontro un interruptor tan grande. Aumenta el nivel de voltaje para esa carga')

        if Interruptor_forzado == 0:
            Interruptor, porcentaje_utilizacion_Interruptor = calculo_Interruptor_parte_iterativa(Inominal, Interruptor_forzado, factor_utilizacion_interruptor, Interruptores)
        else:
            if Inominal <= Interruptor_forzado*(factor_utilizacion_interruptor - factor_error_Interruptor):
                    Interruptor = Interruptor_forzado
                    porcentaje_utilizacion_Interruptor = Inominal*100/Interruptor
            else:
                print('!ERROR!. Amperaje del Interruptor forzado menor a la Icorregida. Se procedio a calcular otro interruptor y porcentaje_utilizacion_Interruptor')
                Interruptor, porcentaje_utilizacion_Interruptor = calculo_Interruptor_parte_iterativa(Inominal, Interruptor_forzado, factor_utilizacion_interruptor, Interruptores)
        
        return Interruptor, porcentaje_utilizacion_Interruptor

    def calculo_factor_temperatura(self, tabla_factor_temperatura, Taislante, Tambiente):

        Tambiente_tabla_factor_temperatura = tabla_factor_temperatura['parametros']['Tambiente']

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

    def calculo_cable_ampacidad(self, calibres_tabla, Area_conductor_tabla, parte_adecuada_tabla_ampacidad_dict, Taislante, Tterminales, factor_agrupamiento, factor_temperatura, Interruptor, numero_conductores_por_fase):

        Ampacidad_tabla_Taislante = parte_adecuada_tabla_ampacidad_dict[Taislante]
        Ampacidad_tabla_Tterminales = parte_adecuada_tabla_ampacidad_dict[Tterminales]

        Ampacidad_corregida_tabla_Taislante = [x*factor_agrupamiento*factor_temperatura for x in Ampacidad_tabla_Taislante]

        Ampacidad_tabla = Ampacidad_tabla_Taislante
        Ampacidad_corregida_tabla = Ampacidad_corregida_tabla_Taislante

        while True:
            for indice, Ampacidad_corregida in enumerate(Ampacidad_corregida_tabla):
                if Ampacidad_corregida >= Interruptor/numero_conductores_por_fase:

                    indice_ampacidad = indice
                    calibre_ampacidad = calibres_tabla[indice]
                    Area_ampacidad = Area_conductor_tabla[indice]
                    Ampacidad = Ampacidad_tabla[indice]
                    Ampacidad_corregida = Ampacidad_corregida

                    if Taislante > Tterminales and (factor_agrupamiento != 1 or Tambiente_tabla_factor_temperatura != Tambiente):

                        if Ampacidad_corregida > Ampacidad_tabla_Tterminales[indice]:
                            print('Se tomo como Ampacidad_corregida la Ampacidad de Tterminales, ya que la Ampacidad_corregida de Taislante > Ampacidad de Tterminales')
                            Ampacidad = Ampacidad_corregida
                            Ampacidad_corregida = Ampacidad_tabla_Tterminales[indice]

                    if Area_ampacidad < 53 and numero_conductores_por_fase > 1:
                        print('Ampacidad')
                        print('!ERROR. Tamano de conductor menor a 1/0. No se puede poner ese tamaño de conductor en paralelo.')
                        print(f'Conductor elegido por ampacidad menor a 1/0: {calibre_ampacidad}')
                        print('')
                    else:
                        return indice_ampacidad, calibre_ampacidad, Area_ampacidad, Ampacidad, Ampacidad_corregida
            else:
                print('Ampacidad')
                print('!ERROR. Tamano de conductor demasiado grande. Fuera de rango de las tablas.')
                print('Se recomienda aumentar numero de conductores por fase')
                print('')

                return

    def calculo_cable_caida_de_tension(self, calibres_tabla, Area_conductor_tabla, resistencia_tabla, reactancia_tabla, caida_tension, Sistema, fp, Longitud, Inominal, Voltaje, numero_conductores_por_fase):

        while True:
            for indice_caida, Area_caida in enumerate(Area_conductor_tabla):
                calibre_caida = calibres_tabla[indice_caida]
                if indice_caida >= 20:
                    print('caída de tensión')
                    print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas.')
                    print('Se recomienda aumentar numero de conductores por fase')

                    return

                Ze = (resistencia_tabla[indice_caida]*fp + reactancia_tabla[indice_caida]*sin(acos(fp)))/1000

                if Sistema == 'monofasico':
                    caida_tension_calculada = 2*Ze*Longitud*Inominal*100/Voltaje/numero_conductores_por_fase
                elif Sistema == 'trifasico':
                    caida_tension_calculada = sqrt(3)*Ze*Longitud*Inominal*100/Voltaje/numero_conductores_por_fase
            
                if caida_tension_calculada <= caida_tension:

                    if Area_caida < 53 and numero_conductores_por_fase > 1:
                        print('caída de tensión')
                        print('!ERROR. Tamaño de conductor menor a 1/0. No se puede poner ese tamaño de conductor en paralelo.')
                        print(f'Conductor elegido por ampacidad menor a 1/0: {calibres_tabla[indice_caida]}')
                        print('')
                    else:
                        return indice_caida, calibre_caida, Area_caida, caida_tension_calculada
            else:
                print('caída de tensión')
                print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas.')
                print('Se recomienda aumentar numero de conductores por fase')

    def calculo_cable_tierra_fisica(self, calibres_tabla, Area_tierra_tabla, interruptor_tierra_fisica_tabla, tierra_fisica_tabla, Interruptor, canalizacion, Area_caida, Area_ampacidad):

        for indice_tierra_fisica, interruptor_tierra_fisica in enumerate(interruptor_tierra_fisica_tabla):
            if Interruptor <= interruptor_tierra_fisica:
                calibre_tierra_fisica = tierra_fisica_tabla[indice_tierra_fisica]
                Area_tierra_fisica = Area_tierra_tabla[calibres_tabla.index(calibre_tierra_fisica)]

                if Area_tierra_fisica < 21.2 and canalizacion == 'charola' and Area_caida <= Area_ampacidad:
                    print('Tierra física')
                    print('Tamaño de conductor menor a 4. No se puede poner ese tamaño de conductor en una charola.')
                    print(f'Conductor de tierra fisica elegido: {calibre_tierra_fisica}')
                    print(f'Material de tierra fisica: {material_conductor_tierra}')
                    print('')

                    Area_tierra_fisica = Area_tierra_tabla[calibres_tabla.index(calibre_tierra_fisica)]
            
                return indice_tierra_fisica, calibre_tierra_fisica, Area_tierra_fisica

    def calculo_cable_tierra_fisica_corregida(self, calibres_tabla, Area_conductor_tabla, Area_caida, Area_ampacidad, Area_tierra_fisica):

        factor_correccion_cable_tierra_fisica = Area_caida/Area_ampacidad
        Area_tierra_fisica_corregida_ideal = Area_tierra_fisica*factor_correccion_cable_tierra_fisica

        while True:
            for indice_tierra_fisica_corregida, Area_tierra_fisica_corregida in enumerate(Area_conductor_tabla):
                if Area_tierra_fisica_corregida >= Area_tierra_fisica_corregida_ideal:
                    calibre_tierra_fisica_corregida = calibres_tabla[indice_tierra_fisica_corregida]

                    return factor_correccion_cable_tierra_fisica, Area_tierra_fisica_corregida_ideal, indice_tierra_fisica_corregida, calibre_tierra_fisica_corregida, Area_tierra_fisica_corregida

    def calculo_eleccion_cable_ampacidad_caida(self, indice_ampacidad, calibre_ampacidad, Area_ampacidad, indice_caida, calibre_caida, Area_caida):

        if indice_ampacidad > indice_caida:
            indice_cable = indice_ampacidad
            calibre_cable = calibre_ampacidad
            Area_cable = Area_ampacidad
        else:
            indice_cable = indice_caida
            calibre_cable = calibre_caida
            Area_cable = Area_caida

        return indice_cable, calibre_cable, Area_cable
''' 
    def calculo_eleccion_cable_tierra_fisica(self):
        if indice_tierra_fisica > indice_tierra_fisica_corregida:
            indice_tierra_fisica_final = indice_tierra_fisica
            calibre_tierra_fisica_final = calibre_tierra_fisica
            Area_tierra_fisica_final = Area_tierra_fisica
        else:
            indice_tierra_fisica_final = indice_tierra_fisica_corregida
            calibre_tierra_fisica_final = calibre_tierra_fisica_corregida
            Area_tierra_fisica_final = Area_tierra_fisica_corregida

        if  adicionar_tierra_fisica_aislada == True:
            indice_tierra_fisica_aislada = indice_tierra_fisica_final
            calibre_tierra_fisica_aislada = calibre_tierra_fisica_final
            Area_tierra_fisica_aislada = Area_tierra_fisica_final

            return indice_tierra_fisica_final, calibre_tierra_fisica_final, Area_tierra_fisica_final, indice_tierra_fisica_aislada, calibre_tierra_fisica_aislada, Area_tierra_fisica_aislada

        return indice_tierra_fisica_final, calibre_tierra_fisica_final, Area_tierra_fisica_final

    def calculo_cable_neutro(self):

        if numero_conductores_neutro > 0:
            ': 1,'tamano_neutro_porcentaje_contra_fase': 100,

        if tipo_circuito == 'alimentador':
            indice_tierra_fisica_final = indice_tierra_fisica
            calibre_tierra_fisica_final = calibre_tierra_fisica
            Area_tierra_fisica_final = Area_tierra_fisica
        else:
            indice_tierra_fisica_final = indice_tierra_fisica_corregida
            calibre_tierra_fisica_final = calibre_tierra_fisica_corregida
            Area_tierra_fisica_final = Area_tierra_fisica_corregida

        if  adicionar_tierra_fisica_aislada == True:
            indice_tierra_fisica_aislada = indice_tierra_fisica_final
            calibre_tierra_fisica_aislada = calibre_tierra_fisica_final
            Area_tierra_fisica_aislada = Area_tierra_fisica_final

            return indice_tierra_fisica_final, calibre_tierra_fisica_final, Area_tierra_fisica_final, indice_tierra_fisica_aislada, calibre_tierra_fisica_aislada, Area_tierra_fisica_aislada

        return indice_tierra_fisica_final, calibre_tierra_fisica_final, Area_tierra_fisica_final

    def calculo_Area_conductores(self):

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