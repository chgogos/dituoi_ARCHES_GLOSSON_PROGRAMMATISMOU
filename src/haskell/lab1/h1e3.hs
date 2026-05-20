import System.IO

main :: IO ()
main = do
  putStr "Enter min : "
  hFlush stdout
  input1 <- getLine
  putStr "Enter max : "
  hFlush stdout
  input2 <- getLine
  putStr "Enter value : "
  hFlush stdout
  input3 <- getLine
  let min = read input1 :: Int
  let max = read input2 :: Int
  let x = read input3 :: Int
  putStrLn "Α' Τρόπος"
  if inRange min max x
    then putStrLn "YES"
    else putStrLn "NO"
  putStrLn "Β' Τρόπος"
  if inRange' min max x
    then putStrLn "YES"
    else putStrLn "NO"
  putStrLn "Γ' Τρόπος"
  if inRange'' min max x
    then putStrLn "YES"
    else putStrLn "NO"
  putStrLn "Δ' Τρόπος"
  if inRange''' min max x
    then putStrLn "YES"
    else putStrLn "NO"

inRange :: (Ord a) => a -> a -> a -> Bool
inRange min max x = min <= x && x <= max

inRange' :: (Ord p) => p -> p -> p -> Bool
inRange' min max x =
  let iub = x <= max
      ilb = x >= min
   in ilb && iub

inRange'' :: (Ord p) => p -> p -> p -> Bool
inRange'' min max x = ilb && iub
  where
    ilb = x >= min
    iub = x <= max

inRange''' :: (Ord a) => a -> a -> a -> Bool
inRange''' min max x
  | x < min = False
  | x > max = False
  | otherwise = True