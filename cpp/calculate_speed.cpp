// calculate_speed.cpp
#include <iostream>
#include <iomanip> // for fixed and setprecision

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: ./calculate_speed <distance_km> <time_seconds>" << std::endl;
        return 1;
    }

    double distance_km = std::stod(argv[1]);
    double time_sec = std::stod(argv[2]);

    if (time_sec == 0) {
        std::cerr << "Time cannot be zero." << std::endl;
        return 1;
    }

    double speed_km_per_sec = distance_km / time_sec;
    double speed_m_per_sec = speed_km_per_sec * 1000;

    std::cout << std::fixed << std::setprecision(4)
              << speed_km_per_sec << " " << speed_m_per_sec << std::endl;

    return 0;
}