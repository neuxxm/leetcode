//00:49-00:58
char * reverseVowels(char * s){
    int n = strlen(s);
    int z[100005];
    int ix = 0;
    for (int i=0; i<n; ++i) {
        char c = s[i];
        if (strchr("aeiouAEIOU", c)) {
            z[ix++] = i;
        }
    }
    int l = ix;
    for (int i=0; i<l/2; ++i) {
        int j = z[i];
        int j2 = z[l-1-i];
        char t = s[j];
        s[j] = s[j2];
        s[j2] = t;
    }
    return s;
}
