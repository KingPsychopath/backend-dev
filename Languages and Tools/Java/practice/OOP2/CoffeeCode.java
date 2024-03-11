package practice.OOP2;

class CoffeeCode {
    // Step 1: Define the component interface
interface Coffee {
    String getDescription();
    double getCost();
}

// Step 2: Implement concrete components
class SimpleCoffee implements Coffee {
    @Override
    public String getDescription() {
        return "Simple Coffee";
    }

    @Override
    public double getCost() {
        return 1;
    }
}



// Step 3: Implement the decorator
abstract class CoffeeDecorator implements Coffee {
    protected final Coffee decoratedCoffee;

    public CoffeeDecorator(Coffee c) {
        this.decoratedCoffee = c;
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription();
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost();
    }
}

// Step 4: Implement concrete decorators
public class WithMilk extends CoffeeDecorator {
    public WithMilk(Coffee c) {
        super(c);
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", with milk";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.5;
    }
}

public class WithSugar extends CoffeeDecorator {
    public WithSugar(Coffee c) {
        super(c);
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", with sugar";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.2;
    }
}

// Step 5: Use the decorators
public class Main {
    public static void main(String[] args) {
        Coffee c = new SimpleCoffee();
        c = new WithMilk(c);
        c = new WithSugar(c);

        Coffee simpleCoffee = new SimpleCoffee();
        Coffee coffeeWithMilk = new WithMilk(simpleCoffee);
        Coffee coffeeWithSugar = new WithSugar(simpleCoffee);

        System.out.println(c.getDescription() + " : " + c.getCost());
    }
}
}
