#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <sstream>
#include "../include/core.h"

namespace py = pybind11;

PYBIND11_MODULE(gt_wrapper, m) {
    m.doc() = "Python bindings for ARM optimized C++ library";
    // ArmRetryParams

    py::class_<ArmSignal>(m, "ArmSignal")
        .def(py::init<>())
        .def("connect", &ArmSignal::connect)
        .def("disconnect", &ArmSignal::disconnect)
        .def("emit", &ArmSignal::emit);

    // ArmTimer
    py::class_<ArmTimer>(m, "ArmTimer")
        .def(py::init<double, std::function<void()>, bool>(), py::arg("interval"), py::arg("callback"), py::arg("single_shot") = false)
        .def("setInterval", &ArmTimer::setInterval)
        .def("start", &ArmTimer::start)
        .def("stop", &ArmTimer::stop);
}