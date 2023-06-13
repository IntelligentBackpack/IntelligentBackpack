from python.domainModel.domainServices.BackpackLogic import BackpackLogicService
from python.application.serviceLocator.backpack_service_locator import ServiceLocator


if __name__ == "__main__":

    serviceLocator = ServiceLocator()
    queue_messages = serviceLocator.get_messages_queue()
    domainLogic = BackpackLogicService(serviceLocator.repository)

    try:

        for module in serviceLocator.get_modules():
            module.start()

        while(True):
            request = queue_messages.get()
            if request == "EXIT":
                raise KeyboardInterrupt()
            elif request["type"] is not None:
                if request["type"] == "REGISTER":
                    print("REGISTRATO")
                    domainLogic.register(request["payload"]["email"])
                if request["type"] == "UNREGISTER":
                    domainLogic.unregister()
                if request["type"] == "TAG_READ":
                    domainLogic.manage_element("", request["payload"])

    except KeyboardInterrupt:
        # Exit application because user indicated they wish to exit.
        # This will have cancelled `main()` implicitly.
        print("EXIT")
