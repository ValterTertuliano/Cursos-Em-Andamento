import java.util.Scanner;

public class aula_11c {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.print("Digite um numero para calcular Fatorial: ");
        int n = num.nextInt();
        long fatorial = 1;
        int contador = n;
        
        while (contador>=1) {
            //5! = 5 x 4 x 3 x 2 x 1
            fatorial *=  contador;
            contador--;

            
        }
        System.out.println(fatorial);
        num.close();
    }
}
