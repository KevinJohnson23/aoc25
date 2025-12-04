#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STRLEN 100

char** parse_input(char *file_name, int *num_lines) {
    FILE *fptr = fopen(file_name, "r");
    char line[STRLEN+1];
    while (fscanf(fptr, "%s\n", line) != EOF) {
        (*num_lines)++;
    }
    rewind(fptr);
    char **input = malloc(sizeof(char*) * (*num_lines));
    for (int i = 0; i < *num_lines; i++) {
        fscanf(fptr, "%s\n", line);
        line[STRLEN] = '\0';
        input[i] = strdup(line);
    }
    fclose(fptr);
    return input;
}

unsigned long long find_largest(char num[], int k) {
    unsigned long long largest = 0;
    int prev = -1;
    printf("%s\n", num);
    for (int i = 0; i < k; i++) {
        int cur = prev+1;
        char cur_digit = num[cur];
        for (int j = prev+1; j <= strlen(num)-(k-i)+1; j++) {
            char digit = num[j];
            if (digit > cur_digit) {
                cur = j;
                cur_digit = digit;
            }
        }
        printf("%d %c %d\n", cur, cur_digit, (int)cur_digit);
        largest *= 10;
        largest += cur_digit-48;
        prev = cur;
    }
    printf("%llu\n", largest);
    return largest;
}

unsigned long long part1(char *file_name) {
    unsigned long long ans = 0;
    int num_lines = 0;
    char **input = parse_input(file_name, &num_lines);
    for (int i = 0; i < num_lines; i++) {
        ans += find_largest(input[i], 2);
    }
    return ans;
}

int main() {
    printf("%llu\n", part1("test.txt"));
}