package CatalogoAtracciones;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import ConsolaGeneral.CGeneral;
import Exceptions.AsignacionInvalidaException;
import GestionEmpleados.*;
import Persistencia.PersistenciaAtracciones;

public class ConsolaAtracciones extends CGeneral {

    private List<Mecanica> mecanicas = new ArrayList<>();
    private List<Operador> operadores = new ArrayList<>();
    Administrador elAdmin = new Administrador("El Admin", "002200202", "lalalal", "el.admin", null);
    private List<Atraccion> atracciones = new ArrayList<>();

    public static void main(String[] args) throws IOException {
    	
    	
        Turno turnoDIA = new Turno(700, 1500);
        Turno turnoTARDE = new Turno(1500, 2300);

        List<Turno> dia = new ArrayList<>();
        dia.add(turnoDIA);
        List<Turno> tarde = new ArrayList<>();
        tarde.add(turnoTARDE);
        List<Turno> diaTarde = new ArrayList<>();
        diaTarde.add(turnoDIA);
        diaTarde.add(turnoTARDE);

        Operador luisa = new Operador("Luisa", "20241012", "hola", "l.uisa", tarde, false, null, 1);
        luisa.anadirAtraccionEntrenado(1);

        Operador carla = new Operador("Carla", "20241013", "hola", "c.arla", dia, true, null, 2);
        carla.anadirAtraccionEntrenado(2);

        Operador alejandro = new Operador("Alejandro", "20241014", "hola", "a.lejandro", diaTarde, true, null, 3);
        alejandro.anadirAtraccionEntrenado(2);
        alejandro.anadirAtraccionEntrenado(3);

        Mecanica gusanito = new Mecanica("Gusanito", "Norte", 10, 1, "BASICO", null, 1.80, 1.30, 90, 20, null, "MEDIO", null);
        gusanito.anadirClima("SOLEADO");
        gusanito.anadirContraindicacion("NINGUNA");

        Mecanica martillo = new Mecanica("Martillo", "Sur", 30, 2, "BASICO", null, 2, 1.50, 100, 20, null, "ALTO", null);
        martillo.anadirClima("SOLEADO");
        martillo.anadirContraindicacion("CARDIACO");

        Mecanica montanaRusa = new Mecanica("Montaña Rusa", "Oeste", 40, 1, "BASICO", null, 1.80, 1.30, 90, 20, null, "ALTO", null);
        montanaRusa.anadirClima("SOLEADO");
        montanaRusa.anadirContraindicacion("CARDIACO");

        ConsolaAtracciones consola = new ConsolaAtracciones();
        consola.mecanicas.addAll(Arrays.asList(gusanito, martillo, montanaRusa));
        consola.operadores.addAll(Arrays.asList(luisa, carla, alejandro));
        consola.ejecutar();
    }

    public void ejecutar() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        boolean terminado = false;

        while (!terminado) {
            System.out.print("Consola atracciones\n");
            System.out.print("1. Creación de atracciones.\n");
            System.out.print("2. Asignación de empleados a atracciones preexistentes.\n");
            System.out.print("3. Ver atracciones creadas.\n");

            String anteopcion = reader.readLine();

            if (anteopcion.equals("1")) {
                System.out.print("¿Qué tipo de atracción desea crear?\n");
                System.out.print("1. Mecánica\n");
                System.out.print("2. Cultural\n");
                System.out.print("3. Espectáculo\n");

                String opcion = reader.readLine();

                if (opcion.equals("1")) {
                    System.out.println("Ha elegido atracción mecánica.\n");
                    crearMecanica();
                } else if (opcion.equals("2")) {
                    System.out.println("Ha elegido atracción Cultural.\n");
                    crearCultural();
                } else if (opcion.equals("3")) {
                    System.out.println("Ha elegido atracción de Espectáculo.");
                    crearEspectaculo();
                } else {
                    System.out.println("Opción no válida.");
                }

                System.out.print("¿Desea realizar otra operación? (s/n): ");
                String respuesta = reader.readLine();
                if (respuesta.equalsIgnoreCase("n")) {
                    terminado = true;
                }

            } else if (anteopcion.equals("2")) {
                asignarEmpleadoAtraccion(reader);
            } else if (anteopcion.equals("3")) {
                cargarAtraccionConsola();
            } 
            else {
                System.out.println("La opción digitada no es válida.");
            }

            System.out.println();
        }

