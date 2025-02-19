/*
 * Conversão Reduzida (Narrowing Casting) – Deve ser feita
 * manualmente, convertendo um tipo maior para um tipo menor
 * 
 * Exemplo de hierarquia:
 * double -> float -> long -> int -> char -> short -> byte
 * 
 * Ao converter um tipo maior para um menor, a conversão deve
 * ser feita manualmente, colocando o tipo desejado entre
 * parênteses antes do valor
*/

public class conversao_reduzida {
    public static void main(String[] args) {
        
        double flutuante = 9.78;

        // Conversão manual: double para int usando typecast
        int converterInteiro = (int) flutuante;

        System.out.println(flutuante);
        System.out.println(converterInteiro);
    }
}
