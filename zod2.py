class TriangleChecker: 
    def __init__(self, a, b, c): 
        self.a, self.b, self.c = a, b, c 
     
    def is_triangle(self): 
        if self.a <= 0 or self.b <= 0 or self.c <= 0: 
            print("С отрицательными числами ничего не выйдет!") 
        else: 
            sides = sorted((self.a, self.b, self.c), key = lambda x : -x) 
            print("Ура, можно построить треугольник!") if sides[0] < sides[1] + sides[2] else print("Жаль, но из этого треугольник не сделать.")
#main           
###Предисловие: 
#если нажать ввести цыфру 1 то будет проверяться треугоьник со сторанами(-1,4,5), 
# если ввести цыфру 2 то будет проверятся тереугольник со сторанами(17,2,5), 
#а если ввести цыфру 3 то будет проверятся треугольник со сторонами(2,3,4)
a=int(input("Проверить треугольник"))
tri1 = TriangleChecker(-1, 4, 5) 
tri2 = TriangleChecker(17, 2, 2)
tri3 = TriangleChecker(2, 3, 4)  
if a==1:
    tri1.is_triangle()
 
elif a==2:
    tri2.is_triangle()
 
elif a==3:
    tri3.is_triangle()

