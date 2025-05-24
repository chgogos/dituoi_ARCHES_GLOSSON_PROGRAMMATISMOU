myReplicate :: (Eq t, Num t) => t -> a -> [a]
myReplicate 0 _ = []
myReplicate n x = x : myReplicate (n - 1) x

valueAt :: (Eq t, Num t) => [p] -> t -> p
valueAt [] _ = error "Out of bounds error"
valueAt (x : _) 0 = x
valueAt (x : xs) n = valueAt xs (n - 1)

myZip :: [a] -> [b] -> [(a, b)]
myZip _ [] = []
myZip [] _ = []
myZip (x : xs) (y : ys) = (x, y) : myZip xs ys