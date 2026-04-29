#include <iostream>
#include <thread>
#include <chrono>

int main() {
    for (int i = 0; i < 5; i++) {
        std::cout << "Client message " << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    return 0;
}
