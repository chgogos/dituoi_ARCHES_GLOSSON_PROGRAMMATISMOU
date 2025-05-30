import Data.Char (digitToInt)

-- Ελέγχει αν ο αριθμός περνάει το τεστ του Luhn
luhnCheck :: String -> Bool
luhnCheck number = total `mod` 10 == 0
  where
    digits = map digitToInt number
    reversed = reverse digits
    processed = zipWith doubleEverySecond [0..] reversed
    total = sum processed

-- Διπλασιάζει κάθε δεύτερο ψηφίο, αφαιρώντας 9 αν χρειάζεται
doubleEverySecond :: Int -> Int -> Int
doubleEverySecond index digit
  | odd index = let d = digit * 2 in if d > 9 then d - 9 else d
  | otherwise = digit

main :: IO ()
main = do
    putStrLn "Δώσε αριθμό:"
    number <- getLine
    if all (`elem` ['0'..'9']) number then
        if luhnCheck number
            then putStrLn "Έγκυρος αριθμός κάρτας."
            else putStrLn "Μη έγκυρος αριθμός κάρτας."
    else
        putStrLn "Ο αριθμός πρέπει να περιέχει μόνο ψηφία."
