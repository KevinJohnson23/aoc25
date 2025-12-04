#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct range {
    unsigned long long start;
    unsigned long long end;
};

struct range* parse_input(char *file_name, int *num_lines) {
    FILE *fptr = fopen(file_name, "r");

    unsigned long long start;
    unsigned long long end;
    while (fscanf(fptr, "%llu-%llu,", &start, &end) != EOF) {
        (*num_lines)++;
    }

    rewind(fptr);
    struct range* ranges = malloc(sizeof(struct range) * *num_lines);
    for (int i = 0; i < *num_lines; i++) {
        fscanf(fptr, "%llu-%llu,", &start, &end);
        ranges[i].start = start;
        ranges[i].end = end;
    }

    fclose(fptr);
    return ranges;
}

int is_repeating1(unsigned long long n) {
    int exp = 0;
    unsigned long long n_temp = n;
    while (n_temp) {
        n_temp /= 10;
        exp += 1;
    }
    if (exp % 2 == 1) {
        return 0;
    }
    unsigned long long exp10 = pow(10, exp/2);
    return n % exp10 == n / exp10;
}

int is_repeating2(unsigned long long n) {
    int exp = 0;
    unsigned long long n_temp = n;
    while (n_temp) {
        n_temp /= 10;
        exp += 1;
    }
    for (int i = 1; i <= exp/2; i++) {
        if (exp % i != 0) {
            continue;
        }
        n_temp = n;
        unsigned long long cur_exp = pow(10, i);
        unsigned long long to_match = n_temp % cur_exp;
        int found_match = 1;
        while (n_temp) {
            unsigned long long cur = n_temp % cur_exp;
            n_temp /= cur_exp;
            if (cur != to_match) {
                found_match = 0;
                break;
            }
        }
        if (found_match) {
            return 1;
        }
    }
    return 0;
}

unsigned long long part1(char *file_name) {
    int num_lines = 0;
    struct range* ranges = parse_input(file_name, &num_lines);
    unsigned long long ans = 0;
    for (int i = 0; i < num_lines; i++) {
        for (unsigned long long j = ranges[i].start; j <= ranges[i].end; j++) {
            if (is_repeating1(j)) {
                ans += j;
            }
        }
    }
    free(ranges);
    return ans;
}

unsigned long long part2(char *file_name) {
    int num_lines = 0;
    struct range* ranges = parse_input(file_name, &num_lines);
    unsigned long long ans = 0;
    for (int i = 0; i < num_lines; i++) {
        for (unsigned long long j = ranges[i].start; j <= ranges[i].end; j++) {
            if (is_repeating2(j)) {
                ans += j;
            }
        }
    }
    free(ranges);
    return ans;
}

int main() {
    printf("%llu\n", part1("input.txt"));
    printf("%llu\n", part2("input.txt"));
}