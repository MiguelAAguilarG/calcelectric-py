from math import sqrt, sin, acos
import tablas

class Calculos():
    
    def __init__(self, datos_por_defecto_Calculos_dict = None, *args, **kargs):
        if isinstance(datos_por_defecto_Calculos_dict, dict):
            self.datos_por_defecto_Calculos_dict = datos_por_defecto_Calculos_dict
        else:
            self.datos_por_defecto_Calculos_dict = {
            'factor_utilizacion_interruptor': 0.8,
            'factor_ampacidad_cable': 1.25,
            'factor_error_Interruptor': 0.01
            }
            self.datos_por_defecto_Calculos_descripcion_dict = {
            'factor_utilizacion_interruptor': 'Corriente de uso recomendable/Corriente nominal (>0-1) NOTA: Como regla general es del 80%',
            'factor_ampacidad_cable': 'Factor propuesto en la NOM-001-SEDE (1.25) antes de aplicar cualquier factor de correción y calculo debido al factor_utilizacion_interruptor para que no haya sobrecarga en las terminales del interruptor',
            'factor_error_Interruptor': 'Factor para elegir interruptor y se pueda elegir uno de menor tamaño como lo indica en algunas partes de la NOM-001-SEDE (>0-valor pequeño)'
            }

        self.datos_por_defecto_Calculos = self.datos_por_defecto_Calculos_dict

        self.factor_utilizacion_interruptor = self.datos_por_defecto_Calculos['factor_utilizacion_interruptor']
        self.factor_ampacidad_cable = self.datos_por_defecto_Calculos['factor_ampacidad_cable']
        self.factor_error_Interruptor = self.datos_por_defecto_Calculos['factor_error_Interruptor']
    
    def calculo_Inominal(self):

        if self.Sistema == 'monofasico':
            self.Inominal = self.Carga/(self.Voltaje*self.fp)
        if self.Sistema == 'trifasico':
            self.Inominal = self.Carga/(sqrt(3)*self.Voltaje*self.fp)

        return self.Inominal
    
    def calculo_Icorregida_factor_ampacidad_cable(self):
        '''Nota calculos.Calculos.calculo_Icorregida_factor_ampacidad_cable:\nLa ampacidad del cable se determino con un factor de 1.25,\npara cambiar este factor de ampacidad (corriente máxima) del cable, agregar a los datos, ejemplo:\ndatos_por_defecto_Calculos_dict = {{'factor_ampacidad_cable': 1.0}}\nclase = calculos.Calculos(datos_por_defecto_Calculos_dict)\nclase = elementos.Carga(datos_por_defecto_Calculos_dict)'''

        self.Icorregida_factor_ampacidad_cable = self.Inominal*self.factor_ampacidad_cable

        return self.Icorregida_factor_ampacidad_cable

    def calculo_Carga_corregida_factor_utilizacion_carga(self):

        self.Carga_corregida_factor_utilizacion_carga = self.Carga*self.factor_utilizacion_carga
    
        return self.Carga_corregida_factor_utilizacion_carga

    def calculo_Carga_corregida_factor_simultaneidad_carga(self):

        self.Carga_corregida_factor_simultaneidad_carga = self.Carga*self.factor_simultaneidad_carga
    
        return self.Carga_corregida_factor_simultaneidad_carga

    def calculo_conductores_canalizacion(self):
        if self.Sistema == 'monofasico':
            if self.misma_canalizacion == True:
                self.conductores_canalizacion = self.numero_conductores_por_fase*int(
                    self.misma_canalizacion) + int(self.neutro_presente)*self.numero_conductores_por_fase*int(self.misma_canalizacion)
            if self.misma_canalizacion == False:
                self.conductores_canalizacion = 1 + int(self.neutro_presente)
        if self.Sistema == 'trifasico':
            if self.misma_canalizacion == True:
                self.conductores_canalizacion = 3*self.numero_conductores_por_fase*int(self.misma_canalizacion) + int(self.neutro_presente)*self.numero_conductores_por_fase*int(self.misma_canalizacion)
            if self.misma_canalizacion == False:
                self.conductores_canalizacion = 3 + int(self.neutro_presente)

        return self.conductores_canalizacion

    def calculo_Interruptor(self, Interruptores = tablas.Tablas.Interruptores_tabla):
        '''Interruptores = tablas.Tablas.Interruptores_tabla\nSe puede cambiar\nfactor_error_Interruptor = 0.01\nSe pude cambiar'''
        
        def calculo_Interruptor_parte_iterativa(Interruptores = Interruptores):
            for x, Interruptor in enumerate(Interruptores):
                if self.Inominal <= Interruptor*(self.factor_utilizacion_interruptor - self.factor_error_Interruptor):
                    self.Interruptor = Interruptor
                    self.porcentaje_utilizacion_Interruptor = self.Inominal*100/self.Interruptor
                    break
            else:
                print('!ERROR!. No se encontro un interruptor tan grande. Aumenta el nivel de voltaje para esa carga')

        if self.Interruptor_forzado == 0:
            calculo_Interruptor_parte_iterativa()
        else:
            if self.Inominal <= self.Interruptor_forzado*(self.factor_utilizacion_interruptor - self.factor_error_Interruptor):
                    self.Interruptor = self.Interruptor_forzado
                    self.porcentaje_utilizacion_Interruptor = self.Inominal*100/self.Interruptor
            else:
                print('!ERROR!. Amperaje del Interruptor forzado menor a la Icorregida. Se procedio a calcular otro interruptor y porcentaje_utilizacion_Interruptor')
                calculo_Interruptor_parte_iterativa()
        
        return self.Interruptor, self.porcentaje_utilizacion_Interruptor

    def calculo_factor_temperatura(self, tabla_factor_temperatura):

        Tambiente_tabla = tabla_factor_temperatura['parametros']['Tambiente']

        self.factor_temperatura = sqrt((self.Taislante - self.Tambiente)/(self.Taislante - Tambiente_tabla))

        return self.factor_temperatura

    def calculo_factor_agrupamiento(self, tabla_factor_agrupamiento):

        if self.Longitud <= 0.6:#Factor de agrupamiento no aplica para 60 cm o menos. 310-15.(b)(3)(a)(2)
            self.factor_agrupamiento = 1
        else:
            for numero_conductores,factor in tabla_factor_agrupamiento.items(): #Determinar factor de agrupamiento NOTA: Ir a la Tabla 310-15(b)(3)(a)
                if self.conductores_canalizacion <= numero_conductores:
                    self.factor_agrupamiento = factor
                    break
            else:
                print('Demasiados conductores en la canalizacion')#modificar cuando se hagan clases
                self.factor_agrupamiento = 0

        return self.factor_agrupamiento

    def calculo_cable_ampacidad(self, calibres_tabla, Area_conductor_tabla, Ampacidad_especifica_tabla):

        Ampacidad_tabla = self.parte_adecuada_tabla_ampacidad_dict
        Ampacidad_corregida_tabla = [x*self.factor_agrupamiento*self.factor_temperatura for x in Ampacidad_tabla]

        while True:
            for indice, Ampacidad_corregida in enumerate(Ampacidad_corregida_tabla):
                if Ampacidad_corregida >= self.Interruptor/self.numero_conductores_por_fase:
                    self.indice_ampacidad = indice
                    self.calibre_ampacidad = calibres_tabla[indice]
                    self.Area_ampacidad = Area_conductor_tabla[indice]
                    self.Ampacidad = Ampacidad_tabla[indice]
                    self.Ampacidad_corregida = Ampacidad_corregida

                    if self.Area_ampacidad < 53 and self.numero_conductores_por_fase > 1:
                        print('Ampacidad')
                        print('!ERROR. Tamano de conductor menor a 1/0. No se puede poner ese tamaño de conductor en paralelo.')
                        print(f'Conductor elegido por ampacidad menor a 1/0: {self.calibre_ampacidad}')
                        print('')
                    else:
                        return self.indice_ampacidad, self.calibre_ampacidad, self.Area_ampacidad, self.Ampacidad, self.Ampacidad_corregida
            else:
                print('Ampacidad')
                print('!ERROR. Tamano de conductor demasiado grande. Fuera de rango de las tablas.')
                print('Se recomienda aumentar numero de conductores por fase')
                print('')

                return None

    def calculo_cable_caida_de_tension(self, calibres_tabla, Area_conductor_tabla, resistencia_tabla, reactancia_tabla):

        while True:
            for self.indice_caida, self.Area_caida in enumerate(Area_conductor_tabla):
                self.calibre_caida = calibres_tabla[self.indice_caida]
                if self.indice_caida >= 20:
                    print('caída de tensión')
                    print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas.')
                    print('Se recomienda aumentar numero de conductores por fase')

                    return

                self.Ze = (resistencia_tabla[self.indice_caida]*self.fp + reactancia_tabla[self.indice_caida]*sin(acos(self.fp)))/1000

                if self.Sistema == 'monofasico':
                    self.caida_tension_calculada = 2*self.Ze*self.Longitud*self.Inominal*100/self.Voltaje/self.numero_conductores_por_fase
                elif self.Sistema == 'trifasico':
                    self.caida_tension_calculada = sqrt(3)*self.Ze*self.Longitud*self.Inominal*100/self.Voltaje/self.numero_conductores_por_fase
            
                if self.caida_tension_calculada <= self.caida_tension:

                    if self.Area_caida < 53 and self.numero_conductores_por_fase > 1:
                        print('caída de tensión')
                        print('!ERROR. Tamaño de conductor menor a 1/0. No se puede poner ese tamaño de conductor en paralelo.')
                        print(f'Conductor elegido por ampacidad menor a 1/0: {calibres_tabla[self.indice_caida]}')
                        print('')
                    else:
                        return self.indice_caida, self.calibre_caida, self.Area_caida, self.caida_tension_calculada
            else:
                print('caída de tensión')
                print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas.')
                print('Se recomienda aumentar numero de conductores por fase')

    def calculo_cable_tierra_fisica(self, calibres_tabla, Area_tierra_tabla, interruptor_tierra_fisica_tabla, tierra_fisica_tabla):

        for self.indice_tierra_fisica, self.interruptor_tierra_fisica in enumerate(interruptor_tierra_fisica_tabla):
            if self.Interruptor <= self.interruptor_tierra_fisica:
                self.calibre_tierra_fisica = tierra_fisica_tabla[material_conductor_tierra][indice_tierra_fisica]
                self.Area_tierra_fisica = Area_tierra_tabla[calibres_tabla.index(calibre_tierra_fisica)]

                if self.Area_tierra_fisica < 21.2 and self.canalizacion == 'charola':
                    print('Tierra física')
                    print('Tamaño de conductor menor a 4. No se puede poner ese tamaño de conductor en una charola.')
                    print(f'Conductor de tierra fisica elegido: {self.calibre_tierra_fisica}')
                    print(f'Material de tierra fisica: {self.material_conductor_tierra}')
                    print('')

                    tierra = '4'
                    Area_tierra_fisica = Area_tierra_tabla[calibres_tabla.index(self.calibre_tierra_fisica)]
            
                return self.calibre_tierra_fisica, self.Area_tierra_fisica
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