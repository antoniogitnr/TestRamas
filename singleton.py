""" class CreateInstance:
    __instance = None
    def __new__(cls):
        if CreateInstance.__instance is None:
            print('Nueva instancia')
            CreateInstance.__instance = object.__new__(cls)
        return CreateInstance.__instance
    
if __name__ =='__main__':
    nuevainstancia = CreateInstance()
    nuevainstancia2 = CreateInstance()

    print(nuevainstancia is nuevainstancia2) """
    
def singleton(cls):
    __instance = dict()
    def wrap(*args,**kwargs):
        if cls not in __instance:
            print('Nueva instancia')
            __instance[cls] = cls(*args,**kwargs)
        return __instance[cls]
    return wrap

@singleton
class PrimerClase():
    pass

@singleton
class SegundaClase():
    pass

if __name__ == '__main__':
    nuevainstancia = PrimerClase()
    nuevainstancia2 = PrimerClase()
    print(nuevainstancia is nuevainstancia2)
    
    instanciaNueva = SegundaClase()
    instanciaNueva2 = SegundaClase()
    print(instanciaNueva is instanciaNueva2)