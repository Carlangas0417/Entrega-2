package CatalogoAtracciones;

import java.awt.Dialog;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import ConsolaGeneral.CGeneral;
import GestionEmpleados.Cafeteria;
import GestionEmpleados.Cajero;
import GestionEmpleados.Cocinero;
import GestionEmpleados.Empleado;
import GestionEmpleados.Operador;
import GestionEmpleados.Turno;

public class ConsolaAtracciones extends CGeneral {
	
	public static void main(String[] args) throws IOException {
		Turno turnoDIA = new Turno(700, 1500);
		Turno turnoTARDE = new Turno(1500, 2300);
		
		List<Turno> dia = new ArrayList<Turno>();
		dia.add(turnoDIA);
		List<Turno> tarde = new ArrayList<Turno>();
		tarde.add(turnoTARDE);
		List<Turno> diaTarde = new ArrayList<Turno>();
		diaTarde.add(turnoDIA);
		diaTarde.add(turnoTARDE);
		
		Cocinero Ivan = new Cocinero("Ivan", "123", "hola", "i.van", diaTarde, null);  //cafeteria - Cocinero
		Cajero Carlos = new Cajero("Carlos", "20241010", "hola", "c.arlos", dia, null); //tienda - Cajero
		Cajero Sergio = new Cajero("Sergio", "20201011", "hola", "s.ergio", diaTarde, null); //taquilla - Cajero
		Operador Luisa = new Operador("Luisa", "20241012", "hola", "l.uisa", tarde, false, null, null); //operador medio
		Operador Carla = new Operador("Carla", "20241013", "hola", "c.arla", dia, true, null, null); //operador alto dia
		Operador Alejandro = new Operador("Alejandro", "20241014", "hola", "a.lejandro", diaTarde, true, null, null); //operador alto dia
		
		Cafeteria cafeteria = new Cafeteria(null,"Sur");
		
		
		
		
	    ConsolaAtracciones consola = new ConsolaAtracciones();
	    consola.ejecutar(); 
	    
	}
	

    public void ejecutar() throws IOException{

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        boolean terminado = false;

        while (!terminado) {
            System.out.print("Consola para crear una nueva atracción\n");
            System.out.print("¿Qué tipo de atracción desea?\n");
            System.out.print("1. Mecánica\n");
            System.out.print("2. Cultural\n");
            System.out.print("3. Espectáculo\n");

            String opcion = reader.readLine();

            if (opcion.equals("1")) {
            	System.out.println("Ha elegido atracción mecánica.\n");
            	crearMecanica();
            } 
            
            else if (opcion.equals("2")) {
                System.out.println("Ha elegido atracción Cultural.\n");
                crearCultural();
            } 
            
            else if (opcion.equals("3")) {
                System.out.println("Ha elegido atracción de Espectáculo.");
            } 
            
            else {
                System.out.println("Opción no válida.");
            }

            System.out.print("¿Desea ingresar otra atracción? (s/n): ");
            String respuesta = reader.readLine();
            
            if (respuesta.equalsIgnoreCase("n")) {
                terminado = true;
            }

            System.out.println(); // Salto de línea por estética (jaja)
        }

        System.out.println("Gracias por usar la consola de atracciones.");
    }
    
   
    
    public void crearMecanica() {
    	String nombre = cadena("Ingrese el nombre de la atracción");
        String ubicacion = cadena("Ingrese la ubicación de la atracción");
        
        int cupoMax = natural("Ingrese el cupo máximo de la atracción");
        int empleadosMin = natural("Ingrese el mínimo de empleados para la atracción");

        double alturaMaxima = real("Ingrese la altura máxima para la atracción (m)");
        double alturaMinima = real("Ingrese la altura mínima para la atracción (m)");
        
        while (alturaMaxima <= alturaMinima) {
            System.out.println("El cupo máximo debe ser mayor que el cupo mínimo. Intente nuevamente.");
            alturaMaxima = real("Ingrese la altura máxima para la atracción (m)");
            alturaMinima = real("Ingrese la altura mínima para la atracción (m)");
        }
        
        double pesoMaximo = real("Ingrese el peso máximo para la atracción (kg)");
        double pesoMinimo = real("Ingrese la peso mínimo para la atracción (kg)");
        
        while (pesoMaximo <= pesoMinimo) {
            System.out.println("El cupo máximo debe ser mayor que el cupo mínimo. Intente nuevamente.");
            pesoMaximo = real("Ingrese el peso máximo para la atracción (kg)");
            pesoMinimo = real("Ingrese la peso mínimo para la atracción (kg)");
        }
        
        List<String> disponibleClima = lista("Ingrese el clima en el que la atracción está disponible");
        List<String> contraindicaciones = lista("Ingrese las contraindicaciones de la atracción");
        
        Set<String> riesgosValidos = Set.of("MEDIO", "BAJO");
        String riesgo = revisarSetString(riesgosValidos, "Ingrese el nivel de riesgo de la atracción (MEDIO, ALTO)");
        Set<String> exclusividadValidos = Set.of("FAMILIAR", "ORO", "DIAMANTE", "BASICO");
        String exclusividad = revisarSetString(exclusividadValidos, "Ingrese la exclusividad de la atracción (BASICO, FAMILIAR, ORO, DIAMANTE)");
        
        Mecanica atrMecanica = new Mecanica(nombre, ubicacion, cupoMax, empleadosMin, exclusividad,
        		disponibleClima, alturaMaxima, alturaMinima, pesoMaximo, pesoMinimo, contraindicaciones, riesgo, null);
        //////////REVISAR ESE NULL CUANDO YA ESTÉ BIEN LO DE EMPLEADOS
        
        atrMecanica.mostrarMecanica();
        
        System.out.println("¡Atracción creada con éxito!\n");
        
    }
    
    public void crearCultural() {
    	String nombre = cadena("Ingrese el nombre de la atracción");
        String ubicacion = cadena("Ingrese la ubicación de la atracción");
        
        int cupoMax = natural("Ingrese el cupo máximo de la atracción");
        int empleadosMin = natural("Ingrese el mínimo de empleados para la atracción");
        
        Set<String> exclusividadValidos = Set.of("FAMILIAR", "ORO", "DIAMANTE", "BASICO");
        String exclusividad = revisarSetString(exclusividadValidos, "Ingrese la exclusividad de la atracción (BASICO, FAMILIAR, ORO, DIAMANTE)");
        List<String> disponibleClima = lista("Ingrese el clima en el que la atracción está disponible");
        List<Empleado> empleados = null;
        //////////REVISAR ESE NULL CUANDO YA ESTÉ BIEN LO DE EMPLEADOS
        
        
        Cultural atrCultural = new  Cultural(nombre, ubicacion, cupoMax, empleadosMin, exclusividad, disponibleClima, null);
        
        atrCultural.mostrarCultural();
        
        System.out.println("¡Atracción creada con éxito!\n");
        
    }
    
    
}
