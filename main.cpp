#include "timer.h"

using Poco::TimerCallback;
using Poco::Thread;

int main(int argc, char** argv){
    TimerExample example;
    Timer timer(250, 500);
    timer.start(TimerCallback<TimerExample>(example, &TimerExample::onTimer));

    Thread::sleep(5000);
    timer.stop();
    return 0;
}
