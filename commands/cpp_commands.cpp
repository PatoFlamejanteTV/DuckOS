#include <iostream>
#include <fstream>
#include <string>

extern "C" {

void cppls() {
    system("ls");
}

void cppcat(const char* filename) {
    std::ifstream file(filename);
    if (file.is_open()) {
        std::string line;
        while (getline(file, line)) {
            std::cout << line << std::endl;
        }
        file.close();
    } else {
        std::cerr << "File '" << filename << "' not found." << std::endl;
    }
}

void cpptouch(const char* FILENAME, const char* CONTENT) {
    std::ofstream file(FILENAME);
    file << CONTENT;
    file.close();
}

} // extern "C"