select Score,
  dense_rank() over(Order By Score desc) `Rank`
FROM Scores;