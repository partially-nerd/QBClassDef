DECLARE FUNCTION Num_subtract(self, y)
CLS

INPUT "Enter two numbers: ", x, y
x_afterSubtract = Num_subtract(x,y)
PRINT x_afterSubtract
END
FUNCTION Num_subtract(self, y)
  Num_subtract = self - y
END FUNCTION
