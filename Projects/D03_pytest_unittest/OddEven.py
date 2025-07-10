class OddEven:
    def get_result(self, nums):
        result = []

        for num in nums:
            if num % 2 == 0:
                result.append('O')
            else:
                result.append('X')

        if all(x == 'O' for x in result) or all(x == 'X' for x in result):
            return None

        return result