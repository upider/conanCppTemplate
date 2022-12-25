#include <iostream>

#include <spdlog/spdlog.h>

int main() {
    SPDLOG_INFO("{} {}", "Hello", "World");
    std::cout << "Hello, world!\n";
}
