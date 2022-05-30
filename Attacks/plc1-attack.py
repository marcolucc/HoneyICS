import easymodbus.modbusClient
modbusclient = easymodbus.modbusClient.ModbusClient('localhost', 502)
modbusclient.connect()
modbusclient.write_single_coil(0,True)
modbusclient.close()