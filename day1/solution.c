#include <stdio.h>
#include <stdlib.h>

int* parse_input(char *file_name, int *num_lines) {
    FILE *fptr = fopen(file_name, "r");

    char dir;
    int num;
    while (fscanf(fptr, "%c%d\n", &dir, &num) != EOF) {
        (*num_lines)++;
    }

    rewind(fptr);
    
    int *input = malloc(sizeof(int) * *num_lines);
    for (int i = 0; i < *num_lines; i++) {
        fscanf(fptr, "%c%d\n", &dir, &num);
        if (dir == 'L') {
            num *= -1;
        }
        input[i] = num;
    }
    fclose(fptr);
    return input;
}

int part1(char *file_name) {
    int num_lines = 0;
    int *input = parse_input(file_name, &num_lines);

    int ans = 0;
    int dial = 50;
    for (int i = 0; i < num_lines; i++) {
        dial += input[i];
        dial = (dial % 100 + 100) % 100;
        if (dial == 0) {
            ans += 1;
        }
    }
    return ans;
}

int part2(char *file_name) {
    int num_lines = 0;
    int *input = parse_input(file_name, &num_lines);

    int ans = 0;
    int dial = 50;
    for (int i = 0; i < num_lines; i++)
    {
        int num = input[i];
        int dir = 1;
        if (num < 0) {
            num *= -1;
            dir = -1;
        }
        for (int j = 0; j < num; j++) {
            dial += dir;
            if (dial == -1) {
                dial = 99;
            } else if (dial == 100) {
                dial = 0;
            }
            if (dial == 0) {
                ans += 1;
            }
        }
    }
    return ans;
}

int main() {

    printf("%d\n", part1("input.txt"));
    printf("%d\n", part2("input.txt"));

    return 0;
}