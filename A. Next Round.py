def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    count = 0
    kth_score = a[k - 1]
    
    for score in a:
        if score >= kth_score and score > 0:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()