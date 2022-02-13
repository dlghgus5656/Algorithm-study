import java.util.Scanner;
// Scanner 사용을 위해서 java.util.Scaaner 클래스를 import 한다.
public class A곱하기B {
// 백준에서는 class 명으로 Main을 사용해야한다.
	public static void main(String[] args) {
	// main 메소드를 메모리에 항상 상주하고 리턴값이 없게 선언한다.
		Scanner sc = new Scanner(System.in);
		// 데이터를 입력받기 위해서 Scanner 객체 sc를 선언한다.
		int num1 = sc.nextInt();
		// int형 변수 num1에 값을 입력받는다.
		int num2 = sc.nextInt();
		// int형 변수 num2에 값을 입력받는다.
		sc.close();
		// 더 이상 사용하지 않는 객체 sc를 종료한다.
		int num3 = num1 * num2;
		/* 변수 num1과 변수 num2에 들어있는 값을 곱한 후
		변수 num3에 그 값을 저장한다.*/
		System.out.println(num3);
		// 변수 num3에 저장되어 있는 값을 출력한다.
	}
}