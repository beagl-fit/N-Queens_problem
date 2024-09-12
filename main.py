import argparse
# http://www.cs.toronto.edu/~victorn/tutorials/z3/SAT.html

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates CNF formula in the DIMACS format for N-queens problem.')
    parser.add_argument('integer', metavar='N', type=int, help='number of queens')  # required = True   is on by default if '--name' ain't used
    args = parser.parse_args()

    N = args.integer
    clauseNum = 0
    clauses = f"c CNF formula in the DIMACS format for {N}-queens problem\n"

    clauses += "c there is at least 1 queen in every line\n"
    # there is at least 1 queen in every line
    for i in range(0, N):       # line 1 -> line N
        for j in range(0, N):   # element 1 -> element N
            clauses += f"{i * N + j + 1} "
        clauses += "0\n"
        clauseNum += 1

    # doesn't change a thing...
    #clauses += "c\n"
    ## there is at least 1 queen in every column
    #for i in range(0, N):       # column 1 -> column N
    #    for j in range(0, N):   # element 1 -> element N
    #        clauses += f"{j * N + i + 1} "
    #    clauses += "0\n"
    #    clauseNum += 1

    clauses += "c there can be only 1 queen in every line\n"
    # there can be only 1 queen in every line
    for i in range(0, N):
        for j in range(i * N + 1, (i + 1) * N + 1):
            for k in range(j+1, (i + 1) * N + 1):
                clauses += f"{-j} {-k} "
                clauses += "0\n"
                clauseNum += 1

    clauses += "c there can be only 1 queen in every column\n"
    # there can be only 1 queen in every column
    for i in range(0, N):
        for j in range(1 + i, N * N + 1, N):
            for k in range(j+N,  N * N + 1, N):
                clauses += f"{-j} {-k} "
                clauses += "0\n"
                clauseNum += 1

    clauses += "c there can be only 1 queen on every diagonal\n"
    # there can be only 1 queen on every diagonal
    ## LR l1 diagonals
    for i in range(0, N):
        for j in range(i + 1, N * N, N + 1):
            for k in range(j + N + 1, N * N + 1 - N * i, N + 1):
                clauses += f"{-j} {-k} "
                clauses += "0\n"
                clauseNum += 1

    ## other LR diagonals
    for i in range(N + 1, N * N, N):
        for j in range(i, N * N, N + 1):
            for k in range(j + N + 1, N * N, N + 1):
                clauses += f"{-j} {-k} "
                clauses += "0\n"
                clauseNum += 1

    ## RL l1 diagonals
    for i in range(1, N):
        for j in range(i + 1, i * N, N - 1):
            for k in range(j + N - 1, (i + 1) * N, N - 1):
                clauses += f"{-j} {-k} "
                clauses += "0\n"
                clauseNum += 1

    ## other RL diagonals
    for i in range(2, N):
        for j in range(i * N, N * N, N - 1):
            for k in range(j + (N - 1), N * N, N - 1):
                clauses += f"{-j} {-k} "
                clauses += "0\n"
                clauseNum += 1

    header = f"p cnf {N*N} {clauseNum}\n"

    file = open("queens.out", "w")
    file.write(header)
    file.write(clauses)

    file.close()
