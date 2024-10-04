// COPYRIGHT (c) 2024 Massonskyi
// All rights reserved.
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
// 1. Redistributions of source code must retain the above copyright notice,
//    this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
// 3. Neither the name of the copyright holder nor the names of its contributors
//    may be used to endorse or promote products derived from this software
//    without specific prior written permission.
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED И НА ЛЮБОЙ ТЕОРИИ ОТВЕТСТВЕННОСТИ, НЕЗАВИСИМО ОТ ТОГО, В КОНТРАКТЕ, СТРОГОЙ ОТВЕТСТВЕННОСТИ ИЛИ ДЕЛИКТЕ (ВКЛЮЧАЯ НЕБРЕЖНОСТЬ ИЛИ ИНАЧЕ) ВОЗНИКАЮЩИЕ ЛЮБОЙ СПОСОБ ИЗ ИСПОЛЬЗОВАНИЯ ЭТОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ДАЖЕ ЕСЛИ СОВЕТУЕТСЯ ВОЗМОЖНОСТЬ ТАКОГО УЩЕРБА.

#ifndef ARM_TIMER_HPP
#define ARM_TIMER_HPP

#include <chrono>
#include <functional>
#include <thread>
#include <atomic>
#include <vector>
#include <iostream>

class ArmTimer {
public:
    using Clock = std::chrono::high_resolution_clock;
    using TimePoint = std::chrono::time_point<Clock>;

    ArmTimer(double interval, std::function<void()> callback, bool single_shot = false)
        : interval(interval), callback(std::move(callback)), single_shot(single_shot), stop_flag(false) {}

    void setInterval(double new_interval) {
        interval = new_interval;
    }

    void start() {
        if (timer_thread.joinable()) {
            stop();
        }
        stop_flag.store(false);
        timer_thread = std::thread(&ArmTimer::run, this);
    }

    void stop() {
        stop_flag.store(true);
        if (timer_thread.joinable()) {
            timer_thread.join();
        }
    }

    ~ArmTimer() {
        stop();
    }

private:
    void run() {
        auto next_call = Clock::now();
        while (!stop_flag.load()) {
            next_call = next_call + std::chrono::duration_cast<Clock::duration>(std::chrono::duration<double>(interval));
            std::this_thread::sleep_until(next_call);
            if (stop_flag.load()) break;
            callback();
            if (single_shot) break;
        }
    }

    double interval;
    std::function<void()> callback;
    bool single_shot;
    std::atomic<bool> stop_flag;
    std::thread timer_thread;
};

#endif // ARM_TIMER_HPP