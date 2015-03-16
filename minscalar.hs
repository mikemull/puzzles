
import Text.ParserCombinators.Parsec
import Data.List
import Data.List.Split
import Control.Applicative
import System.Environment

f :: String -> [Integer]
f x = Data.List.map read (splitOn " " x)

integer :: GenParser Char st Integer
integer = rd <$> many1 digit
    where rd = read :: String -> Integer

intList :: GenParser Char st [Integer]
intList = do
  result <- many1 (noneOf "\n")
  newline
  return $ f result

testCase :: GenParser Char st ([Integer],[Integer])
testCase = do
  vec_len <- integer
  spaces
  vec1 <- intList
  spaces
  vec2 <- intList
  return (vec1, vec2)

cases :: GenParser Char st [([Integer],[Integer])]
cases = do
  num_cases <- integer
  spaces
  result <- many1 testCase
  eof
  return result


parseCases :: String -> Either ParseError [([Integer],[Integer])]
parseCases input = parse cases "(unknown)" input


dotProduct :: [Integer] -> [Integer] -> Integer
dotProduct x y = sum ( zipWith (*) x y )

minScalar :: ([Integer],  [Integer]) -> Integer
minScalar (r, s) = dotProduct (sortBy (flip compare) r) (sort s)
-- minScalar (r, s) = minimum [dotProduct x y | (x,y) <- [(u,v) | u <- (permutations r), v <- (permutations s)]]

testCaseToString :: (Int, Integer) -> String
testCaseToString (x,y) = "Case #" ++ (show x) ++ ": " ++ (show y)

main = do
  args <- getArgs
  testdata <- readFile $ head args
  case (parseCases testdata) of
            Left _ -> print "error"
            Right testcases-> mapM_ putStrLn $ map testCaseToString (zip [1..((length testcases)+1)] (map minScalar testcases))

