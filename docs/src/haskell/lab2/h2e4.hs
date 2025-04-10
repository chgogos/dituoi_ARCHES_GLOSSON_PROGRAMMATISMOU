negateList :: (Num b) => [b] -> [b]
negateList xs = map negate xs

divisors :: Int -> [Int]
divisors p = [f | f <- [1 .. p], p `mod` f == 0]

divisorsList :: [Int] -> [[Int]]
divisorsList xs = map divisors xs