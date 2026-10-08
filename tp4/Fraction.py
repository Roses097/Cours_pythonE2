class Fraction:
    
    def __init__(self,num: int,deno : int):
        self.num = num
        self.deno = deno
        
    def __str__(self):
        return f"{self.num}/{self.deno}"
    
    def __add__(self,autre):
        newnum = self.num * autre.deno + autre.num * self.deno
        newdeno = self.deno * autre.deno
        return Fraction(newnum,newdeno)
    
    def __sub__(self,autre):
        newnum = self.num * autre.deno - autre.num * self.deno
        newdeno = self.deno * autre.deno
        return Fraction(newnum,newdeno)
    
    def __mul__(self,autre):
        newnum = self.num * autre.num 
        newdeno = self.deno * autre.deno
        return Fraction(newnum,newdeno)
    
    def __truediv__(self,autre):
        newnum = self.num * autre.deno 
        newdeno = self.deno * autre.num
        return Fraction(newnum,newdeno)
    