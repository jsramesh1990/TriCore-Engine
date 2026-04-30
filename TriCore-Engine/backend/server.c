#include <stdio.h>
#include <unistd.h>

int main() {
    int tick = 0;
    printf("Server listening on port 8080...\n");
    fflush(stdout);
    
    while(1) {
        printf("Server tick %d\n", tick++);
        fflush(stdout);
        sleep(2);
    }
    return 0;
}
