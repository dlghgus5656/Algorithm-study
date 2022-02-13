import java.util.Scanner;
/* 입력 클래스인 Scanner를 사용하기 위해서 Scanner가
속해잇는 클래스인 java.util.Scanner를 import 해준다. */

public class A더하기B {
    public static void main(String[] args) {
    	// 자바 main 함수를 리턴값이 없이 메모리에 항상 상주하게 선언
		Scanner sc = new Scanner(System.in);
		// Scanner 클래스를 사용하기 위해서 객체를 생성해 준다.
		int num1 = sc.nextInt();
		// 입력받은 정수를 변수 num1에 저장한다.
		int num2 = sc.nextInt();
		// 입력받은 정수를 변수 num2에 저장한다.
		sc.close();
		// Scanner sc 객체를 종료해준다.
		int num3 = num1 + num2;
		// 변수 num1값과 num2값을 덧셈한후 변수 num3에 저장한다.
		System.out.print(num3);
		// 변수 num3에 저장된 값을 출력한다.
		}
}