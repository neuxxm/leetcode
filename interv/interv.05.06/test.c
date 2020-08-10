//2:14fail
void f(unsigned int n, int a[]) {
    int i = 0;
    while (n!=0) {
        a[i++] = n&1;
        n >>= 1;
    }
    while (i < 32) {
        a[i++] = 0;
    }
}
int convertInteger(int A, int B){
    int a[32] = {0};
    int b[32] = {0};
    f(A, a);
    f(B, b);
    int z = 0;
    for (int i=0; i<32; ++i) {
        if (a[i] != b[i]) {
            z += 1;
        }
    }
    return z;
}
