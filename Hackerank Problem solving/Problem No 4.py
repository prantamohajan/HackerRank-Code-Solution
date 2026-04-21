if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    uniqe_scores = set(arr)
    list_scores = list(uniqe_scores)

    list_scores.sort()
    print(list_scores[-2])