package lab03;

public class LowerCaseTester {

	public static void main(String[] args) {
		String greeting = "This is a Test";
		String testString = greeting;
		String smallTestString = greeting.toLowerCase();
		System.out.println(smallTestString);
		
		String bigTestString = smallTestString.toUpperCase();
		System.out.println(bigTestString);

	}

}
