/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
//19:21-19:24
void f(int *a, int x, int y, int n) {
    if (x == y) {
        return;
    }
    if (x+1 == y) {
        return;
    }
    int *b = (int*) malloc(sizeof(int) * (y-x+1));
    int k = 0;
    for (int i=x; i<=y; i+=2) {
        b[k++] = a[i];
    }
    for (int i=x+1; i<=y; i+=2) {
        b[k++] = a[i];
    }
    memcpy(a+x, b, sizeof(int)*(y-x+1));
    int m = (x+y) / 2;
    f(a, x, m, n);
    f(a, m+1, y, n);
}
int* beautifulArray(int N, int* returnSize){
    // 1 2 3 4 5 6 7
    // 1 3 5 7 2 4 6 8
    // 1 5 3 7 2 6 4 8
    int n = N;
    int *a = (int*) malloc(sizeof(int) * n);
    for (int i=0; i<n; ++i) {
        a[i] = i+1;
    }
    f(a, 0, n-1, n);
    *returnSize = n;
    return a;
}
