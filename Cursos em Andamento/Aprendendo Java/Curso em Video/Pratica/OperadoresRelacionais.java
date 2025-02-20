/*
 * Os operadores relacionais comparam dois valores e retornam 
 * um valor booleano (true ou false).
 */

public class OperadoresRelacionais {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;

        boolean igual = (a == b); // false
        boolean diferente = (a != b); // true
        boolean maior = (a > b); // false
        boolean menor = (a < b); // true
        boolean maior_ou_igual = (a >= b); // false
        boolean menor_ou_igual = (a <= b); // true

        System.out.println("a == b: " + igual);
        System.out.println("a != b: " + diferente);
        System.out.println("a > b: " + maior);
        System.out.println("a < b: " + menor);
        System.out.println("a >= b: " + maior_ou_igual);
        System.out.println("a <= b: " + menor_ou_igual);
    }
}
