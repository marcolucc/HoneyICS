import easymodbus.modbusClient
import time

plc1 = easymodbus.modbusClient.ModbusClient('127.0.0.1', 8502)

plc2 = easymodbus.modbusClient.ModbusClient('127.0.0.1', 8503)
plc2.connect()
plc1.connect()

while (True):
    try:
        inputRegisters = plc2.read_coils(0, 1)
    except:
        pass

    try:
        richiesta = inputRegisters[0]
    
        print(richiesta)
    except:
        pass
    try:
        plc1.write_single_coil(2, richiesta)

        plc1.read_coils(2, 1)
    except:
        pass
    #print("close connection")
    time.sleep(1)
    
