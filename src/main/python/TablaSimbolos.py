class TablaSimbolos:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
           cls._instance = super(TablaSimbolos, cls).__new__(cls)
        return cls._instance
    
    ts = [dict()]
    
    def addContex(self):
        self.ts.append(dict())
    
    def removeContex(self):
        self.ts.pop()
        
    
    

class Id:
    
    def __init__(self):
        self.name = ""
        self.tipo = ""
        self.initialized = False
        self.used = False
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def setTipo(self, tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo
    
    
    def setInit(self, init):
        self.initialized = init
    def getInit(self):
        return self.initialized
    
    def setUsed(self, used):
        self.used = used
    def getUsed(self):
        return self.used

    def cloneType(self):
        id = Id()
        id.setTipo(self.getTipo())
        id.setUsed(self.getUsed())
        return id
        
        


class Variable(Id):
    pass

class Funcion(Id):
    arguments = []
    
    def addArguments(self,name,tipo):
        self.arguments.append(dict())
        
        self.arguments[-1].get("type")
        self.arguments[-1]["type"] = tipo
        self.arguments[-1].get("name")
        self.arguments[-1]["name"] = name
        