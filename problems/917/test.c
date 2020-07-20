//17:41AC
char * reverseOnlyLetters(char * S){
    char *s = S;
    int n = strlen(s);
    int l = 0;
    int r = n-1;
    while ( l < r ) {
        if (isalpha(s[l])) {
            if (isalpha(s[r])) {
                char c = s[l];
                s[l] = s[r];
                s[r] = c;
                l += 1;
                r -= 1;
            }
            else {
                r -= 1;
            }
        }
        else {
            l += 1;
        }
    }
    return s;
}
