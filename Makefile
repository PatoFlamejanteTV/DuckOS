# Variables
CXX = g++
CXXFLAGS = -shared -fPIC
TARGET = cpp_commands.so # It should be on the same directory as main.py
SRC = commands/cpp_commands.cpp

# Default target
all: $(TARGET)

# Compile C++ shared library
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $<

# Clean up build files
clean:
	rm -f $(TARGET)

.PHONY: all clean