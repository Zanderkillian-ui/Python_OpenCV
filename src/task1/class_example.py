#!/usr/bin/env python3

# Think of class as a Car. Each Car has some properties and functionalities.
# Here I am creating a music class, with some fixed and variable properties.
# And some functionality, that can be called to do various things
class Music:
    # Methods are functions defined within a class. You can have as many
    # class methods as required. This class have three methods: __init__, volume, bass

    # The __init__ method is a special method. It is also called the constructor method.
    # In professional Object-Oriented-Programming, it is recommended to include this method in
    # class definition. This method is called as soon as an object of the class is created. 
    # This is mostly used for initialization of class variable and calling initialization
    # method, if any, which are required in further logic of the code.

    # A normal function can take various arguments. These arguments acts as a source to change the
    # value of any class variables. self, is a special argument, that is used in Object-Oriented-Programming.
    # Every method of a class must have this argument, even if it doesn't require. When calling a class method,
    # you don't have to pass any value for this argument. One other way, of thinking about self is, this is a struct,
    # and if you want to define to class variable that cab ne accessesible from any class method, you need to,'
    # add that variable as a field of this struct.
    def __init__(self):
        # Now button can be accessd from any method in the class
        self.button = False

    def volume(self, level):
        # This method takes an external argument 'level'
        print(f"Adjusting volume to: {level}")

    def bass(self, boost_level):
        # This method uses 'self' to check if it's even allowed to run
        if self.button:
            print(f"Bass boosted to {boost_level}!")
        else:
            print("Cannot adjust bass. The system is OFF.")

    def toggle_power(self):
        # This switches the state of our attribute
        self.button = not self.button
        status = "ON" if self.button else "OFF"
        print(f"Power toggled. System is now {status}.")


# This is a function not a class method, meaning this is not a part of the class. Well, you can use a different name, but
# The recommended name for this function is main. This hold the main high level logic that gets executed when this
# python file is called
def main():
    # Think of an object of the class as BMW i8, which is a car.
    # Here I created my_music object
    # Now I can set the volume and bass of my_music
    my_music = Music()
    # As soon as I created the object, the __init__ method is called and the button variable get set to False.
    # Now set the button to true
    my_music.toggle_power()
    # Set volume level
    my_music.volume(15)
    # Set the base
    my_music.bass(10)


# Call the main function
if __name__ == "__main__":
    main()