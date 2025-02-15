import java.util.Scanner;

public class aula_10 {
    public static void main(String[] args) {
        
        System.out.print("Digite ano de nascimento: ");
        
        Scanner teclado = new Scanner(System.in);
        int ano = teclado.nextInt();

        int idade = 2025 - ano;
        
        if (idade < 16){
            System.out.println("Menor de Idade, probido votar. ");

        } else if (idade >= 18 && idade <= 70) {
            System.out.println("Maior de 18 e menor que 70, voto Obrigatorio. ");
        } else {
            System.out.println("Idade entre 16 e 17, ou maior que 70, voto Opcional. ");
            
        }
        teclado.close();
    }    
}
