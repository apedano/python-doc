from solid_demo.isp_classes import WrongService1,WrongIndependentService, Service


def test_isp_violation():
    wrong_service_1: WrongService1 = WrongService1(WrongIndependentService())
    actual = wrong_service_1.do_operation()
    assert actual == "operation1 at wrong service name"

