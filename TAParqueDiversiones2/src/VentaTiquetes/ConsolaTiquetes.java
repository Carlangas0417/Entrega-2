package VentaTiquetes;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import CatalogoAtracciones.Atraccion;
import GestionEmpleados.Cliente;
import Util.Fecha;
import Util.RangoFechas;

public class ConsolaTiquetes {

    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        ConsolaTiquetes consola = new ConsolaTiquetes();
        consola.ejecutar();
    }

    public void ejecutar() {
        while (true) {
            System.out.println("\n=== SISTEMA DE VENTA DE TIQUETES ===");
            System.out.println("1. Vender tiquete");
            System.out.println("2. Salir");
            System.out.print("Seleccione una opción: ");
            String opcion = sc.nextLine();

            if (opcion.equals("1")) {
                venderTiquete();
            } else if (opcion.equals("2")) {
                System.out.println("Hasta pronto.");
                break;
            } else {
                System.out.println("Opción inválida.");
            }
        }
    }

    private void venderTiquete() {
        System.out.println("\n¿Venta en:");
        System.out.println("1. Línea");
        System.out.println("2. Taquilla");
        System.out.print("Seleccione una opción: ");
        String tipoVenta = sc.nextLine();

        VentaTiquete venta;
        if (tipoVenta.equals("1")) {
            venta = new VentaOnline(false);
        } else if (tipoVenta.equals("2")) {
            venta = new VentaTaquilla(false);
        } else {
            System.out.println("Opción inválida.");
            return;
        }

        Cliente cliente = seleccionarCliente();
        if (cliente == null) {
            System.out.println("Cliente no encontrado.");
            return;
        }

        String exclusividad = seleccionarExclusividad();
        List<TipoTiquete> modalidades = seleccionarModalidades();

        Tiquete tiquete = venta.venderTiquete(cliente, exclusividad, modalidades);

        System.out.println("Tiquete generado:");
        System.out.println("ID: " + tiquete.getId());
        System.out.println("Exclusividad: " + tiquete.getExclusividad());
        System.out.println("Modalidades:");
        for (TipoTiquete t : tiquete.getModalidades()) {
            System.out.println("- " + t.tipo());
        }
    }

    private Cliente seleccionarCliente() {
        System.out.print("Ingrese su login: ");
        String login = sc.nextLine();
        return Cliente.clientesInfoCompletitud.get(login);
    }

    private String seleccionarExclusividad() {
        System.out.println("Seleccione tipo de exclusividad:");
        System.out.println("- BASICO");
        System.out.println("- FAMILIAR");
        System.out.println("- ORO");
        System.out.println("- DIAMANTE");

        while (true) {
            System.out.print("Opción: ");
            String input = sc.nextLine().toUpperCase();
            if (input.equals("BASICO") || input.equals("FAMILIAR") || input.equals("ORO") || input.equals("DIAMANTE")) {
                return input;
            } else {
                System.out.println("Valor inválido. Intente de nuevo.");
            }
        }
    }


    private List<TipoTiquete> seleccionarModalidades() {
        List<TipoTiquete> modalidades = new ArrayList<>();
        while (true) {
            System.out.println("\nSeleccione modalidad a agregar:");
            System.out.println("1. Temporada");
            System.out.println("2. Individual");
            System.out.println("3. FastPass");
            System.out.println("4. Finalizar");
            System.out.print("Opción: ");
            String op = sc.nextLine();

            switch (op) {
                case "1":
                    modalidades.add(crearTemporada());
                    break;
                case "2":
                    modalidades.add(crearIndividual());
                    break;
                case "3":
                    modalidades.add(crearFastPass());
                    break;
                case "4":
                    return modalidades;
                default:
                    System.out.println("Opción inválida.");
            }
        }
    }

    private TipoTiquete crearTemporada() {
        System.out.println("Ingrese fecha de inicio:");
        Fecha inicio = leerFecha();
        System.out.println("Ingrese fecha de fin:");
        Fecha fin = leerFecha();
        System.out.print("Descuento aplicado (%): ");
        int desc = Integer.parseInt(sc.nextLine());
        return new Temporada(new RangoFechas(inicio, fin), desc);
    }


    private TipoTiquete crearFastPass() {
        System.out.println("Ingrese la fecha del FastPass:");
        Fecha f = leerFecha();
        return new FastPass(f);
    }

    private Fecha leerFecha() {
        System.out.print("Día: ");
        int d = Integer.parseInt(sc.nextLine());
        System.out.print("Mes: ");
        int m = Integer.parseInt(sc.nextLine());
        System.out.print("Año: ");
        int a = Integer.parseInt(sc.nextLine());
        return new Fecha(d, m, a);
    }
}
