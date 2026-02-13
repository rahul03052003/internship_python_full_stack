class A:
    #public method
    def m1(self):
        print("Public m1")
        self.__m5()
    def m2(self):
        print("Public m2")


    #protected method
    def _m4(self):
        print("Protected m4")
        
    #private method
    def __m5(self):
        print("Private m5")
        

'''class B:
    def m3(self):
        print("Public m3")
        self._m4()
    #a=A()
    #a.m4()
   ''' 

'''class B(A):
    def m3(self):
        print("Public m3")
        self._m4()

        '''
#b=B()
#b.m3()
#b._m4()
a=A()
a._m4()
a.m1()
