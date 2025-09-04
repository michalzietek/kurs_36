from abc import ABC, abstractmethod

# class LedLamp:
#     def __init__(self):
#         self.turned_on = False
#
#     def turn_on(self):
#         self.turned_on = True
#         print("Wlaczamy nasza lampe")
#
#     def turn_off(self):
#         self.turned_on = False
#         print("Wyłączamy naszą lampę")
#
#
# class KsenonLamp:
#     def __init__(self):
#         self.turned_on = False
#
#     def turn_on(self):
#         self.turned_on = True
#         print("Wlaczamy nasza lampe")
#
#     def turn_off(self):
#         self.turned_on = False
#         print("Wyłączamy naszą lampę")
#
# class TV:
#     def __init__(self):
#         self.turned_on = False
#
#     def turn_on(self):
#         self.turned_on = True
#         print("Wlaczamy nasz telewizor")
#
#     def turn_off(self):
#         self.turned_on = False
#         print("Wyłączamy nasz telewizor")
#
# class LedLampSwitch:
#     def __init__(self):
#         self.lamp = LedLamp()
#
#     def switch(self):
#         if not self.lamp.turned_on:
#             return self.lamp.turn_on()
#         else:
#             return self.lamp.turn_off()
#
# class KsenonLightSwitch:
#     def __init__(self):
#         self.lamp = KsenonLamp()
#
#     def switch(self):
#         if not self.lamp.turned_on:
#             return self.lamp.turn_on()
#         else:
#             return self.lamp.turn_off()
#
# class RemoteController:
#     def __init__(self):
#         self.tv = TV()
#
#     def switch(self):
#         if not self.tv.turned_on:
#             return self.tv.turn_on()
#         else:
#             return self.tv.turn_off()

class Switchable(ABC):
    def __init__(self):
        self.turned_on = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LedLamp(Switchable):
    def turn_on(self):
        self.turned_on = True
        print("Wlaczamy nasza lampe")

    def turn_off(self):
        self.turned_on = False
        print("Wyłączamy naszą lampę")


class KsenonLamp(Switchable):
    def turn_on(self):
        self.turned_on = True
        print("Wlaczamy nasza lampe")

    def turn_off(self):
        self.turned_on = False
        print("Wyłączamy naszą lampę")

class TV(Switchable):
    def turn_on(self):
        self.turned_on = True
        print("Wlaczamy nasz telewizor")

    def turn_off(self):
        self.turned_on = False
        print("Wyłączamy nasz telewizor")

class Switch:
    def __init__(self, switchable: Switchable):
        self.switchable = switchable

    def switch_light(self):
        if not self.switchable.turned_on:
            self.switchable.turn_on()
        else:
            self.switchable.turn_off()