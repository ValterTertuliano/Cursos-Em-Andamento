/*
 * usando continue dentro  de um laço de repetição para voltar
 * para o inicio do laço
 * 
 * usando break dentro do laço para sair do laço
 */

public class aula_11a {
    public static void main(String[] args) {
        
        int cc = 0;

        while (cc<10) {
            cc++;
            if (cc == 5 || cc == 7) {
                continue;
            } if (cc == 9) {
                break;
            }
            System.out.println("C: " + cc);
        }

    }
}
