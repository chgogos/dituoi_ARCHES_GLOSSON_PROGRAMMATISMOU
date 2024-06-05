quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x : xs) =
  let smallerSorted = quicksort [a | a <- xs, a <= x]
      biggerSorted = quicksort [a | a <- xs, a > x]
   in smallerSorted ++ [x] ++ biggerSorted

main :: IO ()
main = do
  let l1 = [9, 7, 3, 2, 1, 5, 6, 0, 4, 8]
      l2 = [3.142, 2.718, 1.414, 1.618]
      l3 = ["Ioannina", "Preveza", "Igoumenitsa", "Arta"]
      l4 = [False, True, False, True]
  print (quicksort l1)
  print (quicksort l2)
  print (quicksort l3)
  print (quicksort l4)