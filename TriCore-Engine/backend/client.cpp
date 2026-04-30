#include <iostream>
#include <thread>
#include <chrono>

int main() {
    int msg = 0;
    std::cout << "Client connected to server..." << std::endl;
    
    while(1) {
        std::cout << "Client message " << msg++ << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    return 0;
}
