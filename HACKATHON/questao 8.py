class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        N = len(nums) // 2 
        def get_sums(nums): 
            valor = {}
            N = len(nums)
            for i in range(1, N+1):
                sums = []
                for comb in combinations(nums, i):
                    s = sum(comb)
                    sums.append(s)
                valor[i] = sums
            return valor
        parte_esquerda, parte_direita = nums[:N], nums[N:]
        soma_esquerda, soma_direita = get_sums(parte_esquerda), get_sums(parte_direita)
        valor = abs(sum(parte_esquerda) - sum(parte_direita)) 
        total = sum(nums) 
        metade = total // 2 
        for i in range(1, N):
            left = soma_esquerda[i]
            right = soma_direita[N-i]
            right.sort() 
            for x in left:
                r = metade - x 
                p = bisect.bisect_left(right, r) 
                for q in [p, p-1]:
                    if 0 <= q < len(right):
                        left_ans_sum = x + right[q]
                        right_ans_sum = total - left_ans_sum
                        subtracao = abs(left_ans_sum - right_ans_sum)
                        valor = min(valor, subtracao) 
        return valor