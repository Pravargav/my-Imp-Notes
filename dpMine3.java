getAns(0, 0) [Start]
├── getAns(1, 0) [Skip buying]
│   ├── getAns(2, 0) [Skip buying]
│   │   ├── getAns(3, 0) [Skip buying]
│   │   │   ├── getAns(4, 0) = 0 [Base Case]
│   │   │   └── getAns(4, 1) = -5 [Base Case]
│   │   │   Result = max(0, -5) = 0 return Result;
│   │   └── getAns(3, 1) [Buy at 6]
│   │       ├── getAns(4, 1) = 0 [Base Case]
│   │       └── getAns(4, 0) = 5 [Sell at 5]
│   │       Result = max(0, 5) = 5 return Result;
│   │   Result = max(0, -6 + 5) = 0 return Result;
│   └── getAns(2, 1) [Buy at 2]
│       ├── getAns(3, 1) [Skip selling]
│       │   ├── getAns(4, 1) = 0 [Base Case]
│       │   └── getAns(4, 0) = 5 [Sell at 5]
│       │   Result = max(0, 5) = 5 return Result;
│       └── getAns(3, 0) [Sell at 6]
│           ├── getAns(4, 0) = 0 [Base Case]
│           └── getAns(4, 1) = -5 [Base Case]
│           Result = max(0, -5) = 0 return Result;
│       Result = max(5, 6 + 0) = 6 return Result;
│   Result = max(0, -2 + 6) = 4 return Result;
├── getAns(1, 1) [Buy at 3]
│   ├── getAns(2, 1) [Skip selling]
│   │   ├── getAns(3, 1) [Skip selling]
│   │   │   ├── getAns(4, 1) = 0 [Base Case]
│   │   │   └── getAns(4, 0) = 5 [Sell at 5]
│   │   │   Result = max(0, 5) = 5 return Result;
│   │   └── getAns(3, 0) [Sell at 6]
│   │       ├── getAns(4, 0) = 0 [Base Case]
│   │       └── getAns(4, 1) = -5 [Base Case]
│   │       Result = max(0, -5) = 0 return Result;
│   │   Result = max(5, 6 + 0) = 6 return Result;
│   └── getAns(2, 0) [Sell at 2]
│       ├── getAns(3, 0) [Skip buying]
│       │   ├── getAns(4, 0) = 0 [Base Case]
│       │   └── getAns(4, 1) = -5 [Base Case]
│       │   Result = max(0, -5) = 0 return Result;
│       └── getAns(3, 1) [Buy at 6]
│           ├── getAns(4, 1) = 0 [Base Case]
│           └── getAns(4, 0) = 5 [Sell at 5]
│           Result = max(0, 5) = 5  return Result;
│       Result = max(0, -6 + 5) = 0  return Result;
│   Result = max(6, 2 + 0) = 6  return Result;
Result = max(4, -3 + 6) = 6 return Result;


long getAns(long *Arr, int ind, int buy, int n, vector<vector<long>> &dp) {
    // Base case: When we reach the end of the array, there are no more decisions to make.
    if (ind == n) {
        return 0;
    }

    // If the result for this state has already been calculated, return it
   

    long Result = 0;

    if (buy == 0) { // We can buy the stock
        Result = max(0 + getAns(Arr, ind + 1, 0, n, dp), -Arr[ind] + getAns(Arr, ind + 1, 1, n, dp));
    }

    if (buy == 1) { // We can sell the stock
        Result = max(0 + getAns(Arr, ind + 1, 1, n, dp), Arr[ind] + getAns(Arr, ind + 1, 0, n, dp));
    }

    // Store the calculated profit in the DP table and return it
    return  Result;
}
