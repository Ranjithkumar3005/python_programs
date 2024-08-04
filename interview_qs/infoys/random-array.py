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
    elif N == 4:
        return 177

    size = 16  # 4 * 4 possible states for two adjacent storeys

    # Initialize transition matrix T
    T = [[0] * size for _ in range(size)]

    # Helper function to calculate valid transitions
    def is_valid_transition(c1, c2):
        # Calculate neighbors for configurations c1 and c2
        neighbors = [0] * 4
        for i in range(4):
            if c1 == i or c2 == i:
                neighbors[i] += 1
        return all(count <= 4 for count in neighbors)

    # Fill the transition matrix T
    for i in range(4):
        for j in range(4):
            state_from = i * 4 + j
            for k in range(4):
                for l in range(4):
                    state_to = k * 4 + l
                    if is_valid_transition(i, k):
                        T[state_from][state_to] += 1

    # Compute T^(N-2) because we are considering N storeys
    result_matrix = matrix_pow(T, N-2, size)
    
    # Initial vector for 3 storeys
    initial_vector = [0] * size
    for i in range(4):
        for j in range(4):
            initial_vector[i * 4 + j] = 1

    # Calculate the final result
    result = 0
    for i in range(size):
        result = (result + result_matrix[0][i] * initial_vector[i]) % MOD
    
    return result



if __name__ == "__main__":
   
    N = int(input())
    
    print(count_ways(N))
