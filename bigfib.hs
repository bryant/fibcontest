-- fib = 0 : 1 : zipWith (+) fib (tail fib)

-- fib n = round $ phi ** fromIntegral n / sq5
--     where
--     sq5 = sqrt 5 :: Double
--     phi = (1 + sq5) / 2

import Data.Matrix (fromLists, getElem)
bigfib 0 = 0
bigfib n = getElem 1 2 $ (fromLists [[1, 1], [1, 0]]) ^ n
main = print $ bigfib 4374897
