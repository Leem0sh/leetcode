class Solution:
    def numberOfMatches(self, n: int) -> int:
        number_of_matches = 0
        while n > 1:

            if n % 2 == 0:
                number_of_matches += n / 2
                n = n / 2
                print(f"Matches: {number_of_matches}")
                print(f"Number of teams: {n}")
            else:
                number_of_matches += (n - 1) / 2
                n = (n - 1) / 2 + 1
                print(f"Matches: {number_of_matches}")
                print(f"Number of teams: {n}")

        print(number_of_matches)
        return int(number_of_matches)


Solution().numberOfMatches(87)