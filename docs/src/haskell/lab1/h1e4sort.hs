import Data.List (sort)

main :: IO ()
main = do
  let l1 = [9, 7, 3, 2, 1, 5, 6, 0, 4, 8]
      l2 = [3.142, 2.718, 1.414, 1.618]
      l3 = ["Ioannina", "Preveza", "Igoumenitsa", "Arta"]
      l4 = [False, True, False, True]
  print (sort l1)
  print (sort l2)
  print (sort l3)
  print (sort l4)