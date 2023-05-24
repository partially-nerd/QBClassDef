FN Series::ThreeNPlus1(b, n)
  a = b
  for i = 1 to n
    print a;
    if a mod 2 = 0 then
      a = a / 2
    else
      a = 3 * a + 1
    end if
  next i
END FN

-- MAIN --

CDEF series:Series
print; series::ThreeNPlus1(7, 10)
print; series::ThreeNPlus1(3, 8)