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
        
    def addId(self,name,var, i):
        tmp = -1 if i == " " else -i 
         
        self.ts[tmp].get("name_"+str(name))
        self.ts[tmp]["name_"+str(name)] = name
        self.ts[tmp].get("var_"+str(name))
        self.ts[tmp]["var_"+str(name)] = var
    
    def searchId(self,id):
        for i in range(0, len(self.ts)):
            if ("name_"+str(id)) in self.ts[-i]:
                return i, self.ts[-i],get("var_"+str(id))
            
            return i, False
        
        
    

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
        id.setName(self.getName())
        id.setInit(self.getInit())
        id.setUsed(self.getUsed())
        return id
    
    def toDictionay(self):
        dic = dict()
        dic['name'] = self.name
        dic['tipo'] = self.tipo
        dic['initialized'] = self.initialized
        dic['used'] = self.used
        
        return dic
        
        
        


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
    
    
    def toDictionay(self):
        dic = dict()
        dic['name'] = self.name
        dic['tipo'] = self.tipo
        dic['initialized'] = self.initialized
        dic['used'] = self.used
        dic['arguments'] = self.arguments
        return dic
        