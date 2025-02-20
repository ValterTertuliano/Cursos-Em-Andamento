/*
 * O Java define vários operadores bitwise, que podem ser 
 * aplicados a tipos inteiros como long, int, short, char, e 
 * byte.
 *  Esses operadores funcionam diretamente nos bits dos
 * valores e realizam operações bit a bit. Por exemplo,
 * considere que temos os seguintes valores em binário:
 * Valores em binário:
 * a = 60 → 0011 1100
 * b = 13 → 0000 1101
 */

public class OperadoresBitwise {
    public static void main(String[] args) {
        int a = 60; // 0011 1100
        int b = 13; // 0000 1101

        int and = a & b; // 0000 1100
        int or = a | b;  // 0011 1101
        int xor = a ^ b; // 0011 0001
        int notA = ~a;   // 1100 0011 (valores negativos devido à representação em complemento de dois)

        System.out.println("a & b (E bit a bit): " + and);
        System.out.println("a | b (OU bit a bit): " + or);
        System.out.println("a ^ b (OU Exclusivo bit a bit): " + xor);
        System.out.println("~a (Negação bit a bit): " + notA);
    }
}
