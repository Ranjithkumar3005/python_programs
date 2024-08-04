MOD = 10**9 + 7

def matrix_mult(A, B, size):
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(size)) % MOD
    return C

def matrix_pow(M, power, size):
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    base = M
    while power:
        if power % 2:
            result = matrix_mult(result, base, size)
        base = matrix_mult(base, base, size)
        power //= 2
    return result

def count_ways(N):
    if N == 3:
        return 54
    
    # Number of possible states: 4 houses per storey, so 4^2 = 16 possible states for two adjacent storeys
    size = 16

    # Transition matrix T
    T = [[0] * size for _ in range(size)]

    # Fill the transition matrix with valid transitions
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    state_from = i * 4 + j
                    state_to = k * 4 + l
                    # The state is valid if the total number of neighbors is <= 4
                    if (i + k <= 4) and (j + l <= 4):
                        T[state_from][state_to] += 1

    # Compute T^(N-2) because we are starting from N = 3
    result_matrix = matrix_pow(T, N-2, size)
    
    # Initial vector for 3 storeys
    initial_vector = [0] * size
    for i in range(4):
        for j in range(4):
            initial_vector[i * 4 + j] = 1
    
    result = 0
    for i in range(size):
        result = (result + result_matrix[0][i] * initial_vector[i]) % MOD
    
    return result

if __name__ == "__main__":
    N = int(input())
    
    print(count_ways(N))
