package lab03;

import java.util.Scanner;

public class BasicIO {

	public static void main(String[] args) {
		Scanner stdin = new Scanner(System.in);
		
		System.out.print("Enter date: ");
		int year = stdin.nextInt();
		int month = stdin.nextInt();
		int day = stdin.nextInt();
		
		System.out.print("Enter your name: ");
		String name = stdin.next();
		
		System.out.print("Enter your years: ");
		String years = stdin.next();
		int years_ = Integer.parseInt(years);
		
		System.out.print("Enter your height: ");
		int height = stdin.nextInt();
		
		System.out.println("your name is " + name);
		System.out.println("Your years is " + years);
		System.out.println("Years to day: " + (years_ * 365));
		System.out.println("Your height is " + height);
		System.out.printf("%d년 %d월 %d일 현재 홍길동(%d)의 키는 %dcm 입니다.", year, month, day, years_, height);
	}
}
