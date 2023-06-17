from python.domainModel.domainServices.BackpackLogic import BackpackLogicService
from python.application.serviceLocator.backpack_service_locator import ServiceLocator
from python.application.serviceLocator.backpack_service_locator import CONFIG_FILE_PATH
from python.application.preferences.preferences_utils import write_username


if __name__ == "__main__":

    serviceLocator = ServiceLocator()
    queue_messages = serviceLocator.get_messages_queue()
    domainLogic = BackpackLogicService(serviceLocator.repository)
    domainLogic.register(serviceLocator.get_username())
    serviceLocator.repository.sync_remote()

    try:

        for module in serviceLocator.get_modules():
            module.start()

        while True:
            request = queue_messages.get()
            if request == "EXIT":
                raise KeyboardInterrupt()
            elif request["type"] is not None:
                if request["type"] == "REGISTER":
                    print("REGISTRATO")
                    name = request["payload"]["email"]
                    write_username(CONFIG_FILE_PATH, name)
                    domainLogic.register(name)
                if request["type"] == "UNREGISTER":
                    write_username(CONFIG_FILE_PATH, "")
                    domainLogic.unregister()
                if request["type"] == "TAG_READ":
                    domainLogic.manage_element("", request["payload"])

    except KeyboardInterrupt:
        print("EXIT")
