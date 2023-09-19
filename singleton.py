class CreateInstance:
    __instance = None
    def __new__(cls):
        if CreateInstance.__instance is None:
            print('Nueva instancia')
            CreateInstance.__instance = object.__new__(cls)
        return CreateInstance.__instance
    
if __name__ =='__main__':
    nuevainstancia = CreateInstance()
    nuevainstancia2 = CreateInstance()

    print(nuevainstancia is nuevainstancia2)