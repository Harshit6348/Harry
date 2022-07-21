class A:
    def f(self):
        x=10
        y=23
class B(A):
    def f1(self):
        z=self.x+self.y
        print(z)
ob=B()
ob.f
ob.f1
