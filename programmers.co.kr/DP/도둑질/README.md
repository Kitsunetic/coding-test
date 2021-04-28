## 문제 메모 / 개인적인 풀이

https://programmers.co.kr/learn/courses/30/lessons/42897

프로그래머스 연습 문제에서 몇 안되는 Level4 문제.

순환형 데이터(circulation data)에서 DP를 적용할 방법(state가 저장이 되는지 등)을 찾고 적용하는 부분이 난이도가 있기 때문에 level 4에 적합하다고 생각됨.

- 최선의 방법은 모든 경우를 확인해봐야함
- 시작점과 어떤 집을 안 털지 정해지면 그 조건에서 최대로 훔칠 수 있는 money는 결정적임.

그러므로 아래와 같이 푼다.

- DP의 사이즈는 (money사이즈)x(2 or 3)이다.
- 세로축은 n번 째 집까지 털었을 때 훔친 돈을 의미
- 가로축은 몇 번째 집부터 시작했는지 (짝수일 때는 처음 2개의 집에서만 시작 가능, 홀수일 때는 처음 3개의 집에서 시작 가능)
- 처음 1번째 집에서 시작하면 맨 마지막 집은 훔칠 수 없다.

예를들어 money가 `[1, 2, 3, 4, 5, 6, 7, 8, 9]` 이면 DP는 아래와 같이 초기화된다.  
`.`은 아직 값을 정하지 못했다는 뜻.

-|A|B|C
---|---|---|---
1|1|X|X
2|X|2|X
3|.|X|3
4|.|.|X
5|.|.|.

여기서 대각선 방향으로 dp를 iterate 한다.

- `dp[3][A] = dp[1][A] + money[3]`
- `dp[4][B] = dp[2][B] + money[4]`
- `dp[5][C] = dp[3][C] + money[5]`

-|A|B|C
---|---|---|---
1|1|X|X
2|X|2|X
3|4|X|3
4|.|6|X
5|.|.|8
6|.|.|.
7|.|.|.
8|.|.|.
9|.|.|.

이제 3번 행부터는 `dp[4][A] = max(dp[1][A], dp[3][A]) + money[4]` 를 끝까지 반복한다. (단, dp[9][A]에는 값이 들어가면 안된다.)

## 소스코드

```py
def solution(money):
    L = len(money)
    t = 2 + (L & 0x01)  # L이 홀/짝수일 때 dp의 column 수가 바뀜

    if L == 3:
        return max(money)

    dp = [[-1 for _ in range(t)] for _ in range(L)]
    mv = -1
    for j in range(t):
        dp[j][j] = money[j]
        mv = max(mv, money[j])
    for j in range(t):
        dp[2 + j][j] = money[j] + money[2 + j]
        mv = max(mv, money[j] + money[2 + j])

    for i in range(3, L - 2):
        for j in range(t):
            v = max(dp[i + j - 2][j], dp[i + j - 3][j]) + money[i + j]
            dp[i + j][j] = v
            mv = max(mv, v)
    for j in range(2):
        v = max(dp[L - 2 + j - 2][j], dp[L - 2 + j - 3][j]) + money[L - 2 + j]
        dp[L - 2 + j][j] = v
        mv = max(mv, v)

    return mv
```

O(3N)... 하지만 시간초과가 발생한다.
풀이 자체는 잘못되지 않은 것 같아서 C++로도 짜보았다.

```cpp
#include <string>
#include <vector>

using namespace std;

int maxAt(std::vector<int> &vector_name)
{
    int max = 0;
    for (auto val : vector_name)
    {
        if (max < val)
            max = val;
    }
    return max;
}

int solution(vector<int> money)
{
    int L = money.size();
    int t = 2 + (L & 0x01);

    if (L == 3)
        return maxAt(money);

    int dp[1000000][3];
    int m = 0;
    for (int j = 0; j < t; j++)
    {
        dp[j][j] = money[j];
        m = money[j];

        dp[2 + j][j] = money[j] + money[2 + j];
        m = max(dp[j][j], dp[2 + j][j]);
    }

    for (int i = 3; i < L - 2; i++)
    {
        for (int j = 0; j < t; j++)
        {
            dp[i + j][j] = max(dp[i + j - 2][j], dp[i + j - 3][j]) + money[i + j];
            m = max(m, dp[i + j][j]);
        }
    }
    for (int j = 0; j < 2; j++)
    {
        dp[L - 2 + j][j] = max(dp[L - 2 + j - 2][j], dp[L - 2 + j - 3][j]) + money[L - 2 + j];
        m = max(m, dp[L - 2 + j][j]);
    }

    return m;
}
```

통과. Python 효율성 테스트는 시간을 좀 더 넉넉하게 수정해야 할듯?  

아니면 Python으로도 효율성 테스트 통과하신 분이 있다면 메일 주시면 감사하겠습니다.
