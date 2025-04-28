module H3e2 where

-- Υπολογισμός εμβαδού ορθογωνίου
rectangle :: (Num a) => a -> a -> a
rectangle h w = h * w

-- Ύψωση ακεραίου σε μη αρνητική ακέραια δύναμη
power :: Int -> Int -> Int
power _ 0 = 1
power x n = x * power x (n - 1)

-- Άθροισμα στοιχείων λίστας
sumList :: [Int] -> Int
sumList [] = 0
sumList (x:xs) = x + sumList xs 

-- Έλεγχος αν ένας ακέραιος είναι πρώτος
isPrime :: Int -> Bool
isPrime n
  | n <= 1    = False
  | otherwise = not (any (\x -> n `mod` x == 0) [2..(n-1)])

