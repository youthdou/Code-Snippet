#ifndef SNIPPET_H
#define SNIPPET_H


#ifdef WIN32
#include <Windows.h>
#include <Psapi.h>

#pragma comment(lib, "Psapi.lib")
#endif

class MemoryConsumption {
public:
    MemoryConsumption()
    {
        m_iLastMem = getCurrentMemory();
    }

    double consume()
    {
        return getCurrentMemory() - m_iLastMem;
    }

    void start()
    {
        m_iLastMem = getCurrentMemory();
    }

private:
    double getCurrentMemory()
    {
#ifdef WIN32
        PROCESS_MEMORY_COUNTERS memcount;
        if (!GetProcessMemoryInfo(GetCurrentProcess(), &memcount, sizeof(memcount)))
        {
            return 0;
        }

        return memcount.WorkingSetSize / (1024 * 1024);
#else
        return 0;
#endif
    }

private:
    double m_iLastMem; //MB
};

#include <chrono>

class ElapsedTimer
{
public:
    ElapsedTimer()
    {
        m_startTime = std::chrono::steady_clock::now();
    }

    void start()
    {
        m_startTime = std::chrono::steady_clock::now();
    }

    //unit: ms
    double elpased()
    {
        if(m_startTime == std::chrono::steady_clock::time_point())
        {
            return 0;
        }
        std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
        std::chrono::duration<double, std::milli> elapsed = end - m_startTime;
        return elapsed.count();
    }

private:
    std::chrono::steady_clock::time_point m_startTime;
};

#endif // SNIPPET_H
