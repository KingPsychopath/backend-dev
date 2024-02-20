In Java, the decorator pattern is a design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. It is a structural pattern that involves a set of decorator classes that are used to wrap concrete classes.

Here's a simple example of how to use the decorator pattern in Java:

In this example, `Coffee` is the component interface, `SimpleCoffee` is a concrete component, `CoffeeDecorator` is the decorator, and `WithMilk` and `WithSugar` are concrete decorators. The `Main` class shows how to use the decorators to add behavior to a `SimpleCoffee` object.