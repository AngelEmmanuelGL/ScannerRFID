import java.util.Scanner;
public class cola {
    static int[] cola;
    static int primero;
    static int ultimo;
    static int longitud;
    public static void main(String[]arg){
        iniciaCola(5);
        char resp;
        Scanner sc = new Scanner(System.in);
        do{
            System.out.println("""
                    1: Insertar
                    2: Eliminar
                    3: Salir
                    """);
                    resp = sc.next().charAt(0);
            switch (resp) {
                case '1':
                    System.out.println("insertar un numero: ");
                    int dato = sc.nextInt();
                    insertar(dato);
                    break;
                case '2':
                    if(colaVacia()){
                        System.out.println("No hay elementos");
                    }else{
                        dato = eliminar();
                        System.out.println("Dato eliminado: "+dato);
                    }
                    break;
            }
        }while(resp != '3');
    }
    public static void iniciaCola(int longitud){
        cola = new int[longitud];
        primero = 0;
        ultimo = -1;
        this.longitud; 
    }
    public static Boolean colaVacia(){
        return true;
    }
    public static int eliminar(){
        return 0;
    }
    public static void insertar(int dato){

    }
}
