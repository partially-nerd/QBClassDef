FN Num::subtract(self, y)
  Num::subtract = self - y
END FN

-- MAIN --

CDEF x:Num, y:Num
INPUT "Enter two numbers: ", x, y
x::afterSubtract = x::subtract(y)
PRINT x::afterSubtract
