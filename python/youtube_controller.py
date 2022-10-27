from pydoc import apropos
import pyautogui
import serial
import argparse
import time
import logging

class MyControllerMap:
    def __init__(self):
        self.button = {'A': 'right', 'B': 'left', 'C': 'enter', 'D':'up', 'E':'down'} # Fast forward (10 seg) pro Youtube

class SerialControllerInterface:
    # Protocolo
    # byte 1 -> Botão 1 (estado - Apertado 1 ou não 0)
    # byte 2 -> EOP - End of Packet -> valor reservado 'X'
    
    
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate=baudrate)
        self.mapping = MyControllerMap()
        self.incoming = '0'
        self.aprovado = 0
        pyautogui.PAUSE = 0  ## remove delay
    
    def update(self):
        ## Sync protocol
        
      
        while self.incoming != b'X':
            self.incoming = self.ser.read()
            logging.debug("Received INCOMING: {}".format(self.incoming))
        
        data = self.ser.read()      
        print(f'data:{data}')
        print(data)

        # if data == b'P' and self.aprovado==0:
        #     logging.info("entrou 1 if")
        #     self.ser.write(b'P')
        #     self.aprovado=1
        #     print("deu certo")

        # if data == b'P' and self.aprovado :
        #     self.aprovado=0
        
        logging.debug("Received DATA: {}".format(data))

        confirma=b'\x05'
        if data == confirma:
            breakpoint()
            logging.info("KEYUP P")
            self.ser.write(b"\x05")
            print("entrou no 5")

        confirma=b'\x01'
        if data == confirma:
            logging.info("KEYDOWN A")
            pyautogui.keyDown(self.mapping.button['A'])

        confirma=b'\x02'
        if data == confirma:
            logging.info("KEYUP A")
            pyautogui.keyDown(self.mapping.button['B'])

        confirma=b'\x03'
        if data == confirma:
            logging.info("KEYDOWN A")
            pyautogui.keyDown(self.mapping.button['C'])

        confirma=b'\x04'
        if data == confirma:
            logging.info("KEYUP A")
            pyautogui.keyDown(self.mapping.button['D'])

            
        




        self.incoming = self.ser.read()


class DummyControllerInterface:
    def __init__(self):
        self.mapping = MyControllerMap()

    def update(self):
        pyautogui.keyDown(self.mapping.button['A'])
        time.sleep(0.1)
        pyautogui.keyUp(self.mapping.button['A'])
        logging.info("[Dummy] Pressed A button")
        time.sleep(1)


if __name__ == '__main__':
    interfaces = ['dummy', 'serial']
    argparse = argparse.ArgumentParser()
    argparse.add_argument('serial_port', type=str)
    argparse.add_argument('-b', '--baudrate', type=int, default=9600)
    argparse.add_argument('-c', '--controller_interface', type=str, default='serial', choices=interfaces)
    argparse.add_argument('-d', '--debug', default=False, action='store_true')
    args = argparse.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    print("Connection to {} using {} interface ({})".format(args.serial_port, args.controller_interface, args.baudrate))
    if args.controller_interface == 'dummy':
        controller = DummyControllerInterface()
    else:
        controller = SerialControllerInterface(port=args.serial_port, baudrate=args.baudrate)
    
    while True:
        controller.update()
