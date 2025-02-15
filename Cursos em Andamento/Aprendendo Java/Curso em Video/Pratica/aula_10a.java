import java.util.Scanner;

public class aula_10a {
    public static void main(String[] args) {
    
        Scanner teclado = new Scanner(System.in);
        System.out.print("Informe a quantidade de pernas: ");
        int pernas = teclado.nextInt();

        String tipo;
        switch (pernas) {
            case 1:
            tipo = "Saci";
            break;
            
            case 2:
            tipo = "Bipede";
            break;

            case 3:
            tipo = "Tripe";
            break;

            case 4:
            tipo = "Quadrupede";
            break;

            case 6:
            tipo = "Aranha";
            break;
            
            case 8:
            tipo = "Aranha";
            break;

            default:
            tipo = "E.T";
                break;
        }

        // Exibindo o tipo para o usuário  
        System.out.println("Isso é um(a) : " + tipo);
    
        teclado.close();
    }
}
