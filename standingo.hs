import Text.ParserCombinators.Parsec
import Data.List
import Data.List.Split
import Data.Char
import Control.Applicative
import System.Environment


integer :: GenParser Char st Integer
integer = rd <$> many1 digit
    where rd = read :: String -> Integer

shylist :: [Char] -> [Int]
shylist [] = []
shylist (x:xs) = [digitToInt x] ++ (shylist xs)
                  
intList :: GenParser Char st [Int]
intList = do
  result <- many1 (noneOf "\n")
  return $ shylist result

testCase :: GenParser Char st [Int]
testCase = do
  vec_len <- integer
  spaces
  vec1 <- intList
  newline
  return vec1

cases :: GenParser Char st [[Int]]
cases = do
  num_cases <- integer
  spaces
  result <- many1 testCase
  eof
  return result

parseCases :: String -> Either ParseError [[Int]]
parseCases input = parse cases "(unknown)" input

procAudienceList :: Int -> Int -> [(Int, Int)] -> Int
procAudienceList numI _ [] = numI
procAudienceList numI numS ((k,v):xs)
  | v > 0 && (numS + numI) < k = procAudienceList numI' numS' xs
  | otherwise = procAudienceList numI numS' xs
  where numI' = max numI (k-numS)
        numS' = (numS + v)

numInvite :: [Int] -> Int
numInvite [] = 0
numInvite xs = procAudienceList 0 0 (zip [0..] xs)

testCaseToString :: (Int, Int) -> String
testCaseToString (x,y) = "Case #" ++ (show x) ++ ": " ++ (show y)

main = do
  args <- getArgs
  testdata <- readFile $ head args
  case (parseCases testdata) of
            Left _ -> print "error"
            Right testcases-> mapM_ putStrLn $ map testCaseToString (zip [1..((length testcases)+1)] (map numInvite testcases))
