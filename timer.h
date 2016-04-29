#pragma once
#include "Poco/Timer.h"
#include "Poco/Stopwatch.h"

#ifdef WIN32
    #define POCO_TIMER_EXPORT __declspec(dllexport)
#else
    #define POCO_TIMER_EXPORT
#endif

using Poco::Timer;
using Poco::Stopwatch;

class POCO_TIMER_EXPORT TimerExample{
public:
    TimerExample(){ _sw.start();}
    void onTimer(Timer& timer);
private:
    Stopwatch _sw;
};
