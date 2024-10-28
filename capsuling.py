# Capsuling: access modifiers (public, protected, private)
# Python has NO access modifiers
 
# NO underline: public
    # can be used anywhere;

# _(ONE underline): protected
    # should NOT be used outside of a class
    # or subclasses

# __(TWO underlines): private
    # "name mangling"
    # must only be used in the class it was created

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__private)
        self.__metodo_private()
        return 'metodo publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'

fool1 = Foo()

# print(fool1._protected)

# print(fool1.public)

print(fool1._Foo__metodo_private())
