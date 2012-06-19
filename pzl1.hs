
import Data.List

main = putStrLn (show fcheck)

fromDigits = foldl addDigit 0 where addDigit num d = 10*num + d

fcheck = head (filter (faccheck 9)  ( map fromDigits (permutations [1,2,3,4,5,6,7,8,9]) ))

faccheck :: Int -> Int -> Bool
faccheck l x
  | l == 1 =  True
  | x `mod` l == 0 = faccheck (l-1) (quot x 10)
  | otherwise = False

