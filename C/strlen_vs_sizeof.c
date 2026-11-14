#include <stdio.h>
#include <string.h>
int main() {
    int N;
    printf("Enter number of test cases: ");
    scanf("%d", &N);
    while (N--) {
        char s[105];
        printf("Enter a string: ");
        scanf("%s", s);

        int line_strlen = 0;
        int line_sizeof = 0;
        int found_first_null = 0;
        int len = strlen(s);
        for (int i = 0; i < len; i++) {
            if (s[i] == '\\' && i + 1 < len && s[i+1] == '0') {
                line_sizeof++;
                found_first_null = 1;
                i++;
            } else {
                line_sizeof++;
                if (found_first_null == 0) {
                    line_strlen++;
                }
            }
        }
        line_sizeof++;
        printf(" %d %d\n", line_sizeof, line_strlen);
    }
return 0;
}
