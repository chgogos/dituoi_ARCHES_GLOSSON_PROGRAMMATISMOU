primes :: [Integer]
primes = sieve [2..]
    where 
        sieve (p:xs) = p: sieve [n | n <- xs, n `mod` p /= 0 ] 

main :: IO ()
main = do
    print(take 1000 primes)