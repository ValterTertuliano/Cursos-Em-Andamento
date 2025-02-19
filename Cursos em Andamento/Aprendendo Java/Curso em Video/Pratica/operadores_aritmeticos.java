/*
 * Os operadores aritméticos são usados em expressões 
 * matemáticas, da mesma forma que são utilizados na álgebra
 * 
 */

public class operadores_aritmeticos {
    public static void main(String[] args) {
        
        // declarando variaveis A e B para exemplificar os operadores aritmeticos
        int a = 10;
        int b = 20;
        
        int adicao = a + b;// saida : 30
        int subtracao = a - b; // saida : -10
        int multiplicacao = a * b; // saida : 200
        int divisao = b / a; // saida : 2
        int resto_da_divisao = b % a; // saida : 0
        
        // incrementar dentro de uma varivel não funcionou
        b++;
        a--;

        // agora passo os valores incrementados a outras variaveis poderia ter feito no print, mas assim sinto mais presença
        int incrementa = b; // saida: 21
        int decrementa = a; // saida: 9

                // Exibindo as variáveis
                System.out.println("a = " + a);
                System.out.println("b = " + b);
                System.out.println("adicao = " + adicao);
                System.out.println("subtracao = " + subtracao);
                System.out.println("multiplicacao = " + multiplicacao);
                System.out.println("divisao = " + divisao);
                System.out.println("resto_da_divisao = " + resto_da_divisao);
                System.out.println("incrementa = " + incrementa);
                System.out.println("decrementa = " + decrementa);
    }
}
