class tablaValores:
    '''
    name = 'ejemplo'
    id = [id.__init__('a', 'b', 0, 1)] 
    
    ts = [dict(id.name, id)]
    '''
    ts = [dict()]
    def add_id(self, id):
        self.ts[-1][id.name] : id

    def add_context(self):
        self.ts.append(dict())

    def del_context(self):
        self.ts.pop();

    def findKey(self, key):
        for context in self.ts:
            if(key in context):
                return True

        return False

class id:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.initialized = False
        self.used = False

class variable(id):
    pass

class funcion(id):
    def __init__(self, name, type, parameters):
        super().__init__(name, type)
        self.parameters = parameters