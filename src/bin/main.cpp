#include <iostream>

#include <spdlog/spdlog.h>

#include "hello/hello.hpp"

int main() {
    SPDLOG_INFO("{} {}", "Hello", "World");
    hello();
}
