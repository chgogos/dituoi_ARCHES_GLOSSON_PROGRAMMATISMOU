import H3e2
import Test.HUnit

tests :: Test
tests =
  TestList
    [ 
        "rectangle"  ~: rectangle 2 5 ~?= 10,
        "power"  ~: power 2 10 ~?= 1024,
        "sumList"  ~: sumList [1,2,3,4,5] ~?= 15,
        "isPrime 57"  ~: isPrime 57 ~?= False,
        "isPrime 101"  ~: isPrime 101 ~?= True
    ]

main :: IO ()
main = do
  _ <- runTestTT tests
  return ()
