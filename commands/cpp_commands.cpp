#include <iostream>
#include <fstream>
#include <string>

extern "C" {

void cpp_list_files() {
    system("ls");
}

void cpp_show_file_content(const char* filename) {
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

void writefile(const char* FILENAME, const char* CONTENT) {
    std::ofstream file(FILENAME);
    file << CONTENT;
    file.close();
}

} // extern "C"