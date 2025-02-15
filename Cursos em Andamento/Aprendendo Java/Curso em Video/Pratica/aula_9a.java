import java.util.Scanner;

public class aula_9a {
    public static void main(String[] args) {

        // iniciando scanner
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o ano de nascimento: ");
        int ano = teclado.nextInt();
        int idade = 2025 - ano;
        if (idade >= 18){
            System.out.println("Maior de Idade.");
        } else {
            System.out.println("Menor de Idade. ");
        }

        teclado.close();
    }
}
