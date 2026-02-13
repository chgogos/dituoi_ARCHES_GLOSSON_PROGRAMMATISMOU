takeInt :: Int -> [a] -> [a]
takeInt _ [] = []
takeInt 0 _ = []
takeInt n (x : xs) = x : takeInt (n - 1) xs

dropInt :: Int -> [a] -> [a]
dropInt 0 x = x
dropInt _ [] = []
dropInt n (x : xs) = dropInt (n - 1) xs

sumInt :: [Int] -> Int
sumInt [] = 0
sumInt (x : xs) = x + sumInt xs

scanSum :: [Int] -> [Int]
scanSum [] = []
scanSum [x] = [x]
scanSum (x : y : xs) = x : scanSum ((x + y) : xs)