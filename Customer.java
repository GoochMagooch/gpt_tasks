public class Customer {
    String name;
    String email;

    public Customer(String name, String email) {
	this.name = name;
	this.email = email;
    }

    public static void format(String name, String email) {
	System.out.println("Customer Name: " + this.name + ", Email: " + this.email);
    }
    
    public static void main(String[], args) {
	
	Customer rochelle = new Customer("Rochelle Williams", "rochelle@gmail.com");
	Customer sally = new Customer("Sally Mitchell", "sally@gmail.com");

	sally.format();
	rochelle.format();

    }

}
