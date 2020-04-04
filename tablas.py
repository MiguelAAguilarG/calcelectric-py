class Tablas():

    Area_conductor_tabla = (2.08, 3.31, 5.26, 8.37, 13.3, 21.2, 26.7, 33.6, 42.4, 53.49, 67.43, 85.01, 107.2, 127, 152.0, 177, 203, 253, 304, 355, 380, 405, 456, 507, 633, 700, 887, 1013)

    calibres_tabla = ('14', '12', '10', '8', '6', '4', '3', '2', '1', '1/0', '2/0', '3/0', '4/0', '250', '300', '350', '400', '500', '600', '700', '750', '800', '900', '1000', '1250', '1500', '1750', '2000')

    Interruptores_tabla = (10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 125, 150, 175, 200, 225, 250, 300, 400, 500, 600, 700, 800, 1000, 1200, 1600, 2000)

    factor_agrupamiento_tabla = {3:1, 6:0.8, 9:0.7, 20:0.5, 30:0.45, 40:0.4, 50:0.35}

    Ampacidad_tabla_310_15_b16 = {}
    Ampacidad_tabla_310_15_b16['parametros'] = {'Tambiente': 30, 'maximo_numero_conductores_portadores_corriente': 3, 'Voltaje_maximo': 2000, 'material_conductor': ('cobre', 'aluminio'), 'Taislante': (60, 75 ,90), 'unidad': 'Ampere'}
    #############################################
    Ampacidad_tabla_310_15_b16['datos'] = {}
    Ampacidad_tabla_310_15_b16['datos']['material_conductor'] = {'cobre' : {}, 'aluminio': {}}
    #############################################
    Ampacidad_tabla_310_15_b16['datos']['material_conductor']['cobre'] = {'Taislante': {60: (), 75: (), 90: ()}}
    Ampacidad_tabla_310_15_b16['datos']['material_conductor']['cobre']['Taislante'][60] = (15, 20, 30, 40, 55, 70, 85, 90, 110, 125, 145, 165, 195, 215, 240, 260, 280, 320, 350, 385, 400, 410, 435, 455, 495, 525, 545, 555)
    Ampacidad_tabla_310_15_b16['datos']['material_conductor']['cobre']['Taislante'][75] = (20, 25, 35, 50, 65, 85, 100, 115, 130, 150, 175, 200, 230, 255, 285, 310, 335, 380, 420, 460, 475, 490, 520, 545, 590, 625, 650, 665)
    Ampacidad_tabla_310_15_b16['datos']['material_conductor']['cobre']['Taislante'][90] = (25, 30, 40, 55, 75, 95, 115, 130, 145, 170, 195, 225, 260, 290, 320, 350, 380, 430, 475, 520, 535, 555, 585, 615, 665, 705, 735, 750)
    #############################################
    Ampacidad_tabla_310_15_b16['datos']['material_conductor']['aluminio'] = {'Taislante': {60: (), 75: (), 90: ()}}
    #############################################
    Ampacidad_tabla_310_15_b16['datos']['material_conductor']['aluminio']['Taislante'][60] = (0, 0, 0, 0, 40, 55, 65, 75, 85, 100, 115, 130, 150, 170, 195, 210, 225, 260, 285, 315, 320, 330, 355, 375, 405, 435, 455, 470)
    Ampacidad_tabla_310_15_b16['datos']['material_conductor']['aluminio']['Taislante'][75] = (0, 0, 0, 0, 50, 65, 75, 90, 100, 120, 135, 155, 180, 205, 230, 250, 270, 310, 340, 375, 385, 395, 425, 445, 485, 520, 545, 560)
    Ampacidad_tabla_310_15_b16['datos']['material_conductor']['aluminio']['Taislante'][90] = (0, 0, 0, 0, 55, 75, 85, 100, 115, 135, 150, 175, 205, 230, 260, 280, 305, 350, 385, 425, 435, 445, 480, 500, 545, 585, 615, 630)

    Ampacidad_tabla_310_15_b17 = {}
    Ampacidad_tabla_310_15_b17['parametros'] = {'Tambiente': 30, 'maximo_numero_conductores_portadores_corriente': 1, 'Voltaje_maximo': 2000, 'material_conductor': ('cobre', 'aluminio'), 'Taislante': (60, 75 ,90), 'unidad': 'Ampere'}
    #############################################
    Ampacidad_tabla_310_15_b17['datos'] = {}
    Ampacidad_tabla_310_15_b17['datos']['material_conductor'] = {'cobre' : {}, 'aluminio': {}}
    #############################################
    Ampacidad_tabla_310_15_b17['datos']['material_conductor']['cobre'] = {'Taislante': {60: (), 75: (), 90: ()}}
    Ampacidad_tabla_310_15_b17['datos']['material_conductor']['cobre']['Taislante'][60] = (25, 30, 40, 60, 80, 105, 120, 140, 165, 195, 225, 260, 300, 340, 375, 420, 455, 515, 575, 630, 655, 680, 730, 780, 890, 980, 1070, 1155)
    Ampacidad_tabla_310_15_b17['datos']['material_conductor']['cobre']['Taislante'][75] = (30, 35, 50, 70, 95, 125, 145, 170, 195, 230, 265, 310, 360, 405, 445, 505, 545, 620, 690, 755, 785, 815, 870, 935, 1065, 1175, 1280, 1385)
    Ampacidad_tabla_310_15_b17['datos']['material_conductor']['cobre']['Taislante'][90] = (35, 40, 55, 80, 105, 140, 165, 190, 220, 260, 300, 350, 405, 455, 500, 570, 615, 700, 780, 850, 885, 920, 980, 1055, 1200, 1325, 1445, 1560)
    #############################################
    Ampacidad_tabla_310_15_b17['datos']['material_conductor']['aluminio'] = {'Taislante': {60: (), 75: (), 90: ()}}
    #############################################
    Ampacidad_tabla_310_15_b17['datos']['material_conductor']['aluminio']['Taislante'][60] = (0, 0, 0, 0, 60, 80, 95, 110, 130,150, 175, 200, 235, 265, 290, 330, 355, 405, 455, 500, 515, 535, 580, 625, 710, 795, 875, 960)
    Ampacidad_tabla_310_15_b17['datos']['material_conductor']['aluminio']['Taislante'][75] = (0, 0, 0, 0, 75, 100, 115, 135, 155, 180, 210, 240, 280, 315, 350, 395, 425, 485, 545, 595, 620, 645, 700, 750, 855, 950, 1050, 1150)
    Ampacidad_tabla_310_15_b17['datos']['material_conductor']['aluminio']['Taislante'][90] = (0, 0, 0, 0, 85, 115, 130, 150, 175, 205, 235, 270, 315, 355, 395, 445, 480, 545, 615, 670, 700, 725, 790, 845, 965, 1070, 1185, 1295)

    impedancia_tabla_9 = {}
    impedancia_tabla_9['parametros'] = {'Tambiente': 75, 'maximo_numero_conductores_portadores_corriente': 3, 'Voltaje_maximo': 600, 'material_conductor': ('cobre', 'aluminio'), 'canalizacion': 'conduit', 'material_canalizacion': ('pvc', 'aluminio', 'acero'), 'f': 60, 'unidad': 'ohm/km'}
    #############################################
    impedancia_tabla_9['datos'] = {'reactancia': {}, 'resistencia': {}}
    impedancia_tabla_9['datos']['reactancia'] = {'material_conductor': {'cobre': {}, 'aluminio':{}}}
    impedancia_tabla_9['datos']['reactancia']['material_conductor']['cobre'] = {'material_canalizacion': {'pvc': (), 'aluminio': (), 'acero': ()}}
    #############################################
    impedancia_tabla_9['datos']['reactancia']['material_conductor']['cobre']['material_canalizacion']['pvc'] = (0.19, 0.177, 0.164, 0.171, 0.167, 0.157, 0.154, 0.148, 0.151, 0.144, 0.141, 0.138, 0.135, 0.135, 0.135, 0.131, 0.131, 0.128, 0.128, 0.125, 0.121)
    impedancia_tabla_9['datos']['reactancia']['material_conductor']['cobre']['material_canalizacion']['aluminio'] = (0.19, 0.177, 0.164, 0.171, 0.167, 0.157, 0.154, 0.148, 0.151, 0.144, 0.141, 0.138, 0.135, 0.135, 0.135, 0.131, 0.131, 0.128, 0.128, 0.125, 0.121)
    impedancia_tabla_9['datos']['reactancia']['material_conductor']['cobre']['material_canalizacion']['acero'] = (0.24, 0.223, 0.207, 0.213, 0.21, 0.197, 0.194, 0.187, 0.187, 0.18, 0.177, 0.171, 0.167, 0.171, 0.167, 0.164, 0.161, 0.157, 0.157, 0.157, 0.151)
    #############################################
    impedancia_tabla_9['datos']['reactancia']['material_conductor']['aluminio'] = {'material_canalizacion': {'pvc': (), 'aluminio': (), 'acero': ()}}
    #############################################
    impedancia_tabla_9['datos']['reactancia']['material_conductor']['aluminio']['material_canalizacion']['pvc'] = (0.19, 0.177, 0.164, 0.171, 0.167, 0.157, 0.154, 0.148, 0.151, 0.144, 0.141, 0.138, 0.135, 0.135, 0.135, 0.131, 0.131, 0.128, 0.128, 0.125, 0.121)
    impedancia_tabla_9['datos']['reactancia']['material_conductor']['aluminio']['material_canalizacion']['aluminio'] = (0.19, 0.177, 0.164, 0.171, 0.167, 0.157, 0.154, 0.148, 0.151, 0.144, 0.141, 0.138, 0.135, 0.135, 0.135, 0.131, 0.131, 0.128, 0.128, 0.125, 0.121)
    impedancia_tabla_9['datos']['reactancia']['material_conductor']['aluminio']['material_canalizacion']['acero'] = (0.24, 0.223, 0.207, 0.213, 0.21, 0.197, 0.194, 0.187, 0.187, 0.18, 0.177, 0.171, 0.167, 0.171, 0.167, 0.164, 0.161, 0.157, 0.157, 0.157, 0.151)
    #############################################
    impedancia_tabla_9['datos']['resistencia'] = {'material_conductor': {'cobre': {}, 'aluminio': {}}}
    impedancia_tabla_9['datos']['resistencia']['material_conductor']['cobre'] = {'material_canalizacion': {'pvc': (), 'aluminio': (), 'acero': ()}}
    #############################################
    impedancia_tabla_9['datos']['resistencia']['material_conductor']['cobre']['material_canalizacion']['pvc'] = (10.2, 6.6, 3.9, 2.56, 1.61, 1.02, 0.82, 0.62, 0.49, 0.39, 0.33, 0.253, 0.203, 0.171, 0.144, 0.125, 0.108, 0.089, 0.075, 0.062, 0.049)
    impedancia_tabla_9['datos']['resistencia']['material_conductor']['cobre']['material_canalizacion']['aluminio'] = (10.2, 6.6, 3.9, 2.56, 1.61, 1.02, 0.82, 0.66, 0.52, 0.43, 0.33, 0.269, 0.22, 0.187, 0.161, 0.141, 0.125, 0.105, 0.092, 0.079, 0.062)
    impedancia_tabla_9['datos']['resistencia']['material_conductor']['cobre']['material_canalizacion']['acero'] = (10.2, 6.6, 3.9, 2.56, 1.61, 1.02, 0.82, 0.66, 0.52, 0.39, 0.33, 0.259, 0.207, 0.177, 0.148, 0.128, 0.115, 0.095, 0.082, 0.069, 0.059)
    #############################################
    impedancia_tabla_9['datos']['resistencia']['material_conductor']['aluminio'] = {'material_canalizacion': {'pvc': (), 'aluminio': (), 'acero': ()}}
    #############################################
    impedancia_tabla_9['datos']['resistencia']['material_conductor']['aluminio']['material_canalizacion']['pvc'] = (0.0, 0.0, 0.0, 0.0, 2.66, 1.67, 1.31, 1.05, 0.82, 0.66, 0.52, 0.43, 0.33, 0.279, 0.233, 0.2, 0.177, 0.141, 0.118, 0.095, 0.075)
    impedancia_tabla_9['datos']['resistencia']['material_conductor']['aluminio']['material_canalizacion']['aluminio'] = (0.0, 0.0, 0.0, 0.0, 2.66, 1.67, 1.31, 1.05, 0.85, 0.69, 0.52, 0.43, 0.36, 0.295, 0.249, 0.217, 0.194, 0.157, 0.135, 0.112, 0.089)
    impedancia_tabla_9['datos']['resistencia']['material_conductor']['aluminio']['material_canalizacion']['acero'] = (0.0, 0.0, 0.0, 0.0, 2.66, 1.67, 1.31, 1.05, 0.82, 0.66, 0.52, 0.43, 0.33, 0.282, 0.236, 0.207, 0.18, 0.148, 0.125, 0.102, 0.082)

    calibre_tierra_fisica_tabla_250_122 = {}
    calibre_tierra_fisica_tabla_250_122['parametros'] = {'material_conductor': ('cobre', 'aluminio'), 'unidad': 'calibre'}
    #############################################
    calibre_tierra_fisica_tabla_250_122['datos'] = {'interruptor': (), 'material_conductor': {'cobre': (), 'aluminio': ()}}
    #############################################
    calibre_tierra_fisica_tabla_250_122['datos']['interruptor'] = (15, 20, 60, 100, 200, 300, 400, 500, 600, 800, 1000, 1200, 1600, 2000, 2500, 3000, 400, 4000, 5000, 6000)
    #############################################    
    calibre_tierra_fisica_tabla_250_122['datos']['material_conductor']['cobre'] = ('14', '12', '10', '8', '6', '4', '2', '2', '1', '1/0', '2/0', '3/0', '4/0', '250', '350', '400', '500', '700', '800')
    calibre_tierra_fisica_tabla_250_122['datos']['material_conductor']['aluminio'] = ('0', '0', '0', '0', '4', '2', '1', '1/0', '2/0', '3/0', '4/0', '250', '350', '400', '600', '600', '750', '1200', '1200')

    conductor_electrodo_tabla_250_66 = {}
    conductor_electrodo_tabla_250_66['parametros'] = {}
    #############################################
    conductor_electrodo_tabla_250_66['datos'] = {}
    conductor_electrodo_tabla_250_66['datos']['conductor_entrada'] = {}
    conductor_electrodo_tabla_250_66['datos']['conductor_electrodo'] = {}
    #############################################
    conductor_electrodo_tabla_250_66['datos']['conductor_entrada']['material_conductor'] = {'cobre' : {0:33.6, 42.4:53.5, 67.4:85.01, 85.011:177, 177.1:304, 304.1:557.38, 557.381:1013}, 'aluminio': {0:53.5, 67.4:85.01, 107:127.2, 127.21:253, 253.1:456, 456.1:887, 887.1:1013}}
    conductor_electrodo_tabla_250_66['datos']['conductor_electrodo']['material_conductor'] = {'cobre' : ('8', '6', '4', '2', '1/0', '2/0', '3/0'), 'aluminio': ('6', '4', '2', '1/0', '3/0', '4/0', '250')}
    
    dimensiones_cables_tabla_5 = {}
    dimensiones_cables_tabla_5['parametros'] = {'aislante_condutor': ('THW, THHW, THW-2', 'THHN, THWN, THWN-2', 'XHHW, XHHW-2, XHH', 'RHH, RHW, RHW-2', 'RHH*, RHW*, RHW-2*'), 'unidad': 'mm'}
    dimensiones_cables_tabla_5['datos'] = {'aislante_condutor':{}}
    #############################################
    dimensiones_cables_tabla_5['datos']['aislante_condutor']['THW, THHW, THW-2'] = (8.968, 11.68, 15.68, 28.19, 46.84, 62.77, 73.16, 86.00, 122.6, 143.4, 169.3, 201.1, 239.9, 296.5, 340.7, 384.4, 427.0, 509.7, 627.7, 710.3, 751.7, 791.7, 874.9, 953.8, 1200, 1400, 1598, 1795)
    dimensiones_cables_tabla_5['datos']['aislante_condutor']['THHN, THWN, THWN-2'] = ()
    dimensiones_cables_tabla_5['datos']['aislante_condutor']['XHHW, XHHW-2, XHH'] = (3.378, 3.861, 4.47, 5.994, 6.96, 8.179, 8.89, 9.703, 11.23, 12.24, 13.41, 14.73, 16.21, 17.91, 19.3, 20.6, 21.79, 23.95, 26.75, 28.55, 29.41, 30.23, 31.85, 33.32, 37.57, 40.69, 43.59, 46.8)
    dimensiones_cables_tabla_5['datos']['aislante_condutor']['RHH, RHW, RHW-2'] = (4.902, 5.385, 5.994, 8.28, 9.246, 10.46, 11.18, 11.99, 14.78, 15.8, 16.97, 18.29, 19.76, 22.73, 24.13, 25.43, 26.62, 28.78, 31.57, 33.38, 34.24, 35.05, 36.68, 38.15, 43.92, 47.04, 49.94, 52.63)
    dimensiones_cables_tabla_5['datos']['aislante_condutor']['RHH*, RHW*, RHW-2*'] = (4.14, 4.623, 5.232, 6.756, 7.722, 8.941, 9.652, 10.46, 12.50, 13.51, 14.68, 16.0, 17.48, 19.43, 20.83, 22.12, 23.32, 25.48, 28.27, 30.07, 30.94, 31.75, 33.38, 34.85, 39.09, 42.21, 45.1, 47.8)

    porcentaje_llenado_conduit_tabla_1 = {1: 53, 2: 31, 3: 40}

    dimensiones_tubo_conduit_tabla_4 = {}
    dimensiones_tubo_conduit_tabla_4['parametros'] = {'tipo_conduit': ('EMT', 'ENT', 'FMC', 'IMC', 'LFNC-A*', 'LFNC-B*', 'LFNC-C*', 'LFMC', 'RMC', 'PVC, cédula 80', 'PVC, cédula 40', 'HDPE', 'PVC, tipo A', 'PVC, tipo EB'), 'medidas_estandar': 'in/mm'}
    #############################################
    dimensiones_tubo_conduit_tabla_4['datos'] = {'medidas_estandar': {}, 'tipo_conduit': {}}
    dimensiones_tubo_conduit_tabla_4['datos']['medidas_estandar_in'] = ('1/2', '3/4', '1', '1 1/4', '1 1/2', '2', '2 1/2', '3', '3 1/2', '4' ,'5', '6')
    dimensiones_tubo_conduit_tabla_4['datos']['medidas_estandar_mm'] = (16, 21, 27, 35, 41, 53, 63, 78, 91, 103, 1296, 155)
    #############################################
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['EMT'] = (15.8, 20.9, 26.6, 35.1, 40.9, 52.5, 69.4, 85.2, 97.4, 110.1)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['ENT'] = (14.2, 19.3, 25.4, 34, 39.9, 51.3)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['FMC'] = (16.1, 20.9, 25.9, 32.4, 39.1, 51.8, 63.5, 76.2, 88.9, 101)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['IMC'] = (16.8, 21.9, 28.1, 36.8, 42.7, 54.6, 64.9, 80.7, 93.2, 105.4)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['LFNC-A*'] = (16, 21, 26.5, 35.1, 40.7, 52.4)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['LFNC-B*'] = (16.1, 21.1, 26.8, 35.4, 40.3, 51.6)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['LFNC-C*'] = (15.7, 20.7, 26.2, 34.8, 40.3, 51.9)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['LFMC'] = (16.1, 21.1, 26.8, 35.4, 40.3, 61.6, 63.3, 78.4, 89.4, 102.1)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['RMC'] = (16.1, 21.2, 27, 35.4, 41.2, 52.9, 63.2, 78.5, 90.7, 102.9, 128.9, 154.8)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['PVC, cédula 80'] = (13.4, 18.3, 23.8, 31.9, 37.5, 48.6, 58.2, 72.7, 84.5, 96.2, 121.1, 145)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['PVC, cédula 40'] = (15.3, 20.4, 26.1, 34.5, 40.4, 52, 62.1, 77.3, 89.4, 101.5, 127.4, 153.2)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['HDPE'] = (15.3, 20.4, 26.1, 34.5, 40.4, 52, 62.1, 77.3, 89.4, 101.5, 127.4, 153.2)
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['PVC, tipo A'] = (17.80, 23.1, 29.8, 38.1, 43.7, 54.7, 66.9, 82, 93.7, 106.2)  
    dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit']['PVC, tipo EB'] = (0, 0, 0, 0, 0, 56.4, 0, 84.6, 96.6, 108.9, 135, 160.9)

    def __init__(self):
        pass


        
