import os

def generate_cmake_script():
    with open("CMakeLists.txt", "w") as cmake_file:
        cmake_file.write("cmake_minimum_required(VERSION 3.10)\n")
        cmake_file.write("project(MyProject)\n\n")
        
        cmake_file.write("set(CMAKE_CXX_STANDARD 11)\n\n")
        
        cmake_file.write("# Add Raylib library\n")
        cmake_file.write("add_subdirectory(raylib)\n\n")
        
        cmake_file.write("# Add Raygui library\n")
        cmake_file.write("add_subdirectory(raygui)\n\n")
        
        cmake_file.write("# Add your source files here\n")
        cmake_file.write("add_executable(MyApp main.cpp)\n\n")
        
        cmake_file.write("# Link Raylib and Raygui libraries\n")
        cmake_file.write("target_link_libraries(MyApp PUBLIC raylib raygui)\n")

def install_dependencies():
    os.system("git clone https://github.com/raysan5/raylib.git")
    os.system("cd raylib/src && make && sudo make install")
    
    os.system("git clone https://github.com/raysan5/raygui.git")
    os.system("cd raygui/src && make && sudo make install")

if __name__ == "__main__":
    generate_cmake_script()
    install_dependencies()
