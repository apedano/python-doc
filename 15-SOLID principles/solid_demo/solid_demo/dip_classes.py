from abc import ABC, abstractmethod

class ServiceInterface(ABC):
    @abstractmethod
    def execute_service(self):
        pass

class ServiceFactoryInterface(ABC):
    @abstractmethod
    def create_service(self):
        pass

class Application():
    def __init__(self,
                 service_factory: ServiceFactoryInterface):
        self.__service: ServiceInterface = service_factory.create_service()

    def do_operation_using_service(self):
        return self.__service.execute_service()

class ServiceImpl(ServiceInterface):
    def execute_service(self):
        return "executing service implementation"

class ServiceImplFactory(ServiceFactoryInterface):
    def create_service(self):
        return ServiceImpl()










