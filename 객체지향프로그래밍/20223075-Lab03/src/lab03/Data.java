package lab03;

public class Data {
	public static void main(String[] args) {
		int num1 = 40, num2 = 65, x = 99;
		float num3 = 18.53f;
		char letter = 'x';
		num1 = 777;
		double num4 = num1;
		Boolean flag = false;
		final int FIXED = 2020; // 상수 선언 final 데이터타입 상수이름 = 초기화;
		// FIXED = 3030;
		// num1 = flag;
		System.out.println("The value of num1: " + num1);
		System.out.println("The value of num3: " + num3);
		System.out.println("The value of x: " + x);
		System.out.println("The letter x: " + letter);
		System.out.println("The value of num4: " + num4);
		System.out.println("The value of flag: " + flag);
		System.out.println("The value of FIXED: " + FIXED);
	}
}
