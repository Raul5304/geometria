#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from figura import figura

class circulo(figura):
    
    __color = None
    
    # TODO: elevar color a la superclase
    def __init__(self, dimensions=..., color=None) -> None:
        super().__init__(dimensions)
        self.__color == color

if __name__ == "__main__":
    
    c0 = circulo()
    print(c0.getDimensiones)