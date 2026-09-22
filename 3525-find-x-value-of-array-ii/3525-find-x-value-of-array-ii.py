class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)

        size = 1
        while size < n:
            size *= 2

        prod = [1] * (2 * size)
        cnt = [[0] * (2 * size) for _ in range(k)]

        def set_leaf(index, value):
            node = size + index
            remainder = value % k
            prod[node] = remainder

            for r in range(k):
                cnt[r][node] = 0

            cnt[remainder][node] = 1

        def update_node(node):
            left = node * 2
            right = left + 1
            left_prod = prod[left]

            prod[node] = (left_prod * prod[right]) % k

            for r in range(k):
                cnt[r][node] = cnt[r][left]

            for r in range(k):
                new_r = (left_prod * r) % k
                cnt[new_r][node] += cnt[r][right]

        for i in range(n):
            set_leaf(i, nums[i])

        for node in range(size - 1, 0, -1):
            update_node(node)

        def merge(A, B):
            prod_a, cnt_a = A
            prod_b, cnt_b = B

            new_prod = (prod_a * prod_b) % k
            new_cnt = cnt_a[:]

            for r in range(k):
                new_r = (prod_a * r) % k
                new_cnt[new_r] += cnt_b[r]

            return new_prod, new_cnt

        def query(left, right):
            left_result = (1, [0] * k)
            right_result = (1, [0] * k)
            left += size
            right += size

            while left < right:
                if left & 1:
                    data = (
                        prod[left],
                        [cnt[r][left] for r in range(k)]
                    )
                    left_result = merge(left_result, data)
                    left += 1

                if right & 1:
                    right -= 1
                    data = (
                        prod[right],
                        [cnt[r][right] for r in range(k)]
                    )
                    right_result = merge(data, right_result)

                left //= 2
                right //= 2

            return merge(left_result, right_result)

        answer = []
        for index, value, start, x in queries:
            set_leaf(index, value)

            node = (size + index) // 2

            while node:
                update_node(node)
                node //= 2

            _, counts = query(start, n)
            answer.append(counts[x])

        return answer