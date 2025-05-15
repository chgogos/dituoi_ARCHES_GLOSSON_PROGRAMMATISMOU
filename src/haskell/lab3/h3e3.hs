main :: IO ()
main = do
    let numbers = [1,2,3,4,5]
    let doubled = map (\x -> x * 2) numbers
    print doubled
 
    let filtered = filter (\x -> x `mod` 2 == 0) numbers
    print filtered
