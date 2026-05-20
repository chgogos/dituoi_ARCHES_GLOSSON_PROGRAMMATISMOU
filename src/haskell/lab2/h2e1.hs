doubleFactorial :: (Eq p, Num p) => p -> p
doubleFactorial 0 = 1
doubleFactorial 1 = 1
doubleFactorial n = n * doubleFactorial (n - 2)

pow :: (Eq t, Num t, Num p) => p -> t -> p
pow x 0 = 1
pow x y = x * pow x (y - 1)

plusOne :: (Num a) => a -> a
plusOne x = x + 1

addition :: (Eq t1, Num t1, Num t2) => t2 -> t1 -> t2
addition x 0 = x
addition x y = plusOne (addition x (y - 1))

log2 :: (Num p, Integral t) => t -> p
log2 1 = 0
log2 x = 1 + log2 (x `div` 2)