/*
 * O compilador converte automaticamente um tipo menor para 
 * um tipo maior, presevervando a informação
 * Conversão Ampliada (Widening Casting) – Feita
 * automaticamente, converte um tipo menor para um tipo maior
 * Exemplo de hierarquia: ( maior para menor ) 
 * byte -> short -> char -> int -> long -> float -> double
 */

public class conversao_ampliada {

    public static void main(String[] args) {
        int inteiro = 5;
        double flutuante = 2.5;

        //podemos converter o tipo respeitando a hieraquia tranquilamente
        double converter_inteiro = inteiro;
        System.out.println(inteiro + " int - double " + converter_inteiro);

        // aqui a conversão é feita automaticamente de int para double
        double soma = inteiro + flutuante; 
        System.out.println("A soma de " + inteiro + " + " + flutuante + " é igual a " + soma);
    }
}