        System.out.println("Gracias por usar la consola de atracciones.");
    }

    public void asignarEmpleadoAtraccion(BufferedReader reader) throws IOException {
        while (true) {
            System.out.println("Lista de atracciones disponibles:");
            for (int i = 0; i < mecanicas.size(); i++) {
                System.out.println((i + 1) + ". " + mecanicas.get(i).getNombre() + ". " + " Riesgo de la atracción: " + mecanicas.get(i).nivelRiesgo + ". " + " ID de la atracción: " + mecanicas.get(i).id);
            }

            int indexAtraccion = natural("Seleccione el número de la atracción") - 1;
            if (indexAtraccion < 0 || indexAtraccion >= mecanicas.size()) {
                System.out.println("Índice inválido. Intente nuevamente.");
                continue;
            }

            Mecanica seleccionada = mecanicas.get(indexAtraccion);

            System.out.println("Lista de operadores disponibles:");
            for (int i = 0; i < operadores.size(); i++) {
                System.out.println((i + 1) + ". " + operadores.get(i).getNombre() + ". " + " Operador de riesgo alto: " + operadores.get(i).isRiesgoAlto() + ". " + " IDs de atracciones entrenado: " + operadores.get(i).getAtraccionesEntrenado());
            }

            int indexEmpleado = natural("Seleccione el número del operador") - 1;
            if (indexEmpleado < 0 || indexEmpleado >= operadores.size()) {
                System.out.println("Índice inválido. Intente nuevamente.");
                continue;
            }

            Operador operador = operadores.get(indexEmpleado);

            try {
                elAdmin.asignarOperador(operador, seleccionada);
                break;
            } catch (AsignacionInvalidaException e) {
                System.out.println("Error en la asignación: " + e.getMessage() + "\n");
            }
        }
    }

    public void crearMecanica() {
        String nombre = cadena("Ingrese el nombre de la atracción");
        String ubicacion = cadena("Ingrese la ubicación de la atracción");

        int cupoMax = natural("Ingrese el cupo máximo de la atracción");
        int empleadosMin = natural("Ingrese el mínimo de empleados para la atracción");

        double alturaMaxima = real("Ingrese la altura máxima para la atracción (m)");
        double alturaMinima = real("Ingrese la altura mínima para la atracción (m)");
        while (alturaMaxima <= alturaMinima) {
            System.out.println("La altura máxima debe ser mayor que la mínima.");
            alturaMaxima = real("Ingrese la altura máxima para la atracción (m)");
            alturaMinima = real("Ingrese la altura mínima para la atracción (m)");
        }

        double pesoMaximo = real("Ingrese el peso máximo para la atracción (kg)");
        double pesoMinimo = real("Ingrese la peso mínimo para la atracción (kg)");
        while (pesoMaximo <= pesoMinimo) {
            System.out.println("El peso máximo debe ser mayor que el mínimo.");
            pesoMaximo = real("Ingrese el peso máximo para la atracción (kg)");
            pesoMinimo = real("Ingrese la peso mínimo para la atracción (kg)");
        }

        List<String> disponibleClima = lista("Ingrese el clima en el que la atracción está disponible");
        List<String> contraindicaciones = lista("Ingrese las contraindicaciones de la atracción");

        Set<String> riesgosValidos = Set.of("MEDIO", "BAJO", "ALTO");
        String riesgo = revisarSetString(riesgosValidos, "Ingrese el nivel de riesgo de la atracción (BAJO, MEDIO, ALTO)");
        Set<String> exclusividadValidos = Set.of("FAMILIAR", "ORO", "DIAMANTE", "BASICO");
        String exclusividad = revisarSetString(exclusividadValidos, "Ingrese la exclusividad de la atracción (BASICO, FAMILIAR, ORO, DIAMANTE)");

        Mecanica atrMecanica = new Mecanica(nombre, ubicacion, cupoMax, empleadosMin, exclusividad,
                disponibleClima, alturaMaxima, alturaMinima, pesoMaximo, pesoMinimo, contraindicaciones, riesgo, null);
        
        for (int i = 0; i < disponibleClima.size(); i++) {
            atrMecanica.anadirClima(disponibleClima.get(i));
        }

        for (int i = 0; i < contraindicaciones.size(); i++) {
            atrMecanica.anadirContraindicacion(contraindicaciones.get(i)); 
        }

        atrMecanica.mostrarAtraccion();
        mecanicas.add(atrMecanica);

        System.out.println("¡Atracción creada con éxito!\n");
        
        try {
			PersistenciaAtracciones.guardarAtraccion(atrMecanica, "Persistencia.dat");
		} catch (Exception e) {
			System.out.println("Error al guardar los datos");
			e.printStackTrace();
		}
    }

    public void crearCultural() {
        String nombre = cadena("Ingrese el nombre de la atracción");
        String ubicacion = cadena("Ingrese la ubicación de la atracción");

        int cupoMax = natural("Ingrese el cupo máximo de la atracción");
        int empleadosMin = natural("Ingrese el mínimo de empleados para la atracción");

        Set<String> exclusividadValidos = Set.of("FAMILIAR", "ORO", "DIAMANTE", "BASICO");
        String exclusividad = revisarSetString(exclusividadValidos, "Ingrese la exclusividad de la atracción (BASICO, FAMILIAR, ORO, DIAMANTE)");
        List<String> disponibleClima = lista("Ingrese el clima en el que la atracción está disponible");

        Cultural atrCultural = new Cultural(nombre, ubicacion, cupoMax, empleadosMin, exclusividad, disponibleClima, null);
        for (int i = 0; i < disponibleClima.size(); i++) {
        	atrCultural.anadirClima(disponibleClima.get(i));
        }
        
        atrCultural.mostrarAtraccion();

        System.out.println("¡Atracción creada con éxito!\n");
        
        try {
			PersistenciaAtracciones.guardarAtraccion(atrCultural, "Persistencia.dat");
		} catch (Exception e) {
			System.out.println("Error al guardar los datos");
			e.printStackTrace();
		}
    }
    
    public void crearEspectaculo() {
        
        List<Horario> horarios = new ArrayList<>();
        String respuestaHorarios = "s";

        while (respuestaHorarios.equalsIgnoreCase("s")) {
            String input = cadena("Ingrese un horario (formato HH:mm)");
            try {
                horarios.add(new Horario(input));
                respuestaHorarios = cadena("¿Desea agregar otro horario? (s/n)");
            } catch (IllegalArgumentException e) {
                System.out.println("Horario inválido: " + input + ". " + e.getMessage());
            }
            
        }

        List<Fecha> fechas = new ArrayList<>();
        String respuestaFechas = "s";

        while (respuestaFechas.equalsIgnoreCase("s")) {
            String input = cadena("Ingrese una fecha (formato yyyy-MM-dd)");
            try {
                fechas.add(new Fecha(input));
                respuestaFechas = cadena("¿Desea agregar otra fecha? (s/n)");
            } catch (IllegalArgumentException e) {
                System.out.println("Fecha inválida: " + input + ". " + e.getMessage());
            }
            
        }

     
        boolean disponible = false;
        while (true) {
            String dispo = cadena("¿Está disponible actualmente? (SI/NO)").toUpperCase();
            if (dispo.equals("SI")) {
                disponible = true;
                break;
            } else if (dispo.equals("NO")) {
                disponible = false;
                break;
            } else {
                System.out.println("Respuesta inválida. Por favor, escriba SI o NO.");
            }
        }
        

        Espectaculo espectaculo = new Espectaculo(horarios, fechas, disponible);
        System.out.println("¡Espectáculo creado exitosamente!\n");
        espectaculo.mostrarEspectaculo();

    }
    
    public void cargarAtraccionConsola() {
        try {
            Atraccion atraccionCargada = PersistenciaAtracciones.cargarAtraccion("Persistencia.dat");

            if (atraccionCargada != null) {
                System.out.println("Atracción más reciente: \n");
                atraccionCargada.mostrarAtraccion();
                this.atracciones.add(atraccionCargada);
                System.out.println("\n");
            }
            if ()

        } catch (Exception e) {
            System.out.println("Error al cargar los datos");
            e.printStackTrace();
        }
    }


}
