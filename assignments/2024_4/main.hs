import System.IO
import Data.List ( sort )

main :: IO()
main = do
--    let file_name = "input1000"
--    let file_name = "input10000"
--    let file_name = "input100000"
   let file_name = "input1000000"
   content <- readFile (file_name ++ ".txt")
   let points = lines content
       list_of_string_triples = map words points
       tmp = [(read (x!!0) :: Double, read (x!!1) :: Double, read (x!!2) :: Double) | x <- list_of_string_triples]
       list_of_double_triples =  [(distance x, x) | x <- tmp]
    --    list_of_double_triples_sorted = sort list_of_double_triples
       list_of_double_triples_sorted = quicksort list_of_double_triples
       list_of_double_triples_sorted2 = [snd x | x <- list_of_double_triples_sorted]
       list_of_double_triples_sorted3 = [show (get1st x) ++ " " ++ show (get2nd x) ++ " " ++ show (get3rd x) | x <- list_of_double_triples_sorted2]
--    print  list_of_double_triples_sorted3
   writeFile (file_name ++ "-sorted-haskell.txt") (unlines list_of_double_triples_sorted3)

get1st (a,_,_) = a

get2nd (_,a,_) = a

get3rd (_,_,a) = a

slice i j s = drop i (take j s)

distance (x,y,z) =
    sqrt (x**2 + y**2 + z**2)

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
  let smallerSorted = quicksort [a | a <- xs, a <= x]
      biggerSorted = quicksort [a | a <- xs, a > x]
  in  smallerSorted ++ [x] ++ biggerSorted
