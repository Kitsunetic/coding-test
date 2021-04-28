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
